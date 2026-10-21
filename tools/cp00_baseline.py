#!/usr/bin/env python3
"""Reproducible CP-00 characterization and sampling driver. Synthetic lab only."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import re
import time
import cp00

ROOT = Path(__file__).resolve().parent.parent


class Run:
    def __init__(self, name):
        if not name.startswith('run-') or not name[4:].isdigit():
            raise ValueError('Expected run-NN')
        self.name = name
        self.out = ROOT / 'review/cp-00-baseline/evidence' / name
        (self.out / 'application').mkdir(parents=True, exist_ok=True)
        (self.out / 'automated').mkdir(exist_ok=True)
        log = self.out / 'automated/commands.json'
        self.events = json.loads(log.read_text()) if log.exists() else []

    def command(self, argv, required=True, **kwargs):
        result = cp00.request({'command': argv, **kwargs})
        self.events.append(result)
        (self.out / 'automated/commands.json').write_text(json.dumps(self.events, indent=2) + '\n')
        if required and result.get('exit_code', 0 if 'pid' in result else 1) != 0:
            raise RuntimeError(json.dumps(result))
        return result

    def runtime(self, *args, required=True):
        return self.command(['python3', '/lab/runtime_control.py', *args], required)

    def ipc(self, target, action, *args):
        return self.runtime('ipc', 'call', target, action, *args)

    def capture(self, state, output=None, proof='R02'):
        time.sleep(.8)
        file = f'cp-00__{proof}__{state}__{self.name}.png'
        args = ['grim', '-o', output or 'CP00-STABLE', '/lab/capture.png']
        self.command(args)
        shutil.copyfile(cp00.LAB / 'capture.png', self.out / 'application' / file)
        self.command(['hyprctl', '-j', 'monitors'])
        self.command(['hyprctl', '-j', 'layers'])
        print('captured ' + state, flush=True)

    def wait_dual(self, mode):
        deadline = time.monotonic() + 20
        while time.monotonic() < deadline:
            state = json.loads(self.ipc('k4.dual', 'estado')['stdout'])
            if state['modo'] == mode and not state['viajando']:
                return state
            time.sleep(.2)
        raise RuntimeError('Dual did not settle in ' + mode)

    def stopped_settings(self, edge, reserve='reserva'):
        self.runtime('stop')
        path = cp00.LAB / 'home/.local/state/k4/ajustes.json'
        data = json.loads(path.read_text()) if path.exists() else {}
        data.update(posicionBarra=edge, reservaIsla=reserve)
        path.write_text(json.dumps(data, indent=1) + '\n')
        self.runtime('start')
        time.sleep(.8)


FIXTURE = '''import QtQuick
import Quickshell
import Quickshell.Io
ShellRoot {
    Window {
        id: w
        title: "CP00 dummy document"
        visible: true; width: 640; height: 400; color: "#18333a"
        Text { x: 30; y: 30; color: "white"; font.pixelSize: 24; text: "CP-00 · dummy document" }
        TextInput { id: entry; x: 30; y: 100; width: 500; height: 40; color: "white"; text: "Harmless input"; focus: true }
        Rectangle {
            y: 200; width: 40; height: 40; color: "#67dac6"
            SequentialAnimation on x {
                loops: Animation.Infinite
                NumberAnimation { from: 30; to: 400; duration: 1800 }
                NumberAnimation { from: 400; to: 30; duration: 1800 }
            }
        }
    }
    Window {
        title: "CP00 static note"; visible: true; width: 350; height: 250; color: "#44334a"
        Text { x: 25; y: 35; text: "CP-00 · static note"; color: "white"; font.pixelSize: 22 }
    }
    IpcHandler {
        target: "cp00.fixture"
        function fullscreen(on: bool): void { w.visibility = on ? Window.FullScreen : Window.Windowed }
        function input(): string { return entry.text }
    }
}
'''


def fixture(run):
    cp00.LAB.joinpath('fixture.qml').write_text(FIXTURE)
    return run.command(['quickshell', '-p', '/lab/fixture.qml', '--no-color'],
                       background=True, log='fixture.txt')


def direct_ipc(run, config, target, method, *args):
    listed = run.command(['quickshell', 'list', '--all', '--json'])
    found = [i for i in json.loads(listed['stdout']) if i['config_path'] == config]
    assert len(found) == 1, found
    return run.command(['quickshell', 'ipc', '--id', found[0]['id'], 'call', target, method, *args])


def stop_fixture(run, config):
    code = '''import sys,json,os; sys.path.insert(0,"/lab"); import runtime_control as r
config=sys.argv[1]; found=[i for i in r.instances() if i["config_path"]==config]
assert len(found)==1,found
i=found[0]; before=r.process_identity(i["pid"]); fd=os.pidfd_open(i["pid"])
assert r.process_identity(i["pid"])==before
r.execute(["quickshell","kill","--id",i["id"]]); os.close(fd)
print(json.dumps({"stopped":i,"process":before}))
'''
    return run.command(['python3', '-c', code, config])


def characterize(run):
    run.runtime('stop')
    dual = cp00.LAB / 'home/.local/state/k4/plugins/dual/estado.json'
    dual.parent.mkdir(exist_ok=True, parents=True)
    dual.write_text('{"efecto":"viaje","ambas":false}\n')
    for edge in ['arriba', 'abajo', 'izquierda', 'derecha']:
        run.stopped_settings(edge)
        run.capture('surface-' + edge)
        run.ipc('k4', 'toggleLauncher')
        run.capture('launcher-' + edge)
        run.ipc('k4.launcher', 'toggle')
        if edge in ['arriba', 'abajo']:
            run.ipc('k4.dual', 'bajar')
            run.wait_dual('dock')
            run.ipc('k4.dual', 'estado')
            run.capture('dual-from-' + edge)
            run.ipc('k4.dual', 'subir')
            run.wait_dual('barra')
    run.stopped_settings('arriba')
    run.ipc('k4.settings', 'abrirPagina', 'captura')
    run.capture('settings-capture')
    run.ipc('k4.settings', 'close')
    # Send only a known harmless text selection to the nested display.
    run.command(['python3', '-c', 'import subprocess; subprocess.run(["wl-copy"], input="CP00 baseline harmless clipboard text", text=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)'])
    time.sleep(.4)
    run.ipc('k4.clipboard', 'open')
    run.capture('clipboard-text')
    run.ipc('k4.clipboard', 'close')
    run.command(['python3', '/original/tools/captura.py', 'foto', '--ambito', 'pantalla', '--destino', 'fichero'])
    run.capture('capture-return')
    run.command(['magick', '-size', '80x60', 'xc:#41a6a1', '/lab/clipboard-image.png'])
    run.command(['sh', '-c', 'exec wl-copy --foreground --type image/png < /lab/clipboard-image.png'],
                background=True, log='image-selection.txt')
    time.sleep(.4)
    run.ipc('k4.clipboard', 'open')
    run.capture('clipboard-image')
    run.ipc('k4.clipboard', 'close')
    characterize_tail(run)


def characterize_tail(run):
    fixture(run)
    time.sleep(.8)
    direct_ipc(run, '/lab/fixture.qml', 'cp00.fixture', 'fullscreen', 'true')
    run.capture('fullscreen-on')
    run.command(['hyprctl', '-j', 'clients'])
    direct_ipc(run, '/lab/fixture.qml', 'cp00.fixture', 'fullscreen', 'false')
    run.capture('fullscreen-return')
    run.command(['hyprctl', 'output', 'create', 'headless', 'CP00-2'])
    run.capture('two-displays-first', 'CP00-STABLE')
    run.capture('two-displays-second', 'CP00-2')
    run.command(['hyprctl', 'output', 'remove', 'CP00-2'])
    run.capture('display-removal-return')
    stop_fixture(run, '/lab/fixture.qml')
    # Real local media playback, with an intentionally isolated dummy audio sink.
    run.command(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-f', 'lavfi', '-i',
                 'sine=frequency=440:duration=120', '-metadata', 'title=CP00 local sine track',
                 '-y', '/lab/dummy.wav'])
    run.command(['vlc', '--intf', 'dummy', '--extraintf', 'dbus', '--aout', 'adummy',
                 '--no-video', '--no-one-instance', '--loop', '/lab/dummy.wav'],
                background=True, log='vlc.txt')
    time.sleep(1)
    run.command(['playerctl', '-p', 'vlc', 'metadata'])
    run.capture('media-playing')
    run.ipc('k4', 'setMode', 'player')
    run.capture('media-expanded')
    run.ipc('k4', 'setMode', '')
    run.ipc('k4', 'togglePlay')
    run.command(['playerctl', '-p', 'vlc', 'status'])
    run.capture('media-paused')
    run.ipc('k4', 'togglePlay')
    run.command(['playerctl', '-p', 'vlc', 'status'])
    run.command(['playerctl', '-p', 'vlc', 'stop'])
    # Inherited standalone plugin bank, no edits to pinned runtime files.
    bank = cp00.LAB / 'plugin-bank'
    if not bank.exists():
        shutil.copytree(cp00.LAB / 'original', bank)
    user_plugins = cp00.LAB / 'home/.config/k4/plugins'
    user_plugins.mkdir(parents=True, exist_ok=True)
    for name in ['hola', 'piezas', 'efectos', 'snake']:
        target = user_plugins / name
        if not target.exists():
            shutil.copytree(cp00.LAB / 'original/ejemplos' / name, target)
        code = 'import sys; sys.path.insert(0,"/lab/plugin-bank/tools"); import plugins; plugins.enlazar_externos(); sys.exit(plugins.probar(sys.argv[1]))'
        run.command(['python3', '-c', code, name], background=True, log='example-' + name + '.txt')
        time.sleep(.8)
        listed = run.command(['quickshell', 'list', '--all', '--json'])
        bank_instance = next(i for i in json.loads(listed['stdout']) if i['config_path'] == '/lab/plugin-bank/.banco.qml')
        run.command(['quickshell', 'ipc', '--id', bank_instance['id'], 'show'])
        if name == 'snake':
            direct_ipc(run, bank_instance['config_path'], 'k4.snake', 'empezar')
            direct_ipc(run, bank_instance['config_path'], 'k4.snake', 'girar', '0', '1')
            direct_ipc(run, bank_instance['config_path'], 'k4.snake', 'estado')
        if name == 'piezas':
            direct_ipc(run, bank_instance['config_path'], 'k4.piezas', 'estado')
        run.capture('example-' + name)
        stop_fixture(run, bank_instance['config_path'])
        time.sleep(.3)
    run.ipc('k4', 'pluginStatus')
    run.ipc('k4', 'toggleLauncher')
    run.command(['wtype', 'CP00-no-matching-app'])
    run.capture('launcher-keyboard-search')
    run.command(['wtype', '-k', 'Escape'])
    run.capture('launcher-escape-return')
    print('Commands finished; inspect captures and observations before recording outcomes.', flush=True)



def measure(run):
    cp00.LAB.joinpath('sample.py').write_bytes(Path(__file__).with_name('cp00_sample.py').read_bytes())
    run.runtime('stop')
    saved = cp00.LAB / 'home/.local/state/k4/plugins.json'
    data = json.loads(saved.read_text()) if saved.exists() else {'habilitados': {}}
    data.setdefault('habilitados', {}).pop('atalaya', None)
    saved.write_text(json.dumps(data, indent=1) + '\n')
    dual = cp00.LAB / 'home/.local/state/k4/plugins/dual/estado.json'
    dual.parent.mkdir(exist_ok=True, parents=True)
    dual.write_text('{"efecto":"viaje","ambas":false}\n')
    # Startup to IPC readiness is measured separately from a 3-second warmup.
    startup = []
    for repetition in range(3):
        began = time.monotonic()
        result = run.command(['env', 'WAYLAND_DEBUG=client',
                              'python3', '/lab/runtime_control.py', 'start'])
        ready = time.monotonic() - began
        handle = json.loads(result['stdout'])
        time.sleep(3)
        initial = run.command(['python3', '/lab/sample.py', str(handle['instance']['pid']), '0'])
        startup.append({'repetition': repetition + 1, 'ipc_ready_seconds': ready,
                        'handle': handle, 'after_warmup': json.loads(initial['stdout'])})
        if repetition < 2:
            run.runtime('stop')
    (run.out / 'automated/startup.json').write_text(json.dumps(startup, indent=2) + '\n')
    print('startup repetitions complete', flush=True)
    handle = json.loads(run.runtime('status')['stdout'])
    pid = handle['instance']['pid']
    log = cp00.LAB / Path(handle['log']).relative_to('/lab')
    observations = []
    outcomes = []

    def condition(name):
        time.sleep(3)
        for repetition in range(3):
            offset = log.stat().st_size
            result = run.command(['python3', '/lab/sample.py', str(pid), '10'])
            trace = log.read_bytes()[offset:].decode(errors='replace')
            filename = f'{name}-{repetition + 1}-frames.txt'
            archive = cp00.LAB / 'raw-traces' / run.name
            archive.mkdir(parents=True, exist_ok=True, mode=0o700)
            raw_file = archive / filename
            raw_file.write_text(trace)
            (run.out / 'automated' / filename).write_text(frame_trace(trace))
            pending = {}
            delivered = {}
            last = {}
            intervals = []
            for line in trace.splitlines():
                request = re.search(r'wl_surface#(\d+)\.frame\(new id wl_callback#(\d+)\)', line)
                done = re.search(r'wl_callback#(\d+)\.done\((\d+)\)', line)
                if request:
                    pending[request.group(2)] = request.group(1)
                if done and done.group(1) in pending:
                    surface = pending.pop(done.group(1))
                    tick = int(done.group(2))
                    if surface in last and tick >= last[surface]:
                        intervals.append(tick - last[surface])
                    last[surface] = tick
                    delivered[surface] = delivered.get(surface, 0) + 1
            intervals.sort()
            values = intervals
            summary = json.loads(result['stdout'])
            summary.update(condition=name, repetition=repetition + 1,
                           frame_trace=filename, frames_logged=sum(delivered.values()),
                           raw_trace_path=str(raw_file), raw_trace_sha256=hashlib.sha256(raw_file.read_bytes()).hexdigest(),
                           frame_callbacks_by_surface=delivered,
                           callback_interval_ms_max=max(values) if values else None,
                           callback_interval_ms_p95=values[min(len(values)-1, int(len(values)*.95))] if values else None)
            outcomes.append(summary)
            (run.out / 'automated/performance.json').write_text(json.dumps(outcomes, indent=2) + '\n')
            print(name, repetition + 1, 'CPU', round(summary['cpu_percent_one_core'], 2),
                  'GPU', summary['gpu_engine_percent'], 'frames', len(values), flush=True)

    status = json.loads(run.ipc('k4', 'pluginStatus')['stdout'])
    effective = next(i for i in status if i['id'] == 'atalaya')
    assert effective['enabled']
    observations.append({'saved_override': None, 'catalog_default': True, 'effective': effective})
    condition('idle-catalog-atalaya-on')
    run.ipc('k4', 'pluginDisable', 'atalaya')
    time.sleep(.5)
    status = json.loads(run.ipc('k4', 'pluginStatus')['stdout'])
    effective = next(i for i in status if i['id'] == 'atalaya')
    assert not effective['enabled']
    observations.append({'saved_override': False, 'effective': effective})
    condition('idle-atalaya-off')
    run.ipc('k4', 'pluginEnable', 'atalaya')
    time.sleep(.5)
    status = json.loads(run.ipc('k4', 'pluginStatus')['stdout'])
    effective = next(i for i in status if i['id'] == 'atalaya')
    assert effective['enabled']
    observations.append({'saved_override': True, 'effective': effective})
    condition('idle-explicit-atalaya-on')
    run.command(['playerctl', '-p', 'vlc', 'play'])
    condition('media-local-playing')
    run.command(['playerctl', '-p', 'vlc', 'pause'])
    run.ipc('k4.dual', 'bajar')
    run.wait_dual('dock')
    condition('dock-settled')
    run.capture('dock-performance', proof='R03')
    run.ipc('k4.dual', 'subir')
    run.wait_dual('barra')
    fixture(run)
    time.sleep(1)
    direct_ipc(run, '/lab/fixture.qml', 'cp00.fixture', 'input')
    run.ipc('k4.atalaya', 'abrir')
    time.sleep(1)
    observations.append({'open_state': json.loads(run.ipc('k4.atalaya', 'estado')['stdout'])})
    run.capture('atalaya-open', proof='R03')
    condition('atalaya-open-two-dummy-windows')
    run.ipc('k4.atalaya', 'cerrar')
    time.sleep(2)
    observations.append({'closed_state': json.loads(run.ipc('k4.atalaya', 'estado')['stdout'])})
    condition('atalaya-closed-after-open')
    run.capture('atalaya-closed', proof='R03')
    stop_fixture(run, '/lab/fixture.qml')
    (run.out / 'automated/atalaya-states.json').write_text(json.dumps(observations, indent=2) + '\n')
    (run.out / 'automated/profiled-app-log.txt').write_text(frame_trace(log.read_text()))
    # A default, untraced launch calibrates protocol-log overhead without changing render loops.
    run.runtime('stop')
    run.command(['playerctl', '-p', 'vlc', 'stop'])
    handle = json.loads(run.runtime('start')['stdout'])
    pid = handle['instance']['pid']
    log = cp00.LAB / Path(handle['log']).relative_to('/lab')
    condition('idle-untraced-control')
    print('Resource matrix finished; review raw counters and frame traces before acceptance.', flush=True)


def frame_trace(text):
    """Keep frame callbacks and diagnostics durable; raw protocol chatter stays in the lab."""
    selected = [line for line in text.splitlines() if
                ('wl_surface#' in line and any(s in line for s in ['.frame(', '.destroy(']))
                or ('wl_callback#' in line and '.done(' in line)
                or any(s in line for s in ['ERROR', 'WARN', 'error:', 'wl_output#'])]
    return ('# Filtered Wayland frame request/callback, output and diagnostic trace.\n'
            + '\n'.join(selected)).rstrip() + '\n'

def inventory(run):
    rows = []
    for p in sorted((ROOT / 'plugins').rglob('*')) + sorted((ROOT / 'screenshots').rglob('*')):
        if p.is_file() and p.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif', '.wav', '.mp3', '.json', '.ttf', '.otf', '.qsb', '.frag']:
            rows.append({'path': str(p.relative_to(ROOT)), 'bytes': p.stat().st_size,
                         'sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
                         'rights': 'Not cleared by this inventory; consult docs/ASSET_LICENSE_AUDIT.md'})
    (run.out / 'automated/asset-inventory.json').write_text(json.dumps(rows, indent=2) + '\n')
    print('Inventoried', len(rows), 'asset/data/shader paths; no rights clearance asserted.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['characterize', 'characterize-tail', 'measure', 'inventory'])
    parser.add_argument('run')
    args = parser.parse_args()
    target = Run(args.run)
    {'characterize': characterize, 'characterize-tail': characterize_tail, 'measure': measure, 'inventory': inventory}[args.action](target)
