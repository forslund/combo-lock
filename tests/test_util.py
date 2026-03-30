from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase
from unittest.mock import patch

from combo_lock.util import get_ram_directory, make_dir_with_global_permissions


class TestComboLock(TestCase):
    def test_ram_dir(self):
        ram_dir = get_ram_directory("test_combo_locks")
        assert ram_dir is not None
        access_rights = 0o777
        assert Path(ram_dir).stat().st_mode & access_rights == access_rights

    def test_make_dir_with_global_permissions_allows_existing_directory(self):
        with TemporaryDirectory() as tmpdir:
            path = Path(tmpdir, "combo_locks")
            path.mkdir()

            make_dir_with_global_permissions(path)

            assert path.is_dir()

    def test_make_dir_with_global_permissions_rejects_existing_file(self):
        with TemporaryDirectory() as tmpdir:
            path = Path(tmpdir, "combo_locks")
            path.write_text("not a directory")

            with self.assertRaises(FileExistsError):
                make_dir_with_global_permissions(path)

    def test_make_dir_with_global_permissions_handles_racing_directory_creation(self):
        with TemporaryDirectory() as tmpdir:
            path = Path(tmpdir, "combo_locks")
            original_mkdir = type(path).mkdir
            mkdir_called = False

            def racing_mkdir(this, *args, **kwargs):
                nonlocal mkdir_called
                if this == path and not mkdir_called:
                    mkdir_called = True
                    original_mkdir(this, *args, **kwargs)
                    raise FileExistsError(this)
                return original_mkdir(this, *args, **kwargs)

            with patch.object(type(path), "mkdir", new=racing_mkdir):
                make_dir_with_global_permissions(path)

            assert path.is_dir()
