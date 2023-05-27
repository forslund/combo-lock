import os
import platform
import tempfile

from memory_tempfile import MemoryTempfile

def get_ram_directory(folder):
    """ Fallback to a regular temp directory on unsupported platforms. """
    if platform.system() == "Linux":
        temp_dir = MemoryTempfile(fallback=True).gettempdir()
    else:
        temp_dir = tempfile.gettempdir()
    path = os.path.join(temp_dir, folder)
    os.makedirs(path, exist_ok=True)
    return path

