import os
from subprocess import Popen
from tempfile import mktemp
from threading import Thread
import time
from unittest import TestCase

from combo_lock import ComboLock


class TestComboLock(TestCase):
    def setUp(self):
        self.lock_file = mktemp()

    def tearDown(self):
        os.remove(self.lock_file)

    def test_thread_lock(self):
        lock = ComboLock(self.lock_file)
        call_order = []
        def thread_a():
            nonlocal call_order
            with lock:
                time.sleep(0.2)
                call_order.append('a')

        def thread_b():
            nonlocal call_order
            time.sleep(0.1)
            with lock:
                call_order.append('b')

        a = Thread(target=thread_a)
        b = Thread(target=thread_b)

        b.start()
        a.start()
        b.join()
        a.join()
        self.assertEqual(call_order, ['a', 'b'])

    def test_process_lock(self):
        test_process = os.path.join(os.path.dirname(__file__), 'process.py')
        test_output = '/tmp/test_process.lock'

        # Run processes
        a = Popen(['python3', test_process, 'a', self.lock_file, '0', '0.2'])
        b = Popen(['python3', test_process, 'b', self.lock_file, '0.1', '0'])
        a.wait()
        b.wait()

        # Read result
        with open(test_output, 'r') as f:
            result = f.read()
        os.remove(test_output)

        # Verify that the written order is correct
        self.assertEqual(result, 'ab')
