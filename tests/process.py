"""
Test process run by the test case. The file will

Expects three arguments
 identifier lock_file sleep_1 sleep_2

 identifier: process identifier to be written to the out file
 lock_file: is the path to the lockfile to use
 sleep_1: is the time to sleep before locking
 sleep_2: is the time to sleep after the locking.
"""
import sys
import time

from combo_lock import ComboLock


if __name__ == '__main__':
    identifier = sys.argv[1]
    lock_file = sys.argv[2]
    sleep_1 = float(sys.argv[3])
    sleep_2 = float(sys.argv[4])

    lock = ComboLock(lock_file)
    time.sleep(sleep_1)
    with lock:
        time.sleep(sleep_2)
        with open('/tmp/test_process.lock', 'a') as f:
            f.write(identifier)
