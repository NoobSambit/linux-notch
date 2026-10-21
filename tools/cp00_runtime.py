#!/usr/bin/env python3
"""Exact-instance controls and disposable-store recovery, INSIDE the CP-00 sandbox."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import time

LAB = Path('/lab')
HOME_DIR = Path('/home/cp00')
BACKUPS = Path('/backups')
SOURCE = os.environ.get('CP00_SOURCE_PATH', '/original')
CONFIG = SOURCE + '/shell.qml'
REVISION = os.environ.get('CP00_SOURCE_REVISION', 'ff520e33e136bbce11b7100c69888dedf42f7273')
STORES = ['.local/state/k4', '.config/k4', '.config/k4term']


def execute(command):
    r = subprocess.run(command, capture_output=True, text=True, timeout=15)
    if r.returncode:
        raise RuntimeError(f'{command!r} exited {r.returncode}: {r.stdout}{r.stderr}')
    return r.stdout


def instances():
    raw = execute(['quickshell', 'list', '--all', '--json'])
    # Installed 0.2.1 prints this sentence even when --json was requested.
    return [] if raw.strip() == 'No running instances.' else json.loads(raw)


def process_identity(pid):
    proc = Path('/proc', str(pid))
    tail = proc.joinpath('stat').read_text().rsplit(')', 1)[1].split()
    if tail[0] == 'Z':
        raise ProcessLookupError(pid)
    return {'pid': pid, 'start_ticks': tail[19],
            'exe': str(proc.joinpath('exe').resolve()),
            'argv': [v.decode() for v in proc.joinpath('cmdline').read_bytes().split(b'\0')[:-1]],
            'pid_namespace': os.readlink(proc / 'ns/pid')}


def environment():
    assert os.environ['HOME'] == str(HOME_DIR)
    assert not Path('/home/noobsambit').exists() and not Path('/parent').exists()
    return {key: os.environ[key] for key in ['WAYLAND_DISPLAY', 'HYPRLAND_INSTANCE_SIGNATURE',
                                           'DBUS_SESSION_BUS_ADDRESS', 'XDG_RUNTIME_DIR']}


def record(instance, log=None):
    assert instance['config_path'] == CONFIG
    value = {'instance': instance, 'process': process_identity(instance['pid']),
             'environment': environment(), 'revision': REVISION}
    if log:
        value['log'] = str(log)
    LAB.joinpath('k4.json').write_text(json.dumps(value, indent=2) + '\n')
    return value


def verify(handle):
    expected = handle['instance']
    matches = [i for i in instances() if i['id'] == expected['id']]
    if not matches:
        return False
    if expected['config_path'] != CONFIG:
        raise RuntimeError('Refusing foreign configuration')
    if handle['environment'] != environment() or handle['revision'] != REVISION:
        raise RuntimeError('Refusing changed session or source revision')
    if len(matches) != 1 or matches[0] != expected:
        raise RuntimeError('Refusing changed full instance identity')
    if process_identity(expected['pid']) != handle['process']:
        raise RuntimeError('Refusing changed PID/start time/executable/arguments/namespace')
    return True


def current():
    handle = json.loads(LAB.joinpath('k4.json').read_text())
    if not verify(handle):
        raise RuntimeError('Recorded full instance ID is absent; no replacement selected')
    return handle


def start():
    environment()
    # The immutable export is verified against Git archive bytes before every launch.
    manifest = json.loads(Path(os.environ.get('CP00_SOURCE_MANIFEST', '/lab/source-manifest.json')).read_text())
    assert manifest['revision'] == REVISION
    for name, digest in manifest['files'].items():
        assert hashlib.sha256(Path(SOURCE, name).read_bytes()).hexdigest() == digest, name
    if any(i['config_path'] == CONFIG for i in instances()):
        raise RuntimeError('Original config already running; refusing unrecorded/default selection')
    log = LAB.joinpath('logs', 'k4-' + str(time.time_ns()) + '.txt')
    with log.open('w') as output:
        child = subprocess.Popen(['sh', SOURCE + '/arrancar', '--no-color'],
                                 stdin=subprocess.DEVNULL, stdout=output, stderr=output, close_fds=True)
    for _ in range(100):
        found = [i for i in instances() if i['pid'] == child.pid and i['config_path'] == CONFIG]
        if found:
            value = record(found[0], log)
            ready = subprocess.run(['quickshell', 'ipc', '--id', found[0]['id'], 'show'],
                                   capture_output=True, text=True, timeout=5)
            if ready.returncode or 'target k4\n' not in ready.stdout:
                time.sleep(.1)
                continue
            print(json.dumps(value, indent=2))
            return
        if child.poll() is not None:
            raise RuntimeError('Original startup failed: ' + log.read_text())
        time.sleep(.05)
    raise RuntimeError('Startup discovery timed out; inspect exact child PID ' + str(child.pid))


def stop():
    if not LAB.joinpath('k4.json').exists():
        if any(i['config_path'] == CONFIG for i in instances()):
            raise RuntimeError('Unrecorded original instance exists; refusing to choose one')
        print('Already stopped; no recorded instance')
        return
    handle = json.loads(LAB.joinpath('k4.json').read_text())
    if not verify(handle):
        print('Already stopped; recorded full ID absent. No replacement touched.')
        return
    pid = handle['instance']['pid']
    fd = os.pidfd_open(pid)
    try:
        if not verify(handle):
            raise RuntimeError('Identity disappeared before stop')
        result = subprocess.run(['quickshell', 'kill', '--id', handle['instance']['id']],
                                capture_output=True, text=True, timeout=10)
        if result.returncode:
            if not verify(handle):
                return
            signal.pidfd_send_signal(fd, signal.SIGTERM)
        for _ in range(100):
            try:
                if process_identity(pid) != handle['process']:
                    break
            except (FileNotFoundError, ProcessLookupError):
                break
            time.sleep(.05)
        else:
            # Escalation remains confined to the same pinned, reverified test process.
            if verify(handle):
                signal.pidfd_send_signal(fd, signal.SIGKILL)
            time.sleep(.1)
        if any(i['id'] == handle['instance']['id'] for i in instances()):
            raise RuntimeError('Recorded instance still listed after stop')
    finally:
        os.close(fd)
    print('Stopped only full ID ' + handle['instance']['id'])


def digest_tree(root):
    values = {}
    for p in sorted(root.rglob('*')):
        if p.is_symlink():
            raise RuntimeError('Refusing symlink in disposable backup: ' + str(p))
        if p.is_file():
            values[str(p.relative_to(root))] = hashlib.sha256(p.read_bytes()).hexdigest()
    return values


def snapshot(name):
    if not name or any(c not in 'abcdefghijklmnopqrstuvwxyz0123456789-' for c in name):
        raise ValueError('Snapshot name must use lowercase letters, digits and hyphens')
    return BACKUPS / name


def backup(name, quiet=False):
    environment()
    if any(i['config_path'] == CONFIG for i in instances()):
        raise RuntimeError('Stop original before snapshot')
    target = snapshot(name)
    target.mkdir(mode=0o700)  # Immutable; never replace a previous snapshot.
    for relative in STORES:
        source = HOME_DIR / relative
        if source.exists():
            if source.is_symlink() or any(p.is_symlink() for p in source.parents):
                raise RuntimeError('Refusing redirected disposable store')
            digest_tree(source)  # Reject links before copying.
            shutil.copytree(source, target / 'home' / relative)
    store = target / 'home'
    store.mkdir(exist_ok=True)
    manifest = {'revision': REVISION, 'stores': STORES, 'files': digest_tree(store)}
    target.joinpath('manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    if not quiet:
        print(json.dumps({'snapshot': str(target), 'manifest': manifest}, indent=2))


def restore(name):
    stop()
    target = snapshot(name)
    manifest = json.loads(target.joinpath('manifest.json').read_text())
    if manifest['revision'] != REVISION or manifest['stores'] != STORES:
        raise RuntimeError('Snapshot does not match original source/store scope')
    if digest_tree(target / 'home') != manifest['files']:
        raise RuntimeError('Snapshot checksum mismatch; no state changed')
    retained = 'before-restore-' + str(time.time_ns())
    backup(retained, quiet=True)
    for relative in STORES:
        dest = HOME_DIR / relative
        source = target / 'home' / relative
        if dest.is_symlink() or any(p.is_symlink() for p in dest.parents):
            raise RuntimeError('Refusing redirected state path')
        if dest.exists():
            shutil.rmtree(dest)  # Only allowlisted, verified disposable directories.
        if source.exists():
            shutil.copytree(source, dest)
    # Compare the entire restored store set, including plugin, clipboard and Shelf fixtures.
    restored = {}
    for relative in STORES:
        if (HOME_DIR / relative).exists():
            restored.update({relative + '/' + k: v for k, v in digest_tree(HOME_DIR / relative).items()})
    assert restored == manifest['files']
    print('Restored matching disposable snapshot; retained current state in ' + retained)
    start()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['start', 'stop', 'status', 'ipc', 'backup', 'restore'])
    parser.add_argument('arguments', nargs=argparse.REMAINDER)
    args = parser.parse_args()
    if args.action == 'start':
        start()
    elif args.action == 'stop':
        stop()
    elif args.action == 'status':
        print(json.dumps(current(), indent=2))
    elif args.action == 'ipc':
        h = current()
        print(execute(['quickshell', 'ipc', '--id', h['instance']['id']] + args.arguments))
    elif args.action == 'backup':
        backup(args.arguments[0])
    elif args.action == 'restore':
        restore(args.arguments[0])


if __name__ == '__main__':
    main()
