import unittest
import signal
import subprocess
import sys
import time


class TestMain(unittest.TestCase):
    def setUp(self):
        self.command = [sys.executable, 'main.py']
        self.EXIT_SUCCESS = 0

    def test_quit_gracefully_with_interrupt(self):
        process = subprocess.Popen(
            self.command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

        time.sleep(2)
        process.send_signal(signal.SIGINT)

        exit_code = process.wait()

        self.assertEqual(exit_code, self.EXIT_SUCCESS)

    def test_quit_gracefully_with_eof(self):
        process = subprocess.Popen(
            self.command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

        process.stdin.close()

        exit_code = process.wait()

        self.assertEqual(exit_code, self.EXIT_SUCCESS)
