#!/usr/bin/env python3
"""Read-only /proc CPU/RSS and deduplicated DRM client sampling in the CP00 namespace."""
import json
import os
from pathlib import Path
import re
import sys
import time


def sample(pid):
    proc = Path('/proc', str(pid))
    stat = proc.joinpath('stat').read_text().rsplit(')', 1)[1].split()
    engines = {}
    clients = set()
    raw_gpu = []
    for entry in proc.joinpath('fdinfo').iterdir():
        try:
            text = entry.read_text()
        except FileNotFoundError:
            continue
        client = re.search(r'drm-client-id:\s*(\d+)', text)
        if not client:
            continue
        key = (re.search(r'drm-pdev:\s*(\S+)', text).group(1), client.group(1))
        if key in clients:
            continue
        clients.add(key)
        raw_gpu.append(text)
        for name, value in re.findall(r'drm-engine-([^:\s]+):\s*(\d+)\s+ns', text):
            engines[name] = engines.get(name, 0) + int(value)
    return {'monotonic': time.monotonic(), 'pid': pid, 'start_ticks': stat[19],
            'cpu_ticks': int(stat[11]) + int(stat[12]),
            'reaped_child_ticks': int(stat[13]) + int(stat[14]),
            'rss_kib': int(stat[21]) * os.sysconf('SC_PAGE_SIZE') / 1024,
            'engines_ns': engines, 'raw_drm_fdinfo': raw_gpu}


if __name__ == '__main__':
    pid, seconds = int(sys.argv[1]), float(sys.argv[2])
    if seconds == 0:
        print(json.dumps({'snapshot': sample(pid)}, indent=2))
        sys.exit(0)
    if seconds < 0:
        raise ValueError('Sampling duration must be nonnegative')
    samples = [sample(pid)]
    end = time.monotonic() + seconds
    while time.monotonic() < end:
        time.sleep(min(1, max(0, end - time.monotonic())))
        samples.append(sample(pid))
    first, last = samples[0], samples[-1]
    assert first['start_ticks'] == last['start_ticks']
    elapsed = last['monotonic'] - first['monotonic']
    hz = os.sysconf('SC_CLK_TCK')
    print(json.dumps({'duration_seconds': elapsed, 'clock_ticks_per_second': hz,
                      'cpu_percent_one_core': (last['cpu_ticks'] - first['cpu_ticks']) / hz / elapsed * 100,
                      'reaped_child_cpu_percent': (last['reaped_child_ticks'] - first['reaped_child_ticks']) / hz / elapsed * 100,
                      'rss_kib_min': min(s['rss_kib'] for s in samples),
                      'rss_kib_max': max(s['rss_kib'] for s in samples),
                      'gpu_engine_percent': {k: (v - first['engines_ns'].get(k, v)) / elapsed / 1e9 * 100
                                             for k, v in last['engines_ns'].items()},
                      'samples': samples}, indent=2))
