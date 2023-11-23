import src.constants as consts

import math
import os
import time

from PyDictionary import PyDictionary


class Interface:
    def __init__(self):
        self.dic = PyDictionary()

    def display_title_and_rules(self):
        self._display_title()
        self._display_rules()

    def _display_title(self):
        welcome_text = 'Welcome to...'
        title = "\
    .----------------.  .----------------.  .----------------.  .----------------.  .----------------.\n\
    | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |\n\
    | |   ______     | || |  ____  ____  | || |  ________    | || |   _____      | || |  _________   | |\n\
    | |  |_   __ \   | || | |_  _||_  _| | || | |_   ___ `.  | || |  |_   _|     | || | |_   ___  |  | |\n\
    | |    | |__) |  | || |   \ \  / /   | || |   | |   `. \ | || |    | |       | || |   | |_  \_|  | |\n\
    | |    |  ___/   | || |    \ \/ /    | || |   | |    | | | || |    | |   _   | || |   |  _|  _   | |\n\
    | |   _| |_      | || |    _|  |_    | || |  _| |___.' / | || |   _| |__/ |  | || |  _| |___/ |  | |\n\
    | |  |_____|     | || |   |______|   | || | |________.'  | || |  |________|  | || | |_________|  | |\n\
    | |              | || |              | || |              | || |              | || |              | |\n\
    | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |\n\
    '----------------'  '----------------'  '----------------'  '----------------'  '----------------' "

        print()
        print(consts.FBWHITE + welcome_text + consts.CEND)
        print()

        colored_title = ''
        for (index, char) in enumerate(title):
            if index % 100 < 20:
                colored_title += consts.FBGREEN + char + consts.CEND
            elif index % 100 >= 20 and index % 100 < 40:
                colored_title += consts.FBMAGENTA + char + consts.CEND
            elif index % 100 >= 40 and index % 100 < 60:
                colored_title += consts.FBCYAN + char + consts.CEND
            elif index % 100 >= 60 and index % 100 < 80:
                colored_title += consts.FBYELLOW + char + consts.CEND
            elif index % 100 >= 80 and index % 100 < 100:
                colored_title += consts.FBBLUE + char + consts.CEND

        print(colored_title)

    def _display_rules(self):
        print(consts.FBWHITE + '\nHow to play...' + consts.CEND)
        rules = "\
    1. Letters that are in the answer and in the right place turn " + consts.BGREEN + "green" + consts.CEND + ".\n\
    2. Letters that are in the answer but in the wrong place turn " + consts.BYELLOW + "yellow" + consts.CEND + ".\n\
    3. Letters that are not in the answer turn " + consts.BWHITE + "gray" + consts.CEND + ".\n\
    4. Letters can appear more than once. So if your guess includes two of one letter, they may both turn yellow, \
    both turn green, or one could be yellow and the other green.\n\
    5. Each guess must be a valid word in the English dictionary. You can't guess ABCDE, for instance.\n\
    6. The guesses are case insensitive, which means that it doesn't matter whether you write in lower or upper case.\n"
        print(rules)

    def display_guesses(self, guesses, tries):
        for (index, guess) in enumerate(guesses):
            for letter in guess:
                if index == tries - 1:
                    time.sleep(0.2)

                print(letter, end='', flush=True)

            print()
            time.sleep(0.1)

    def display_meanings_of_word(self, word):
        meanings = self.dic.meaning(word, disable_errors=True)
        if meanings is None:
            return

        flat_meanings_list = [item for sublist in meanings.values()
                              for item in sublist]
        num_meanings = min(3, len(flat_meanings_list))

        print(consts.FBWHITE + f'\nMeanings of {word}' + consts.CEND)

        for i in range(num_meanings):
            print(' - ' + flat_meanings_list[i])

    def display_colored_keyboard(self, color_dict):
        keyboard = "+---+---+---+---+---+---+---+---+---+---+\n"
        count_letters = 0
        first_row = 10
        for i in range(first_row):
            keyboard += self._display_colored_key(consts.LETTERS[i], color_dict)

        keyboard += "|\n+---+---+---+---+---+---+---+---+---+---+\n  "
        count_letters += first_row
        second_row = 9
        for i in range(second_row):
            keyboard += self._display_colored_key(
                consts.LETTERS[i + count_letters], color_dict)
        keyboard += "|\n  +---+---+---+---+---+---+---+---+---+\n      "
        count_letters += second_row
        third_row = 7
        for i in range(third_row):
            keyboard += self._display_colored_key(
                consts.LETTERS[i + count_letters], color_dict)

        keyboard += "|\n      +---+---+---+---+---+---+---+\n"

        print(keyboard)

    def _display_colored_key(self, letter, color_dict):
        key = "| " + color_dict[letter] + letter + consts.CEND + " "
        return key

    def display_winning_art(self):
        art = "\
                                                             _  _  \n\
                                                            | || | \n\
      _   __   .--.   __   _    _   _   __   .--.   _ .--.  | || | \n\
     [ \ [  ]/ .'`\ \[  | | |  [ \ [ \ [  ]/ .'`\ \[ `.-. | | || | \n\
      \ '/ / | \__. | | \_/ |,  \ \/\ \/ / | \__. | | | | | |_||_| \n\
    [\_:  /   '.__.'  '.__.'_/   \__/\__/   '.__.' [___||__](_)(_) \n\
     \__.'                                                         \n\n\
    "

        colored_text = ""
        for char in art:
            colored_text += consts.FBGREEN + char + consts.CEND

        print(colored_text)

    def display_losing_art(self):
        art = "\
                               ,--.               ,--.   \n\
    ,--. ,--.,---. ,--.,--.    |  | ,---.  ,---.,-'  '-. \n\
    \   '  /| .-. ||  ||  |    |  || .-. |(  .-''-.  .-' \n\
      \   ' ' '-' ''  ''  '    |  |' '-' '.-'  `) |  |   \n\
    .-'  /   `---'  `----'     `--' `---' `----'  `--'   \n\
    `---'\n"

        colored_text = ""
        for char in art:
            colored_text += consts.FBRED + char + consts.CEND

        print(colored_text)

    def display_statistics_and_distribution(self, daily_word, word_size, tries_last_game):
        time.sleep(0.2)

        (times_played, difficulty, win_rate, occurrences_of_number_of_tries,
         most_common_number_of_tries) = daily_word.compute_statistics(word_size)
        max_tries = word_size + 1

        self._display_daily_statistics(times_played, difficulty, win_rate)
        self._display_distribution(occurrences_of_number_of_tries,
                                 most_common_number_of_tries, tries_last_game, max_tries)

        print()

    def _display_daily_statistics(self, times_played, difficulty, win_rate):
        print(f'{consts.FBWHITE}Statistics{consts.CEND}')

        print(f'\tYou played Daily Word {consts.FBMAGENTA}{times_played}{consts.CEND} \
    times in {difficulty} difficulty')

        print(
            f'\tYou have won {consts.FBCYAN}{win_rate:.2%}{consts.CEND} of times!')

    def _display_distribution(self, occurrences_of_number_of_tries, most_common_number_of_tries,
                            tries_last_game, max_tries):
        terminal_width = os.get_terminal_size().columns
        total_width = terminal_width / 3

        print(f'{consts.FBWHITE}Guess distribution{consts.CEND}')
        for i_tries in range(1, max_tries + 1):
            print(f'\t{consts.FBWHITE}{i_tries}:{consts.CEND} ', end='')

            if i_tries in occurrences_of_number_of_tries:
                ratio = occurrences_of_number_of_tries[i_tries] / \
                    most_common_number_of_tries
                width = math.ceil(ratio * total_width)
            else:
                width = 0

            if i_tries == tries_last_game:
                bar = consts.BGREEN + ' ' + consts.CEND
            else:
                bar = consts.BGRAY + ' ' + consts.CEND

            for _ in range(width):
                print(bar, end='')

            print()
