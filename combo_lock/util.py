from memory_tempfile import MemoryTempfile
import os


def get_ram_directory(folder):
    tempfile = MemoryTempfile(fallback=True)
    path = os.path.join(tempfile.gettempdir(), folder)
    os.makedirs(path, exist_ok=True)
    return path

