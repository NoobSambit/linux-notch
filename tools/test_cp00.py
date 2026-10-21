#!/usr/bin/env python3
"""Safety regressions for CP-00 controls. No host service/process is signalled."""
import copy
import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('runtime', Path(__file__).with_name('cp00_runtime.py'))
runtime = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runtime)


class Controls(unittest.TestCase):
    def setUp(self):
        self.instance = {'id': 'full-test-id', 'pid': 10, 'config_path': runtime.CONFIG,
                         'launch_time': '2026-10-21T00:00:00', 'shell_id': 'fixture'}
        self.process = {'pid': 10, 'start_ticks': '100', 'exe': '/usr/bin/quickshell',
                        'argv': ['quickshell', '-p', runtime.CONFIG], 'pid_namespace': 'test'}
        self.env = {'WAYLAND_DISPLAY': 'test', 'HYPRLAND_INSTANCE_SIGNATURE': 'test',
                    'DBUS_SESSION_BUS_ADDRESS': 'test', 'XDG_RUNTIME_DIR': 'test'}
        self.handle = {'instance': self.instance, 'process': self.process,
                       'environment': self.env, 'revision': runtime.REVISION}

    def verify(self, handle=None, found=None, process=None, env=None):
        with patch.object(runtime, 'instances', return_value=found if found is not None else [self.instance]), \
             patch.object(runtime, 'process_identity', return_value=process or self.process), \
             patch.object(runtime, 'environment', return_value=env or self.env), \
             patch.object(runtime.os, 'pidfd_open', side_effect=AssertionError('must not signal')):
            return runtime.verify(handle or self.handle)

    def test_matches_full_identity(self):
        self.assertTrue(self.verify())

    def test_absent_old_id_does_not_select_replacement(self):
        replacement = dict(self.instance, id='other-full-id')
        self.assertFalse(self.verify(found=[replacement], env={'changed': True}))

    def test_substring_id_is_not_a_match(self):
        self.assertFalse(self.verify(found=[dict(self.instance, id='full-test-id-extra')]))

    def test_previous_revision_absent_is_already_stopped(self):
        handle = copy.deepcopy(self.handle)
        handle['instance']['config_path'] = '/previous/shell.qml'
        self.assertFalse(self.verify(handle, found=[]))

    def test_changed_config_refused(self):
        with self.assertRaises(RuntimeError):
            self.verify(found=[dict(self.instance, config_path='/foreign/shell.qml')])

    def test_recorded_foreign_config_refused(self):
        handle = copy.deepcopy(self.handle)
        handle['instance']['config_path'] = '/foreign/shell.qml'
        with self.assertRaises(RuntimeError):
            self.verify(handle)

    def test_pid_reuse_refused(self):
        with self.assertRaises(RuntimeError):
            self.verify(process=dict(self.process, start_ticks='101'))

    def test_changed_bus_refused(self):
        with self.assertRaises(RuntimeError):
            self.verify(env=dict(self.env, DBUS_SESSION_BUS_ADDRESS='foreign'))

    def test_changed_executable_refused(self):
        with self.assertRaises(RuntimeError):
            self.verify(process=dict(self.process, exe='/usr/bin/sleep'))

    def test_no_instance_cli_sentence(self):
        with patch.object(runtime, 'execute', return_value='No running instances.\n'):
            self.assertEqual(runtime.instances(), [])

    def test_malformed_cli_is_not_silently_empty(self):
        with patch.object(runtime, 'execute', return_value='Unexpected error'):
            with self.assertRaises(ValueError):
                runtime.instances()

    def test_snapshot_path_traversal_refused(self):
        for value in ['../personal', '/tmp/test', '', 'UPPER', 'name.json']:
            with self.subTest(value=value), self.assertRaises(ValueError):
                runtime.snapshot(value)

    def test_backup_symlinks_refused(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'outside').symlink_to('/etc/passwd')
            with self.assertRaises(RuntimeError):
                runtime.digest_tree(root)

    def test_corrupt_snapshot_does_not_change_state(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            snap = root / 'baseline'
            (snap / 'home').mkdir(parents=True)
            (snap / 'home/dummy').write_text('corrupt')
            import json
            (snap / 'manifest.json').write_text(json.dumps({'revision': runtime.REVISION,
                                                        'stores': runtime.STORES, 'files': {}}))
            with patch.object(runtime, 'BACKUPS', root), patch.object(runtime, 'stop'), \
                 patch.object(runtime, 'backup', side_effect=AssertionError('must not mutate')):
                with self.assertRaisesRegex(RuntimeError, 'checksum mismatch'):
                    runtime.restore('baseline')


if __name__ == '__main__':
    unittest.main()
