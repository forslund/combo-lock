from pathlib import Path
import platform
import tempfile

from memory_tempfile import MemoryTempfile


def make_dir_with_global_permissions(path):
    """ Create directory and allow all to read/write to it. """
    path = Path(path)  # Handle string input
    if not path.exists():
        path.mkdir(parents=True)
        path.chmod(0o777)


def get_ram_directory(folder):
    """ Fallback to a regular temp directory on unsupported platforms. """
    if platform.system() == "Linux":
        temp_dir = MemoryTempfile(fallback=True).gettempdir()
    else:
        temp_dir = tempfile.gettempdir()
    path = Path(temp_dir, folder)
    make_dir_with_global_permissions(path)
    return str(path)
