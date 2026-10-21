#!/usr/bin/env python3
"""CP-00 disposable runtime. Never installs or changes the owner's session config.

Two independent bubblewrap sandboxes share only dummy home/runtime/lab files.
Only the compositor sandbox receives a parent display socket. The command server
and all application descendants have no mount or process path to that socket.
"""
from __future__ import annotations

import argparse
import datetime
import json
import os
from pathlib import Path
import signal
import socket
import socketserver
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent.parent
LAB = ROOT / 'scratch/cp00/lab'
BASELINE = 'ff520e33e136bbce11b7100c69888dedf42f7273'


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def identity(pid):
    p = Path('/proc') / str(pid)
    stat = p.joinpath('stat').read_text().rsplit(')', 1)[1].split()
    if stat[0] == 'Z':
        raise ProcessLookupError(pid)
    return {'pid': pid, 'start_ticks': stat[19],
            'exe': str(p.joinpath('exe').resolve()),
            'pid_namespace': os.readlink(p / 'ns/pid'),
            'argv': p.joinpath('cmdline').read_bytes().split(b'\0')[:-1]}


def save_identity(name, pid):
    i = identity(pid)
    i['argv'] = [s.decode() for s in i['argv']]
    i['date'] = now()
    LAB.joinpath(name + '.json').write_text(json.dumps(i, indent=2) + '\n')


def save_payload(name, wrapper_pid, argv):
    """Record the payload, not bwrap's forwarding wrapper (which can orphan init)."""
    for _ in range(100):
        pending = [wrapper_pid]
        while pending:
            pid = pending.pop()
            try:
                i = identity(pid)
                if i['argv'] == [s.encode() for s in argv]:
                    if Path('/proc', str(pid), 'root/lab').stat().st_ino != LAB.stat().st_ino:
                        raise RuntimeError('Payload does not use our lab')
                    save_identity(name, pid)
                    return
                pending += [int(s) for s in Path('/proc', str(pid), 'task', str(pid), 'children').read_text().split()]
            except (FileNotFoundError, ProcessLookupError):
                pass
        time.sleep(.05)
    raise RuntimeError('Payload not found; inspect exact wrapper ' + str(wrapper_pid))


def stop_verified(name):
    file = LAB / (name + '.json')
    if not file.exists():
        return 'already stopped (no recorded handle)'
    old = json.loads(file.read_text())
    try:
        current = identity(old['pid'])
    except (FileNotFoundError, ProcessLookupError):
        return 'already stopped (recorded process absent)'
    current['argv'] = [s.decode() for s in current['argv']]
    if any(current[k] != old[k] for k in ['pid', 'start_ticks', 'exe', 'argv', 'pid_namespace']):
        raise RuntimeError('Refusing changed process identity: ' + name)
    if Path('/proc', str(old['pid']), 'root/lab').stat().st_ino != LAB.stat().st_ino:
        raise RuntimeError('Refusing process outside our lab')
    # pidfd pins the verified process, avoiding PID reuse between check and signal.
    fd = os.pidfd_open(old['pid'])
    try:
        check = identity(old['pid'])
        if check['start_ticks'] != old['start_ticks']:
            raise RuntimeError('Refusing reused PID')
        signal.pidfd_send_signal(fd, signal.SIGTERM)
    finally:
        os.close(fd)
    for _ in range(100):
        try:
            identity(old['pid'])
        except (FileNotFoundError, ProcessLookupError):
            return 'stopped verified ' + name
        time.sleep(.05)
    raise RuntimeError('Verified process did not stop; no broad termination attempted')


def prepare():
    for child in ['home', 'runtime', 'etc', 'logs']:
        LAB.joinpath(child).mkdir(parents=True, exist_ok=True, mode=0o700)
    os.chmod(LAB, 0o700)
    os.chmod(LAB / 'runtime', 0o700)
    LAB.joinpath('etc/passwd').write_text('cp00:x:1000:1000:CP00 disposable user:/home/cp00:/bin/sh\n')
    LAB.joinpath('etc/group').write_text('cp00:x:1000:\n')
    LAB.joinpath('etc/nsswitch.conf').write_text('passwd: files\ngroup: files\nhosts: files\n')
    LAB.joinpath('etc/fonts').mkdir(exist_ok=True)
    LAB.joinpath('etc/ld.so.cache').touch()
    LAB.joinpath('session-bus.conf').write_text('''<busconfig>
<type>session</type><listen>unix:tmpdir=/tmp</listen><auth>EXTERNAL</auth>
<policy context="default">
<allow send_destination="*"/><allow receive_sender="*"/><allow own="*"/>
</policy>
</busconfig>
''')
    LAB.joinpath('hyprland.lua').write_text('''-- CP-00 nested compositor only. No autostart, device bindings or host includes.
hl.monitor({output = "", mode = "1280x720@60", position = "auto", scale = 1})
hl.config({
    general = {gaps_in = 5, gaps_out = 10, border_size = 2},
    animations = {enabled = false},
    misc = {disable_hyprland_logo = true, disable_splash_rendering = true},
    xwayland = {enabled = false},
})
''')
    if not (LAB / 'original').exists():
        # External to either sandbox; only this immutable source export is mounted.
        raise RuntimeError('Prepare source export first: see tools/cp00.md')


