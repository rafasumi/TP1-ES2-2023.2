import unittest
import os
import platform
import signal
import subprocess
import sys

import pexpect.fdpexpect


class TestMain(unittest.TestCase):
    def setUp(self):
        self.command = [sys.executable, 'main.py']
        self.EXIT_SUCCESS = 0

    def test_quit_gracefully_with_interrupt(self):
        if platform == 'Windows':
            flags = subprocess.CREATE_NEW_PROCESS_GROUP
        else:
            flags = 0

        process = subprocess.Popen(
            self.command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, creationflags=flags)

        stdout_expect = pexpect.fdpexpect.fdspawn(process.stdout.fileno())
        stdout_expect.expect('Select: ')

        if platform == 'Windows':
            os.kill(0, signal.CTRL_BREAK_EVENT)
        else:
            process.send_signal(signal.SIGINT)

        exit_code = process.wait()

        self.assertEqual(exit_code, self.EXIT_SUCCESS)

    def test_quit_gracefully_with_eof(self):
        process = subprocess.Popen(
            self.command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

        process.stdin.close()

        exit_code = process.wait()

        self.assertEqual(exit_code, self.EXIT_SUCCESS)
