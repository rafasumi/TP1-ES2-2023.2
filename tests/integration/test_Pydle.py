import unittest

from src.Pydle import Pydle


class TestPydle(unittest.TestCase):
    def setUp(self):
        self.pydle = Pydle()

    def test_get_random_word_gets_word_in_correct_file(self):
        file_name = 'data/words_intermediate.txt'
        word = self.pydle.get_random_word(file_name)

        with open(file_name, 'r') as file:
            self.assertTrue(word in file.read())
