import unittest
from unittest.mock import mock_open, patch
from datetime import date

from src.DailyWord import DailyWord


class AnyStringWith(str):
    def __eq__(self, other):
        return self in other


class TestDailyWord(unittest.TestCase):
    def setUp(self):
        self.daily_word = DailyWord()

    @patch('builtins.open', new_callable=mock_open)
    def test_save_daily_word_results(self, mock_file_open):
        today = date.today().isoformat()
        tries = 4
        word_size = 5
        victory = True

        self.daily_word.save_daily_word_results(tries, word_size, victory)

        mock_file_open().write.assert_called_with(AnyStringWith(
            f'{today},{word_size},{tries},{victory}'))

    @patch('os.path.exists', return_value=True)
    def test_already_played_daily_word_today(self, _):
        csv_header = 'Date,WordSize,Tries,Victory'

        today = date.today().isoformat()
        tries = 4
        word_size = 5
        victory = True
        csv_row = f'{today},{word_size},{tries},{victory}'

        read_data = csv_header + '\n' + csv_row + '\n'

        with patch('builtins.open', new_callable=mock_open, read_data=read_data):
            already_played = self.daily_word.already_played_daily_word_today(
                word_size)

        self.assertTrue(already_played)
