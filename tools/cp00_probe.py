#!/usr/bin/env python3
"""Fail-closed assertions run INSIDE the CP-00 app namespace before k4."""
import json
import os
from pathlib import Path
import subprocess


def command(args):
    r = subprocess.run(args, capture_output=True, text=True, timeout=10)
    return {'command': args, 'exit_code': r.returncode,
            'stdout': r.stdout, 'stderr': r.stderr}


absent = ['/home/noobsambit', '/parent', '/run/user/1000',
          '/run/dbus/system_bus_socket', '/run/udev', '/dev/snd', '/dev/input',
          '/dev/video0', '/dev/dri/card0', '/dev/dri/card1', '/tmp/.X11-unix']
assert os.environ['HOME'] == '/home/cp00'
assert os.environ['XDG_RUNTIME_DIR'] == '/run/cp00'
assert all(not Path(p).exists() for p in absent), 'Host path/device exposed'
assert os.environ['WAYLAND_DISPLAY'].startswith('wayland-')
assert Path('/run/cp00', os.environ['WAYLAND_DISPLAY']).is_socket()
signature = os.environ['HYPRLAND_INSTANCE_SIGNATURE']
assert Path('/run/cp00/hypr', signature, '.socket.sock').is_socket()
# /sys contains read-only device metadata; /proc/net describes this network namespace.
assert [line.split(':')[0].strip() for line in Path('/proc/net/dev').read_text().splitlines()[2:]] == ['lo']
assert os.environ['DBUS_SESSION_BUS_ADDRESS'].startswith('unix:path=/tmp/dbus-')
bus = command(['busctl', '--address=' + os.environ['DBUS_SESSION_BUS_ADDRESS'],
               'call', 'org.freedesktop.DBus', '/org/freedesktop/DBus',
               'org.freedesktop.DBus', 'GetId'])
assert bus['exit_code'] == 0, bus
names = command(['busctl', '--address=' + os.environ['DBUS_SESSION_BUS_ADDRESS'], '--no-pager', 'list'])
assert names['exit_code'] == 0, names
assert '(activatable)' not in names['stdout'], 'Unexpected bus activation directory'
assert 'org.freedesktop.Notifications' not in names['stdout'], 'Unexpected test-bus notification owner'
assert 'org.freedesktop.portal.Desktop' not in names['stdout'], 'Unexpected portal'
for alias in ['/original', '/lab/original']:
    try:
        Path(alias, 'cp00-must-not-write').write_text('probe')
    except OSError:
        pass
    else:
        raise AssertionError('Pinned source is writable: ' + alias)
state = Path('/home/cp00/.local/state/k4')
state.mkdir(parents=True, exist_ok=True)
state.joinpath('cp00-probe.txt').write_text('CP00 DUMMY STATE ONLY\n')
print(json.dumps({'result': 'PASS', 'environment': dict(os.environ),
                  'namespaces': {k: os.readlink('/proc/self/ns/' + k)
                                 for k in ['pid', 'mnt', 'net', 'ipc', 'user']},
                  'absent_paths': absent, 'session_bus': bus, 'names': names,
                  'monitors': command(['hyprctl', '-j', 'monitors']),
                  'interfaces': Path('/proc/net/dev').read_text(),
                  'process_ids': sorted(p.name for p in Path('/proc').glob('[0-9]*')),
                  'state_sentinel': str(state / 'cp00-probe.txt')}, indent=2))
