import unittest

from src.Pydle import Pydle
import src.constants as consts


class TestPydle(unittest.TestCase):
    def setUp(self):
        self.pydle = Pydle()

    def test_compute_char_count(self):
        word = 'ancient'
        expected_dict = {'a': 1, 'c': 1, 'e': 1, 'i': 1, 'n': 2, 't': 1}

        self.assertEqual(self.pydle.compute_char_count(word), expected_dict)

    def test_compute_guess_colors_and_update_keyboard_colors_partially_correct_guess(self):
        guessed_word = 'SNAKE'
        secret_word = 'SIREN'

        color_dict = self.pydle.init_color_dict()
        guess_display = [f'{consts.BWHITE}_{consts.CEND}']*len(secret_word)

        expected_dict = self.pydle.init_color_dict()
        expected_dict['S'] = consts.FBGREEN
        expected_dict['N'] = consts.FBYELLOW
        expected_dict['A'] = consts.FBLACK
        expected_dict['K'] = consts.FBLACK
        expected_dict['E'] = consts.FBYELLOW

        self.pydle.compute_guess_colors_and_update_keyboard_colors(
            guessed_word, secret_word, color_dict, guess_display)
        self.assertEqual(color_dict, expected_dict)

    def test_compute_guess_colors_and_update_keyboard_colors_incorrect_guess(self):
        guessed_word = 'ABOUT'
        secret_word = 'SIREN'

        color_dict = self.pydle.init_color_dict()
        guess_display = [f'{consts.BWHITE}_{consts.CEND}']*len(secret_word)

        expected_dict = self.pydle.init_color_dict()
        expected_dict['A'] = consts.FBLACK
        expected_dict['B'] = consts.FBLACK
        expected_dict['O'] = consts.FBLACK
        expected_dict['U'] = consts.FBLACK
        expected_dict['T'] = consts.FBLACK

        self.pydle.compute_guess_colors_and_update_keyboard_colors(
            guessed_word, secret_word, color_dict, guess_display)
        self.assertEqual(color_dict, expected_dict)

    def test_compute_guess_colors_and_update_keyboard_colors_correct_guess(self):
        guessed_word = 'WHILE'
        secret_word = 'WHILE'

        color_dict = self.pydle.init_color_dict()
        guess_display = [f'{consts.BWHITE}_{consts.CEND}']*len(secret_word)

        expected_dict = self.pydle.init_color_dict()
        expected_dict['W'] = consts.FBGREEN
        expected_dict['H'] = consts.FBGREEN
        expected_dict['I'] = consts.FBGREEN
        expected_dict['L'] = consts.FBGREEN
        expected_dict['E'] = consts.FBGREEN

        self.pydle.compute_guess_colors_and_update_keyboard_colors(
            guessed_word, secret_word, color_dict, guess_display)
        self.assertEqual(color_dict, expected_dict)

    def test_compute_guess_colors_and_update_keyboard_colors_guess_display_with_repeated_letter(self):
        guessed_word = 'HELLO'
        secret_word = 'WHILE'

        color_dict = self.pydle.init_color_dict()
        guess_display = [f'{consts.BWHITE}_{consts.CEND}']*len(secret_word)

        expected_guess_display = []
        expected_guess_display.append(f'{consts.BYELLOW}H{consts.CEND}')
        expected_guess_display.append(f'{consts.BYELLOW}E{consts.CEND}')
        expected_guess_display.append(f'{consts.BWHITE}L{consts.CEND}')
        expected_guess_display.append(f'{consts.BGREEN}L{consts.CEND}')
        expected_guess_display.append(f'{consts.BWHITE}O{consts.CEND}')

        self.pydle.compute_guess_colors_and_update_keyboard_colors(
            guessed_word, secret_word, color_dict, guess_display)
        self.assertEqual(guess_display, expected_guess_display)

    def test_compute_guess_colors_and_update_keyboard_colors_guess_display_with_repeated_letter_wrong_position(self):
        guessed_word = 'HELLO'
        secret_word = 'LILAC'

        color_dict = self.pydle.init_color_dict()
        guess_display = [f'{consts.BWHITE}_{consts.CEND}']*len(secret_word)

        expected_guess_display = []
        expected_guess_display.append(f'{consts.BWHITE}H{consts.CEND}')
        expected_guess_display.append(f'{consts.BWHITE}E{consts.CEND}')
        expected_guess_display.append(f'{consts.BGREEN}L{consts.CEND}')
        expected_guess_display.append(f'{consts.BYELLOW}L{consts.CEND}')
        expected_guess_display.append(f'{consts.BWHITE}O{consts.CEND}')

        self.pydle.compute_guess_colors_and_update_keyboard_colors(
            guessed_word, secret_word, color_dict, guess_display)
        self.assertEqual(guess_display, expected_guess_display)
