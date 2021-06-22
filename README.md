# Combo Lock

The combo-lock is a combination of a process lock and a thread lock. Usable in cases both multiple threads and multiple processes are sharing the same resource such as a file in the file system.

The module utilizes the InterProcessLock from [fasteners](https://pypi.org/project/fasteners/) and the standard *Lock* from threading.

The InterProcessLock uses a filesystem lock so the initialization of the class requires a path for the lock file.

## Example

```python
from combo_lock import ComboLock

lock = ComboLock('/tmp/my.lock')

with lock:
    write_my_shared_resource()


```

A `NamedLock` will save the lock file to shared memory using [memory-tempfile](https://github.com/mbello/memory-tempfile)

```python
from combo_lock import NamedLock

lock = NamedLock('some_name')

with lock:
    write_my_shared_resource()
```

### History

The combo-lock was originally created for [Mycroft-core](https://github.com/mycroftai/mycroft-core) but as it's been useful in other projects a separate release seemed appropriate.
