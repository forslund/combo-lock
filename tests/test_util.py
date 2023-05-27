from unittest import TestCase

from combo_lock.util import get_ram_directory


class TestComboLock(TestCase):
    def test_ram_dir(self):
        ram_dir = get_ram_directory("combo_locks")
        assert(ram_dir is not None)