def sandbox(compositor=False):
    command = ['bwrap', '--unshare-all', '--unshare-user', '--new-session', '--cap-drop', 'ALL',
               '--ro-bind', '/usr', '/usr', '--symlink', 'usr/bin', '/bin',
               '--symlink', 'usr/lib', '/lib', '--symlink', 'usr/lib', '/lib64',
               '--proc', '/proc', '--dev', '/dev', '--tmpfs', '/tmp',
               '--tmpfs', '/run', '--ro-bind', str(LAB / 'etc'), '/etc',
               '--ro-bind', '/etc/fonts', '/etc/fonts',
               '--ro-bind', '/etc/ld.so.cache', '/etc/ld.so.cache',
               '--ro-bind', '/sys', '/sys',
               '--bind', str(LAB / 'home'), '/home/cp00',
               '--bind', str(LAB / 'runtime'), '/run/cp00',
               '--bind', str(LAB), '/lab',
               '--ro-bind', str(LAB / 'original'), '/original',
               '--ro-bind', str(LAB / 'original'), '/lab/original',
               '--ro-bind', str(Path(__file__).resolve()), '/control.py',
               '--clearenv', '--setenv', 'PATH', '/usr/bin',
               '--setenv', 'HOME', '/home/cp00', '--setenv', 'USER', 'cp00',
               '--setenv', 'LOGNAME', 'cp00', '--setenv', 'LANG', 'C.UTF-8',
               '--setenv', 'XDG_RUNTIME_DIR', '/run/cp00',
               '--setenv', 'XDG_CONFIG_HOME', '/home/cp00/.config',
               '--setenv', 'XDG_STATE_HOME', '/home/cp00/.local/state',
               '--setenv', 'XDG_CACHE_HOME', '/home/cp00/.cache',
               '--setenv', 'QT_QPA_PLATFORM', 'wayland',
               '--setenv', 'QML_IMPORT_PATH', '/original/api',
               '--setenv', 'XDG_SESSION_TYPE', 'wayland',
               '--setenv', 'XDG_CURRENT_DESKTOP', 'Hyprland',
               '--setenv', 'K4_LOG', '0', '--chdir', '/home/cp00']
    # Only render nodes, never DRM card/input/audio/camera devices.
    for node in ['/dev/dri/renderD128', '/dev/dri/renderD129']:
        if Path(node).exists():
            command += ['--dev-bind', node, node]
    if compositor:
        parent = Path(os.environ['XDG_RUNTIME_DIR']) / os.environ['WAYLAND_DISPLAY']
        if not parent.is_socket():
            raise RuntimeError('Parent display socket is absent')
        command += ['--ro-bind', str(parent), '/parent/display',
                    '--setenv', 'WAYLAND_DISPLAY', '/parent/display',
                    '--setenv', 'DBUS_SESSION_BUS_ADDRESS', 'unix:path=/nonexistent',
                    '--setenv', 'HYPRLAND_NO_CRASHREPORTER', '1']
    else:
        command += ['--disable-userns']
    return command


def request(message):
    with socket.socket(socket.AF_UNIX) as client:
        client.settimeout(90)
        client.connect(str(LAB / 'control.sock'))
        client.sendall(json.dumps(message).encode() + b'\n')
        data = bytearray()
        while not data.endswith(b'\n'):
            block = client.recv(65536)
            if not block:
                raise RuntimeError('Command server disconnected')
            data.extend(block)
        return json.loads(data)


