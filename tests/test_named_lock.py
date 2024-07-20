from pathlib import Path
from unittest import TestCase

from combo_lock import NamedLock


class TestNamedLock(TestCase):
    def test_simple_name(self):
        lock = NamedLock('test_lock')
        with lock:
            pass

    def test_name_with_slash(self):
        lock = NamedLock('test/lock')
        with lock:
            pass

    def test_name_with_emoji(self):
        lock = NamedLock('💖🔒')
        with lock:
            pass

    def test_named_lock_file_access_rights(self):
        lock = NamedLock('access_rights_test_lock')
        lock_path = Path(lock.path)
        access_rights = 0o666
        with lock:
            pass
        assert Path(lock_path).stat().st_mode & access_rights == access_rights
