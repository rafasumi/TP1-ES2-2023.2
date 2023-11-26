import unittest
import os
import signal
import subprocess
import sys


class TestMain(unittest.TestCase):
    def setUp(self):
        self.command = [sys.executable, 'main.py']

    def test_quit_gracefully_with_interrupt(self):
        process = subprocess.Popen(
            self.command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

        process.communicate()
        process.send_signal(signal.SIGINT)

        exit_code = process.wait()

        self.assertEqual(exit_code, os.EX_OK)

    def test_quit_gracefully_with_eof(self):
        process = subprocess.Popen(
            self.command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

        process.communicate()
        process.stdin.close()

        exit_code = process.wait()

        self.assertEqual(exit_code, os.EX_OK)
