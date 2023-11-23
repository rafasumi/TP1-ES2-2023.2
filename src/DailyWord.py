import src.constants as consts

import csv
from datetime import date
import os

import pandas as pd


class DailyWord:
    def __init__(self):
        self.start_date = date(2023, 10, 13)

    def get_daily_word(self, file_name):
        today = date.today()

        with open(file_name, encoding='utf-8') as words_file:
            words = words_file.readlines()
            day_offset = abs((today - self.start_date).days) % len(words)

            return words[day_offset].strip()

    def save_daily_word_results(self, tries, word_size, victory):
        file_exists = os.path.exists(consts.SAVE_FILE)
        os.makedirs(consts.SAVE_DIR, exist_ok=True)

        with open(consts.SAVE_FILE, mode='a') as save_file:
            fields = ['Date', 'WordSize', 'Tries', 'Victory']
            csv_writer = csv.DictWriter(
                save_file, fieldnames=fields, delimiter=',')

            if not file_exists:
                csv_writer.writeheader()

            today_isoformat = date.today().isoformat()
            csv_writer.writerow(
                {'Date': today_isoformat, 'WordSize': word_size, 'Tries': tries,
                 'Victory': victory})

    def already_played_daily_word_today(self, word_size):
        if not os.path.exists(consts.SAVE_FILE):
            return False

        daily = pd.read_csv(consts.SAVE_FILE, sep=',')
        today_isoformat = date.today().isoformat()

        return ((daily.Date == today_isoformat) & (daily.WordSize == word_size)).any()

    def compute_statistics(self, word_size):
        daily_history = pd.read_csv(consts.SAVE_FILE, sep=',')
        daily_history = daily_history[daily_history.WordSize == word_size]
        successful_daily_history = daily_history[daily_history.Victory == True]

        times_played = len(daily_history)
        difficulty = consts.DIFFICULTY_MAP[word_size]
        win_rate = len(successful_daily_history) / len(daily_history)

        occurrences_of_number_of_tries = successful_daily_history.Tries.value_counts()
        most_common_number_of_tries = occurrences_of_number_of_tries.max()

        return (times_played, difficulty, win_rate, occurrences_of_number_of_tries, most_common_number_of_tries)
