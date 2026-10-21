#!/usr/bin/env python3
"""Workflow-only tests. All records, approvals and media below are synthetic temporary fixtures."""
import copy
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import workflow


class WorkflowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix='notchbar-workflow-test-')
        cls.root = Path(cls.temp.name)
        cls.source = workflow.ROOT
        for directory in ['docs', 'owner', 'review']:
            shutil.copytree(cls.source / directory, cls.root / directory)
        for name in ['AGENTS.md', 'README.md', '.gitignore']:
            shutil.copy2(cls.source / name, cls.root / name)
        (cls.root / 'tools').mkdir()
        shutil.copy2(cls.source / 'tools/workflow.py', cls.root / 'tools/workflow.py')
        cls.base = json.loads(workflow.RECORD.read_text())
        # Contracts/IDs come from the project; execution state must be synthetic.
        # Real checkpoint SHAs do not exist in this temporary repository, and a
        # live current_task must never leak into a synthetic completed handoff.
        cls.base.update(workflow_status='AWAITING WORKFLOW APPROVAL', active_checkpoint=None,
                        next_checkpoint=cls.base['checkpoints'][0]['id'])
        for checkpoint in cls.base['checkpoints']:
            checkpoint.update(status='PLANNED', authorization=None, gate_a=None, gate_b=None,
                              reference_sets=[], runs=[], latest_run=None, branch=None,
                              last_good_sha=None, current_task=None, blocked_reason=None)
            for field in ['approval_history', 'submission', 'proposed_design_spec']:
                checkpoint.pop(field, None)
            for task in checkpoint['tasks']:
                task.update(status='PENDING', evidence=[])
            for test in checkpoint['tests']:
                test.update(result='NOT TESTED', reason='Synthetic fixture has not run.', history=[])
                test.pop('disposition', None)
                test.pop('required', None)
        (cls.root / 'docs/workflow/progress.json').write_text(json.dumps(cls.base, indent=2) + '\n')
        (cls.root / 'owner/PROGRESS.md').write_text(workflow.overview(cls.base))
        cls.git('init', '-q')
        cls.git('config', 'user.name', 'Workflow fixture')
        cls.git('config', 'user.email', 'fixture@invalid')
        # Relative links into runtime code are checked against the real checkout;
        # create inert link targets in the fixture, never launch any product code.
        for name in subprocess.check_output(['git', 'ls-files'], cwd=cls.source).decode().splitlines():
            p = cls.root / name
            if not p.exists():
                p.parent.mkdir(parents=True, exist_ok=True)
                p.touch()
        cls.git('add', '.')
        cls.git('commit', '-qm', 'synthetic fixture')
        cls.sha = cls.git('rev-parse', 'HEAD').strip()
        cls.date = '2026-10-20T00:00:00Z'
        cls.note = cls.make_artifact('review/cp-00-baseline/evidence/run-01/automated/proof.md')

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    @classmethod
    def git(cls, *args):
        return subprocess.check_output(['git', *args], cwd=cls.root, stderr=subprocess.PIPE).decode()

    @classmethod
    def make_artifact(cls, path, content=b'SYNTHETIC TEST FIXTURE; no product evidence.\n'):
        p = cls.root / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(content)
        cls.git('add', '-f', path)
        return {'path': path, 'sha256': hashlib.sha256(content).hexdigest()}

    def setUp(self):
        self.data = copy.deepcopy(self.base)
        self.patcher = patch.object(workflow, 'ROOT', self.root)
        self.patcher.start()
        self.addCleanup(self.patcher.stop)

    def errors(self, data=None, previous=None):
        return workflow.validate(data or self.data, previous)

    def good(self):
        self.assertEqual([], self.errors())

    def bad(self, fragment):
        errors = self.errors()
        self.assertTrue(any(fragment in e for e in errors), errors)

    def authorize(self, i):
        c = self.data['checkpoints'][i]
        c.update(status='IMPLEMENTING', authorization={
            'owner_quote': 'SYNTHETIC authorization', 'date': self.date,
            'source': 'synthetic fixture', 'scope': c['id']
        }, branch='checkpoint/' + c['id'], last_good_sha=self.sha)
        self.data.update(workflow_status='IN PROGRESS', active_checkpoint=c['id'], next_checkpoint=c['id'])
        return c

    def references(self, c):
        folder = f'review/{c["id"]}/references/approved/r01/'
        files = []
        for slot in c['reference_requirements']:
            a = self.make_artifact(folder + slot['file'], b'\x89PNG\r\n\x1a\nfixture header only')
            files.append(dict(a, requirement=slot['file'], source_path='synthetic'))
        spec = self.make_artifact(folder + 'design-spec.md')
        c['reference_sets'] = [{'id': 'r01', 'files': files, 'inspection': 'SYNTHETIC; not decoded', 'design_spec': spec}]
        c['gate_a'] = {'owner_quote': 'SYNTHETIC Gate A', 'date': self.date, 'source': 'fixture',
                       'set_id': 'r01', 'design_spec_sha256': spec['sha256']}

    def handoff(self, i, approve=False):
        c = self.authorize(i)
        if c['visual']:
            self.references(c)
        note = self.make_artifact(f'review/{c["id"]}/evidence/run-01/automated/handoff.md')
        c['runs'] = [{'id': 'run-01', 'revision': self.sha, 'date': self.date, 'environment': 'synthetic',
                      'handoff': note, 'review': note, 'recovery': note}]
        if c['visual']:
            c['runs'][0].update(comparison=note, reference_set='r01')
        c['latest_run'] = 'run-01'
        for t in c['tasks']:
            t.update(status='DONE', evidence=[note])
        for t in c['tests']:
            if t['kind'] == 'owner' and not approve:
                continue
            t.update(result='PASS', reason='', history=[{
                'result': 'PASS', 'run': 'run-01', 'revision': self.sha, 'date': self.date,
                'environment': 'synthetic', 'evidence': [note], 'command': 'true',
                'exit_code': 0, 'steps': 'synthetic test', 'observed': 'synthetic result'
            }])
        c['status'] = 'APPROVED' if approve else 'AWAITING OWNER TEST'
        if approve:
            c['gate_b'] = {'owner_quote': 'SYNTHETIC approval', 'source': 'fixture',
                           'date': self.date, 'run': 'run-01', 'revision': self.sha}
            nxt = self.data['checkpoints'][i + 1]['id'] if i < 10 else None
            self.data.update(active_checkpoint=None, next_checkpoint=nxt)
            if i == 10:
                self.data['workflow_status'] = 'CHECKPOINTS APPROVED'
        return c

    def test_initial_record(self):
        self.good()

    def test_valid_handoff_and_full_sequence(self):
        self.handoff(0)
        self.good()
        for i in range(11):
            self.handoff(i, approve=True)
            self.good()

    def test_schema_and_workflow_status(self):
        for field, value, fragment in [('schema_version', 999, 'schema_version'),
                                       ('workflow_status', 'APPROVED', 'workflow_status')]:
            with self.subTest(field=field):
                self.data = copy.deepcopy(self.base)
                self.data[field] = value
                self.bad(fragment)

    def test_wrong_active_and_next(self):
        self.data.update(active_checkpoint='cp-10-release', next_checkpoint='cp-10-release')
        self.bad('Active checkpoint')
        self.bad('Next checkpoint')

    def test_nonvisual_visual_state(self):
        self.authorize(0)['status'] = 'AWAITING REFERENCES'
        self.bad('nonvisual')

    def test_work_without_authorization(self):
        self.data['checkpoints'][0]['tasks'][0].update(status='DONE', evidence=[self.note])
        self.bad('before authorization')

    def test_planned_cannot_claim_results(self):
        c = self.handoff(0)
        c.update(status='PLANNED', authorization=None)
        for t in c['tasks']:
            t.update(status='PENDING', evidence=[])
        self.data.update(workflow_status='AWAITING WORKFLOW APPROVAL', active_checkpoint=None)
        self.bad('before activation')
        self.bad('PLANNED results')

    def test_deleted_tasks_and_tests(self):
        c = self.data['checkpoints'][0]
        c['tasks'] = []
        c['tests'] = []
        self.bad('task IDs differ')
        self.bad('test IDs differ')

    def test_current_task_and_premature_testing(self):
        c = self.authorize(0)
        c['tasks'][0]['status'] = 'IN PROGRESS'
        self.bad('current_task')
        c['current_task'] = 'T01'
        self.good()
        c['status'] = 'TESTING'
        self.bad('testing before tasks')

    def test_missing_changed_and_untracked_evidence(self):
        c = self.handoff(0)
        c['tasks'][0]['evidence'] = [{'path': 'review/missing.txt', 'sha256': 'a'*64}]
        self.bad('evidence missing')
        c['tasks'][0]['evidence'] = [dict(self.note, sha256='a'*64)]
        self.bad('hash mismatch')
        artifact = self.make_artifact('review/untracked-fixture.txt')
        self.git('rm', '--cached', 'review/untracked-fixture.txt')
        c['tasks'][0]['evidence'] = [artifact]
        self.bad('must be tracked')
        (self.root / artifact['path']).unlink()

    def test_absolute_escape_and_symlink_evidence(self):
        c = self.handoff(0)
        for path in ['/etc/passwd', '../outside', 'review/../../outside']:
            c['tasks'][0]['evidence'] = [{'path': path, 'sha256': 'a'*64}]
            self.bad('repository-relative')
        link = self.root / 'review/escape'
        link.symlink_to('/etc/passwd')
        self.addCleanup(link.unlink)
        c['tasks'][0]['evidence'] = [{'path': 'review/escape', 'sha256': 'a'*64}]
        self.bad('escapes repository')

    def test_stale_result_and_run_identity(self):
        c = self.handoff(0)
        h = c['tests'][0]['history'][0]
        h['run'] = 'run-99'
        self.bad('history run missing')
        self.bad('stale result')
        h['run'] = 'run-01'
        h['revision'] = 'a'*40
        self.bad('identity mismatch')
        h['revision'] = self.sha
        h['environment'] = 'other machine'
        self.bad('identity mismatch')

    def test_failed_command_cannot_pass(self):
        c = self.handoff(0)
        c['tests'][0]['history'][0]['exit_code'] = 1
        self.bad('nonzero exit code')

    def test_staged_evidence_must_match(self):
        c = self.handoff(0)
        a = self.make_artifact('review/cp-00-baseline/evidence/run-01/automated/staged.txt')
        p = self.root / a['path']
        try:
            p.write_text('Changed after staging')
            a['sha256'] = hashlib.sha256(p.read_bytes()).hexdigest()
            c['tasks'][0]['evidence'] = [a]
            self.bad('staged evidence differs')
        finally:
            self.git('rm', '-f', a['path'])

    def test_product_change_invalidates_handoff(self):
        self.handoff(0)
        p = self.root / 'shell.qml'
        original = p.read_bytes()
        try:
            p.write_text('synthetic product change')
            self.bad('product differs from tested revision')
        finally:
            p.write_bytes(original)

    def test_missing_reference_requirements(self):
        self.data['checkpoints'][3]['reference_requirements'] = []
        self.bad('mandatory brief slots')

    def test_incomplete_run_and_dirty_handoff(self):
        c = self.handoff(0)
        c['runs'][0]['patch'] = self.note
        self.bad('clean committed revision')
        c['runs'][0].pop('patch')
        c['runs'][0].pop('recovery')
        self.bad('recovery')

    def test_duplicate_and_old_latest_run(self):
        c = self.handoff(0)
        c['runs'].append(copy.deepcopy(c['runs'][0]))
        self.bad('duplicate runs')
        c['runs'][1]['id'] = 'run-02'
        self.bad('newest run')

    def test_gate_b_mismatch_and_stale_approval(self):
        c = self.handoff(0, approve=True)
        c['gate_b']['revision'] = 'a'*40
        self.bad('approved revision differs')
        c['status'] = 'IMPLEMENTING'
        self.bad('stale Gate B')

    def test_blocked_predecessor(self):
        c = self.handoff(0, approve=True)
        c['blocked_reason'] = 'unresolved failure'
        self.authorize(1)
        self.bad('blocked dependency')

    def test_visual_gate_and_design_spec(self):
        for i in range(3):
            self.handoff(i, approve=True)
        c = self.authorize(3)
        self.bad('without Gate A')
        self.references(c)
        self.good()
        c['gate_a']['design_spec_sha256'] = 'a'*64
        self.bad('translation mismatch')
        c['gate_a'] = None
        c['status'] = 'AWAITING REFERENCES'
        c['reference_sets'][0]['files'][0]['sha256'] = 'a'*64
        self.bad('hash mismatch')

    def test_submission_cannot_skip_inventory(self):
        for i in range(3):
            self.handoff(i, approve=True)
        c = self.authorize(3)
        c['status'] = 'REFERENCES SUBMITTED'
        self.bad('submission inventory')
        self.references(c)
        c['submission'] = copy.deepcopy(c['reference_sets'][0]['files'])
        c['proposed_design_spec'] = c['reference_sets'][0]['design_spec']
        c['gate_a'] = None
        c['status'] = 'AWAITING VISUAL APPROVAL'
        self.good()

    def test_conditional_not_tested_and_failure(self):
        c = self.handoff(0, approve=True)
        t = c['tests'][0]
        t.update(result='NOT TESTED', reason='synthetic limitation', required=False)
        self.bad('required test not passed')
        t['disposition'] = {'owner_quote': 'SYNTHETIC decision', 'date': self.date,
                            'source': 'fixture', 'spec_reference': 'docs/DECISIONS.md',
                            'reason': 'synthetic scope decision', 'evidence': self.note}
        self.good()
        t['result'] = 'FAIL'
        self.bad('required test not passed')

    def test_history_cannot_be_erased_or_rewritten(self):
        c = self.handoff(0, approve=True)
        old = copy.deepcopy(self.data)
        c['tests'][0]['history'] = []
        self.assertTrue(any('append-only' in e for e in self.errors(previous=old)))
        self.data = copy.deepcopy(old)
        self.data['checkpoints'][0]['runs'][0]['environment'] = 'rewritten'
        self.assertTrue(any('append-only' in e for e in self.errors(previous=old)))

    def test_correction_archives_approval_and_suspends_downstream(self):
        self.handoff(0, approve=True)
        self.handoff(1, approve=True)
        old = copy.deepcopy(self.data)
        for i, c in enumerate(self.data['checkpoints'][:2]):
            c['approval_history'] = [{'gate': 'gate_b', 'decision': c['gate_b'],
                                      'reason': 'synthetic regression', 'date': self.date}]
            c['gate_b'] = None
            c['status'] = 'IMPLEMENTING' if i == 0 else 'PLANNED'
            c['blocked_reason'] = 'Revalidation after predecessor correction'
            for t in c['tests']:
                t.update(result='NOT TESTED', reason='Invalidated after regression')
        self.data.update(active_checkpoint='cp-00-baseline', next_checkpoint='cp-00-baseline')
        self.assertEqual([], self.errors(previous=old))
        self.data['checkpoints'][0]['approval_history'] = []
        self.assertTrue(any('must be archived' in e for e in self.errors(previous=old)))

    def test_visual_reapproval_retains_old_work_and_closes_gate(self):
        for i in range(4):
            c = self.handoff(i, approve=True)
        old = copy.deepcopy(self.data)
        c['approval_history'] = [{'gate': gate, 'decision': c[gate], 'date': self.date,
                                  'reason': 'synthetic material revision'} for gate in ['gate_a', 'gate_b']]
        c.update(gate_a=None, gate_b=None, status='AWAITING REFERENCES',
                 blocked_reason='Waiting for replacement visual decision')
        for t in c['tests']:
            t.update(result='NOT TESTED', reason='Visual revision invalidates result')
        self.data.update(active_checkpoint=c['id'], next_checkpoint=c['id'])
        self.assertEqual([], self.errors(previous=old))
        c['status'] = 'IMPLEMENTING'
        self.bad('without Gate A')

    def test_base_reader_and_rejected_missing_base(self):
        with patch.object(workflow, 'RECORD', self.root / 'docs/workflow/progress.json'):
            self.assertEqual(self.base, workflow.read_base(self.sha))
            with self.assertRaises(subprocess.CalledProcessError):
                workflow.read_base('nonexistent-ref')

    def test_reference_set_history_cannot_be_replaced(self):
        for i in range(4):
            c = self.handoff(i, approve=True)
        old = copy.deepcopy(self.data)
        c['reference_sets'][0]['inspection'] = 'rewritten'
        self.assertTrue(any('reference_sets: append-only' in e for e in self.errors(previous=old)))

    def test_retained_run_proof_is_checked_during_correction(self):
        c = self.handoff(0)
        c['status'] = 'IMPLEMENTING'
        c['runs'][0]['recovery'] = {'path': 'review/cp-00-baseline/evidence/run-01/missing.md',
                                   'sha256': 'a'*64}
        self.bad('evidence missing')

    def test_malformed_record_and_invalid_render_do_not_write(self):
        for value in [None, {}, {'checkpoints': []}, {'schema_version': 1}]:
            self.assertTrue(workflow.validate(value))
        record = self.root / 'docs/workflow/progress.json'
        view = self.root / 'owner/PROGRESS.md'
        before = view.read_bytes()
        original = record.read_bytes()
        try:
            record.write_text('{"schema_version": 999}')
            result = subprocess.run(['python3', 'tools/workflow.py', '--render'],
                                    cwd=self.root, capture_output=True, text=True)
            self.assertEqual(1, result.returncode)
            self.assertNotIn('Traceback', result.stderr)
            self.assertEqual(before, view.read_bytes())
        finally:
            record.write_bytes(original)


if __name__ == '__main__':
    unittest.main()
