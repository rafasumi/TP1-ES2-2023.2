
from src.DailyWord import DailyWord
from src.InputHandler import InputHandler
from src.Interface import Interface
import src.constants as consts

import random


class Pydle:
    def __init__(self):
        self.interface = Interface()
        self.daily_word = DailyWord()
        self.input_handler = InputHandler()

    def start_game_loop(self):
        self.interface.display_title_and_rules()
        print(consts.FBWHITE + '\nWhat do you want to do now?' + consts.CEND)

        while self.input_handler.check_play_or_exit() != consts.EXIT:
            game_mode = self.input_handler.check_game_mode()
            if game_mode in (consts.CLASSIC, consts.DAILY):
                difficulty = self.input_handler.check_difficulty()
                if difficulty == consts.EASY:
                    word_size = 5
                    file_name = consts.EASY_WORDS_FILE
                elif difficulty == consts.INTERMEDIATE:
                    word_size = 6
                    file_name = consts.INTERMEDIATE_WORDS_FILE
                elif difficulty == consts.HARD:
                    word_size = 7
                    file_name = consts.HARD_WORDS_FILE

                is_daily = game_mode == consts.DAILY
                self.play(word_size, file_name, is_daily)
            elif game_mode == consts.THEMED:
                theme = self.input_handler.check_theme()
                word_size = 5
                if theme == consts.FOOD:
                    file_name = consts.FOOD_WORDS_FILE
                elif theme == consts.MUSIC:
                    file_name = consts.MUSIC_WORDS_FILE
                elif theme == consts.BODY:
                    file_name = consts.BODY_WORDS_FILE
                elif theme == consts.SPORTS:
                    file_name = consts.SPORTS_WORDS_FILE

                self.play(word_size, file_name)

    def get_random_word(self, file_name):
        with open(file_name, encoding='utf-8') as words_file:
            return random.choice(words_file.readlines()).strip()

    def compute_char_count(self, string):
        char_count = {}

        for char in string:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        return char_count

    def init_color_dict(self):
        return {letter: consts.FBWHITE for letter in consts.LETTERS}

    def compute_guess_colors_and_update_keyboard_colors(self, guessed_word, secret_word, color_dict, guess_display):
        char_count = self.compute_char_count(secret_word)
        uncolored_indexes = []

        for (index, char) in enumerate(guessed_word):
            if char == secret_word[index]:
                guess_display[index] = consts.BGREEN + char + consts.CEND
                color_dict.update({char: consts.FBGREEN})
                char_count[char] -= 1
            else:
                uncolored_indexes.append(index)

        for index in uncolored_indexes:
            char = guessed_word[index]
            if char in char_count and char_count.get(char) > 0:
                guess_display[index] = consts.BYELLOW + char + consts.CEND
                if color_dict[char] != consts.FBGREEN:
                    color_dict.update({char: consts.FBYELLOW})
                char_count[char] -= 1
            else:
                guess_display[index] = consts.BWHITE + char + consts.CEND
                color_dict.update({char: consts.FBLACK})

    def play(self, word_size, file_name, is_daily=False):
        max_tries = word_size + 1
        if is_daily:
            daily_word = DailyWord()

            if daily_word.already_played_daily_word_today(word_size):
                print("You've already played today's word in this difficulty!\n")
                return

            secret_word = daily_word.get_daily_word(file_name)
        else:
            secret_word = self.get_random_word(file_name)

        base_string = f'{consts.BWHITE}_{consts.CEND}'
        guesses = [[base_string]*word_size for _ in range(max_tries)]

        tries = 0
        victory = False

        color_dict = self.init_color_dict()

        while tries < max_tries:
            self.interface.display_guesses(guesses, tries)
            print()
            self.interface.display_colored_keyboard(color_dict)

            guessed_word = self.input_handler.get_user_guess(word_size)

            print()

            self.compute_guess_colors_and_update_keyboard_colors(
                guessed_word, secret_word, color_dict, guesses[tries])

            tries += 1

            if guessed_word == secret_word:
                victory = True
                break

        self.interface.display_guesses(guesses, tries)
        print()

        if victory:
            print('Congratulations!')
            self.interface.display_winning_art()
        else:
            print('What a bummer :(')
            self.interface.display_losing_art()
            print(f'The word was "{secret_word}". Try again!')

        self.interface.display_meanings_of_word(secret_word)
        print()

        if is_daily:
            daily_word.save_daily_word_results(tries, word_size, victory)
            self.interface.display_statistics_and_distribution(
                daily_word, word_size, tries)
