"""Read-only CP-00 evidence closure audit; run from repository root."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys

BASE = '570387d'
ROOT = Path.cwd()
AREA = Path('review/cp-00-baseline/evidence/run-05/automated')
SHA = 'b114d5a1b8c3ed90e97b577e3424092a783e04ed'
def git(*args):
    return subprocess.check_output(['git', *args])
def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def refs(value):
    if isinstance(value, dict):
        if 'path' in value and 'sha256' in value:
            yield value
        for v in value.values():
            yield from refs(v)
    elif isinstance(value, list):
        for v in value:
            yield from refs(v)

old = json.loads(git('show', BASE + ':docs/workflow/progress.json'))
new = json.loads(Path('docs/workflow/progress.json').read_text())
a, b = old['checkpoints'][0], new['checkpoints'][0]
assert new['checkpoints'][1:] == old['checkpoints'][1:]
assert b['gate_b'] is None and b['status'] == a['status']
for key in a:
    if key not in {'tests', 'next_agent_action', 'next_owner_action'}:
        assert a[key] == b[key], key
current = {t['id']: t for t in b['tests']}
for t in a['tests']:
    u = current[t['id']]
    assert u['history'][:len(t['history'])] == t['history'], t['id']
    if t['id'] not in {'M01', 'M02', 'M03'}:
        assert t == u, t['id']
required = [t for t in b['tests'] if t.get('required', True)]
assert len(required) == 8 and all(t['result'] == 'PASS' for t in required)
conditional = [t for t in b['tests'] if not t.get('required', True)]
assert {t['id'] for t in conditional} == {'R02-physical-2-display', 'M03-physical-2-display'}
for t in conditional:
    assert t['result'] == 'NOT TESTED' and 'ENVIRONMENT LIMITATION' in t['reason'], t['result']
    for field in ['owner_quote', 'date', 'source', 'spec_reference', 'reason', 'evidence']:
        assert t['disposition'][field]
old_contract = git('show', BASE + ':docs/workflow/checkpoints/cp-00-baseline.md').decode()
old_owner = git('show', BASE + ':owner/checkpoints/cp-00-baseline.md').decode()
assert 'where available' in old_contract and 'If a second test display exists' in old_owner
checked = 0
for obj in [b, json.loads((AREA/'closure-evidence-inventory.json').read_text())]:
    for item in refs(obj):
        assert digest(item['path']) == item['sha256'], item['path']
        assert hashlib.sha256(git('show', ':' + item['path'])).hexdigest() == item['sha256'], item['path']
        checked += 1
old_files = git('ls-tree', '-r', '--name-only', BASE, 'review/cp-00-baseline/evidence').decode().splitlines()
for path in old_files:
    assert Path(path).read_bytes() == git('show', BASE + ':' + path), path
for path in git('diff', '--name-only', BASE).decode().splitlines():
    assert path.startswith(('docs/workflow/', 'owner/', 'review/cp-00-baseline/evidence/')), path
sys.path.insert(0, 'tools')
import cp00
import cp00_runtime as runtime
assert not cp00.payload_live('server') and not cp00.payload_live('compositor')
selected = json.loads((cp00.LAB/'selected-source.json').read_text())
assert selected['revision'] == SHA
sources = {}
for rev in [SHA, 'ff520e33e136bbce11b7100c69888dedf42f7273']:
    source = cp00.LAB/'checkouts'/rev
    assert git('-C', str(source), 'rev-parse', 'HEAD').decode().strip() == rev
    assert not git('-C', str(source), 'status', '--porcelain')
    sources[rev] = 'clean'
state = json.loads((AREA/'m04-return-final-state.json').read_text())
snapshot_counts = {}
for name, snapshot in state['snapshots'].items():
    files = runtime.digest_tree(cp00.BACKUPS/name/'home')
    assert files == snapshot['files'], name
    snapshot_counts[name] = len(files)
assert len(snapshot_counts) == 3
assert len(json.loads((AREA/'performance.json').read_text())) == 24
assert len(json.loads((AREA/'startup.json').read_text())) == 3
displays = json.loads((AREA/'closure-display-verification.json').read_text())
for record in displays['current_host_monitors']:
    assert record['exit_code'] == 0
    assert [m['name'] for m in record['monitors']] == ['eDP-1']
result = {'date': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'result': 'PASS',
          'base_ref': BASE, 'tested_revision': SHA, 'run': 'run-05',
          'required_pass': len(required), 'conditional_not_tested': [t['id'] for t in conditional],
          'checked_hashed_references_in_worktree_and_index': checked,
          'preserved_old_evidence_files': len(old_files),
          'all_old_histories_preserved': True, 'later_checkpoints_unchanged': True,
          'product_and_helper_source_unchanged': sources, 'selected_source': selected,
          'test_payloads_stopped': True, 'immutable_snapshot_file_counts': snapshot_counts,
          'resource_samples': 24, 'startup_samples': 3, 'physical_display_names': ['eDP-1'],
          'gate_b': None}
print(json.dumps(result, indent=2))
