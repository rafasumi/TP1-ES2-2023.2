import src.constants as consts

import readline

from spellchecker import SpellChecker

class InputHandler:
    def __init__(self):
        self.spell_checker = SpellChecker()
        self.spell_checker.word_frequency.load_text_file(consts.EASY_WORDS_FILE)
        self.spell_checker.word_frequency.load_text_file(consts.INTERMEDIATE_WORDS_FILE)
        self.spell_checker.word_frequency.load_text_file(consts.HARD_WORDS_FILE)
        self.spell_checker.word_frequency.load_text_file(consts.FOOD_WORDS_FILE)

    def is_valid_numeric_option(self, option, start, end):
        if not option.isnumeric():
            print('You must give a number!')
            return False

        option_int = int(option)
        if start > option_int or option_int > end:
            print('Invalid option')
            return False

        return True

    def get_numeric_option(self, start, end):
        while True:
            option = input('Select: ').strip()

            if not self.is_valid_numeric_option(option, start, end):
                continue
            else:
                break

        return int(option)

    def check_play_or_exit(self):
        print(consts.FBWHITE + '1)' + consts.CEND +
              consts.FBGREEN + ' Play' + consts.CEND)
        print(consts.FBWHITE + '2)' + consts.CEND +
              consts.FBRED + ' Exit' + consts.CEND + '\n')

        decision = self.get_numeric_option(1, 2)

        return decision

    def check_game_mode(self):
        print(consts.FBWHITE + '\nChoose your game mode:' + consts.CEND)
        print(consts.FBWHITE + '1)' + consts.CEND +
              consts.FBCYAN + ' Classic' + consts.CEND)
        print(consts.FBWHITE + '2)' + consts.CEND +
              consts.FBBLUE + ' Daily Word' + consts.CEND)
        print(consts.FBWHITE + '3)' + consts.CEND +
              consts.FBMAGENTA + ' Themed' + consts.CEND + '\n')

        game_mode = self.get_numeric_option(1, 3)

        return game_mode

    def check_difficulty(self):
        print(consts.FBWHITE + '\nChoose difficulty:' + consts.CEND)
        print(consts.FBWHITE + '1)' + consts.CEND +
              consts.FBGREEN + ' Easy (5 letters)' + consts.CEND)
        print(consts.FBWHITE + '2)' + consts.CEND +
              consts.FBYELLOW + ' Intermediate (6 letters)' + consts.CEND)
        print(consts.FBWHITE + '3)' + consts.CEND +
              consts.FBRED + ' Hard (7 letters)' + consts.CEND + '\n')

        difficulty = self.get_numeric_option(1, 3)

        print()

        return difficulty

    def check_theme(self):
        print(consts.FBWHITE + '\nChoose theme:' + consts.CEND)
        print(consts.FBWHITE + '1)' + consts.CEND +
              consts.FBYELLOW + ' Food' + consts.CEND)
        print(consts.FBWHITE + '2)' + consts.CEND +
              consts.FBMAGENTA + ' Music' + consts.CEND)
        print(consts.FBWHITE + '3)' + consts.CEND +
              consts.FBCYAN + ' Body parts' + consts.CEND)
        print(consts.FBWHITE + '4)' + consts.CEND +
              consts.FBGREEN + ' Sports' + consts.CEND + '\n')

        theme = self.get_numeric_option(1, 4)

        print()

        return theme

    def get_user_guess(self, word_size):
        while True:
            guessed_word = input('Type your guess: ').strip().upper()

            if self.is_valid_guess(guessed_word, word_size):
                break
    
        return guessed_word

    def is_valid_guess(self, word, word_size):
        if len(word) != word_size:
            print(f'Your guess must have {word_size} characters!')
            return False
        elif not word.isalpha():
            print('Your guess must contain only alphabet letters!')
            return False
        elif not word in self.spell_checker:
            print('Your guess must be a valid english word!')
            return False

        return True