def start_server():
    if (LAB / 'control.sock').exists():
        try:
            print(json.dumps(request({'command': ['/usr/bin/true']})))
            return
        except (ConnectionRefusedError, FileNotFoundError):
            LAB.joinpath('control.sock').unlink()
    log = LAB.joinpath('logs/server.txt').open('a')
    proc = subprocess.Popen(sandbox() + ['--', 'dbus-run-session', '--config-file=/lab/session-bus.conf', '--',
                            'python3', '/control.py', '_server'],
                            stdin=subprocess.DEVNULL, stdout=log, stderr=log,
                            start_new_session=True, close_fds=True)
    save_payload('server', proc.pid, ['python3', '/control.py', '_server'])
    for _ in range(100):
        if proc.poll() is not None:
            raise RuntimeError('Command server failed; inspect scratch/cp00/lab/logs/server.txt')
        if (LAB / 'control.sock').exists():
            print(json.dumps(request({'command': ['/usr/bin/true']})))
            return
        time.sleep(.05)
    raise RuntimeError('Command server readiness timed out; inspect recorded handle')


def start_compositor():
    handle = LAB / 'compositor.json'
    if handle.exists():
        old = json.loads(handle.read_text())
        try:
            i = identity(old['pid'])
            if i['start_ticks'] == old['start_ticks']:
                raise RuntimeError('Recorded compositor is still live; stop it first')
        except (FileNotFoundError, ProcessLookupError):
            pass
    log = LAB.joinpath('logs/compositor.txt').open('a')
    proc = subprocess.Popen(sandbox(True) + ['--', 'Hyprland', '-c', '/lab/hyprland.lua'],
                            stdin=subprocess.DEVNULL, stdout=log, stderr=log,
                            start_new_session=True, close_fds=True)
    save_payload('compositor', proc.pid, ['Hyprland', '-c', '/lab/hyprland.lua'])
    print(json.dumps({'wrapper': proc.pid, 'started': now(), 'log': str(log.name)}))


def serve():
    class Handler(socketserver.StreamRequestHandler):
        def handle(self):
            try:
                message = json.loads(self.rfile.readline(1024 * 1024))
                command = message['command']
                if not isinstance(command, list) or not command or not all(isinstance(s, str) for s in command):
                    raise ValueError('Expected command argument list')
                env = dict(os.environ)
                # Derive nested identity from this private runtime, never the host environment.
                sockets = sorted(Path('/run/cp00').glob('wayland-*'))
                sockets = [p for p in sockets if p.is_socket()]
                instances = list(Path('/run/cp00/hypr').glob('*/.socket.sock'))
                if len(sockets) == 1 and len(instances) == 1:
                    env['WAYLAND_DISPLAY'] = sockets[0].name
                    env['HYPRLAND_INSTANCE_SIGNATURE'] = instances[0].parent.name
                if message.get('background'):
                    log = Path('/lab/logs') / message['log']
                    if log.parent != Path('/lab/logs'):
                        raise ValueError('Invalid log path')
                    with log.open('a') as output:
                        p = subprocess.Popen(command, env=env, stdin=subprocess.DEVNULL,
                                             stdout=output, stderr=output, close_fds=True)
                    response = {'pid': p.pid, 'started': now()}
                else:
                    p = subprocess.run(command, env=env, capture_output=True, text=True,
                                       timeout=message.get('timeout', 60), stdin=subprocess.DEVNULL)
                    response = {'command': command, 'exit_code': p.returncode,
                                'stdout': p.stdout, 'stderr': p.stderr, 'date': now()}
            except Exception as error:
                response = {'error': str(error)}
            self.wfile.write(json.dumps(response).encode() + b'\n')
    with socketserver.ThreadingUnixStreamServer('/lab/control.sock', Handler) as server:
        os.chmod('/lab/control.sock', 0o600)
        server.serve_forever()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['prepare', 'server-start', 'server-stop',
                                         'compositor-start', 'compositor-stop', 'exec', '_server'])
    parser.add_argument('command', nargs=argparse.REMAINDER)
    args = parser.parse_args()
    if args.action == '_server':
        serve()
    elif args.action == 'prepare':
        prepare()
    elif args.action == 'server-start':
        start_server()
    elif args.action == 'compositor-start':
        start_compositor()
    elif args.action.endswith('-stop'):
        print(stop_verified(args.action[:-5]))
    elif args.action == 'exec':
        command = args.command[1:] if args.command[:1] == ['--'] else args.command
        response = request({'command': command})
        print(json.dumps(response, indent=2))
        return response.get('exit_code', 1)
    return 0


if __name__ == '__main__':
    sys.exit(main())
