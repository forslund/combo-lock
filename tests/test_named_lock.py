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
