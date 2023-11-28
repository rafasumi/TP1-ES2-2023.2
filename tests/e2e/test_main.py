import unittest
import subprocess
import sys


class TestMain(unittest.TestCase):
    def setUp(self):
        self.command = [sys.executable, 'main.py']
        self.EXIT_SUCCESS = 0

    def test_exit_with_exit_command(self):
        process = subprocess.Popen(
            self.command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

        process.communicate(input=b'2\n')

        exit_code = process.wait()

        self.assertEqual(exit_code, self.EXIT_SUCCESS)

    def test_exit_gracefully_with_eof(self):
        process = subprocess.Popen(
            self.command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

        process.communicate()

        exit_code = process.wait()

        self.assertEqual(exit_code, self.EXIT_SUCCESS)
