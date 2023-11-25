import unittest

from src.InputHandler import InputHandler


class TestInputHandler(unittest.TestCase):
    def setUp(self):
        self.handler = InputHandler()

    def test_is_valid_numeric_option_invalidate_non_numeric(self):
        self.assertFalse(
            self.handler.is_valid_numeric_option('nonAlpha', 0, 10))

    def test_is_valid_numeric_option_invalidate_less_than(self):
        self.assertFalse(self.handler.is_valid_numeric_option('0', 1, 4))

    def test_is_valid_numeric_option_invalidate_greater_than(self):
        self.assertFalse(self.handler.is_valid_numeric_option('5', 1, 4))

    def test_is_valid_numeric_option_validate_lower_bound(self):
        self.assertTrue(self.handler.is_valid_numeric_option('1', 1, 4))

    def test_is_valid_numeric_option_validate_upper_bound(self):
        self.assertTrue(self.handler.is_valid_numeric_option('4', 1, 4))

    def test_is_valid_guess_invalidate_wrong_size(self):
        word = 'incorrect'
        word_size = 5
        self.assertFalse(self.handler.is_valid_guess(word, word_size))

    def test_is_valid_guess_invalidate_not_alpha(self):
        word = 'mine6'
        word_size = 5
        self.assertFalse(self.handler.is_valid_guess(word, word_size))

    def test_is_valid_guess_invalid_english_word(self):
        word = 'klash'
        word_size = 5
        self.assertFalse(self.handler.is_valid_guess(word, word_size))

    def test_is_valid_guess_validate_correct_guess(self):
        word = 'right'
        word_size = 5
        self.assertTrue(self.handler.is_valid_guess(word, word_size))
