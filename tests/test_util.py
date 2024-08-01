from pathlib import Path
from unittest import TestCase

from combo_lock.util import get_ram_directory


class TestComboLock(TestCase):
    def test_ram_dir(self):
        ram_dir = get_ram_directory("test_combo_locks")
        assert ram_dir is not None
        access_rights = 0o777
        assert Path(ram_dir).stat().st_mode & access_rights == access_rights
