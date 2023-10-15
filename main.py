import csv
import os
import random
import sys
import time
import enchant
import pandas as pd

from datetime import date
from PyDictionary import PyDictionary

CEND = '\33[0m'
# Background colors
BBLACK = '\33[1;30;40m'
BRED = '\33[1;30;41m'
BGREEN = '\33[1;30;42m'
BYELLOW = '\33[1;30;43m'
BBLUE = '\33[1;30;44m'
BMAGENTA = '\33[1;30;45m'
BCYAN = '\33[1;30;46m'
BWHITE = '\33[1;30;47m'
BGRAY = '\33[1;30;100m'
BBRED = '\33[1;30;101m'
BBGREEN = '\33[1;30;102m'
BBYELLOW = '\33[1;30;103m'
BBBLUE = '\33[1;30;104m'
BBMAGENTA = '\33[1;30;105m'
BBCYAN = '\33[1;30;106m'
BBWHITE = '\33[1;30;107m'
# Font colors
FBRED = '\33[1;30;91m'
FBGREEN = '\33[1;30;92m'
FBYELLOW = '\33[1;30;93m'
FBBLUE = '\33[1;30;94m'
FBMAGENTA = '\33[1;30;95m'
FBCYAN = '\33[1;30;96m'
FBWHITE = '\33[1;30;97m'

EASY_WORDS_FILE = 'data/words_easy.txt'
INTERMEDIATE_WORDS_FILE = 'data/words_intermediate.txt'
HARD_WORDS_FILE = 'data/words_hard.txt'
SAVE_DIR = 'data/save'
SAVE_FILE = f'{SAVE_DIR}/daily.csv'

EXIT = 2
CLASSIC = 1
DAILY = 2
THEMED = 3
EASY = 1
INTERMEDIATE = 2
HARD = 3


def show_title_and_rules():
    welcome_text = 'Welcome to...'
    title = " .----------------.  .----------------.  .----------------.  .----------------.  .----------------.\n\
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
    print(FBWHITE + welcome_text + CEND)
    print()

    colored_title = ''
    for (index, char) in enumerate(title):
        if index % 100 < 20:
            colored_title += FBGREEN + char + CEND
        elif index % 100 >= 20 and index % 100 < 40:
            colored_title += FBMAGENTA + char + CEND
        elif index % 100 >= 40 and index % 100 < 60:
            colored_title += FBCYAN + char + CEND
        elif index % 100 >= 60 and index % 100 < 80:
            colored_title += FBYELLOW + char + CEND
        elif index % 100 >= 80 and index % 100 < 100:
            colored_title += FBBLUE + char + CEND

    print(colored_title)

    print(FBWHITE + '\nHow to play...' + CEND)
    rules = "1. Letters that are in the answer and in the right place turn " + BGREEN + "green" + CEND + ".\n\
2. Letters that are in the answer but in the wrong place turn " + BYELLOW + "yellow" + CEND + ".\n\
3. Letters that are not in the answer turn " + BWHITE + "gray" + CEND + ".\n\
4. Letters can appear more than once. So if your guess includes two of one letter, they may both turn yellow, both turn green, or one could be yellow and the other green.\n\
5. Each guess must be a valid word in the English dictionary. You can't guess ABCDE, for instance.\n"
    print(rules)


def get_numeric_option(start, end):
    while True:
        print('Select: ', end='')
        option = input().strip()
        if not option.isnumeric():
            print('You must give a number!')
            continue

        option = int(option)

        if start <= option <= end:
            break
        else:
            print('Invalid option!')

    return option


def check_play_or_exit():
    print(FBWHITE + '1)' + CEND + FBGREEN + ' Play' + CEND)
    print(FBWHITE + '2)' + CEND + FBRED + ' Exit' + CEND + '\n')

    decision = get_numeric_option(1, 2)

    return decision


def check_game_mode():
    print(FBWHITE + '\nChoose your game mode:' + CEND)
    print(FBWHITE + '1)' + CEND + FBCYAN + ' Classic' + CEND)
    print(FBWHITE + '2)' + CEND + FBBLUE + ' Daily Word' + CEND)
    print(FBWHITE + '3)' + CEND + FBMAGENTA + ' Themed' + CEND + '\n')

    game_mode = get_numeric_option(1, 3)

    return game_mode


def check_difficulty():
    print(FBWHITE + '\nChoose difficulty:' + CEND)
    print(FBWHITE + '1)' + CEND + FBGREEN + ' Easy' + CEND)
    print(FBWHITE + '2)' + CEND + FBYELLOW + ' Intermediate' + CEND)
    print(FBWHITE + '3)' + CEND + FBRED + ' Hard' + CEND + '\n')

    difficulty = get_numeric_option(1, 3)

    print()

    return difficulty


def get_count_dict(string):
    count_dict = {}

    for char in string:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    return count_dict


def print_meanings_of_word(word):
    print(FBWHITE + f'\nMeanings of {word}' + CEND)

    dic = PyDictionary()
    meanings = dic.meaning(word)
    flat_meanings_list = [item for sublist in meanings.values()
                          for item in sublist]
    num_meanings = min(3, len(flat_meanings_list))

    for i in range(num_meanings):
        print(' - ' + flat_meanings_list[i])

    print()


def get_random_word(file_name):
    with open(file_name, encoding='utf-8') as words_file:
        return random.choice(words_file.readlines()).strip()


def get_daily_word(file_name):
    start_date = date(2023, 10, 13)
    today = date.today()

    with open(file_name, encoding='utf-8') as words_file:
        words = words_file.readlines()
        day_offset = abs((today - start_date).days) % len(words)

        return words[day_offset].strip()


def is_valid_guess(word, word_size):
    english_dictionary = enchant.Dict('en_US')

    if len(word) != word_size:
        print(f'Your guess must have {word_size} characters!')
        return False
    elif not word.isalpha():
        print('Your guess must contain only alphabet letters!')
        return False
    elif not english_dictionary.check(word):
        print('Your guess must be a valid english word!')
        return False

    return True


def print_guesses(guesses, tries):
    for (index, guess) in enumerate(guesses):
        for letter in guess:
            if index == tries - 1:
                time.sleep(0.2)

            print(letter, end='')
            sys.stdout.flush()

        print()
        time.sleep(0.1)


def save_daily_word_results(tries, word_size):
    file_exists = os.path.exists(SAVE_FILE)
    os.makedirs(SAVE_DIR, exist_ok=True)

    with open(SAVE_FILE, mode='a') as save_file:
        fields = ['Date', 'WordSize', 'Tries']
        csv_writer = csv.DictWriter(
            save_file, fieldnames=fields, delimiter=',')

        if not file_exists:
            csv_writer.writeheader()

        today_isoformat = date.today().isoformat()
        csv_writer.writerow(
            {'Date': today_isoformat, 'WordSize': word_size, 'Tries': tries})


def already_played_daily_word_today(word_size):
    if not os.path.exists(SAVE_FILE):
        return False

    daily = pd.read_csv(SAVE_FILE, sep=',')
    today_isoformat = date.today().isoformat()

    return ((daily.Date == today_isoformat) & (daily.WordSize == word_size)).any()


def play(word_size, file_name, is_daily=False):
    max_tries = word_size + 1
    if is_daily:
        if already_played_daily_word_today(word_size):
            print("You've already played today's word in this difficulty!\n")
            return

        secret_word = get_daily_word(file_name)
    else:
        secret_word = get_random_word(file_name)

    base_string = f'{BWHITE}_{CEND}'
    guesses = [[base_string]*word_size for _ in range(max_tries)]

    tries = 0
    victory = False

    while tries < max_tries:
        print_guesses(guesses, tries)

        while True:
            print('Type your guess: ', end='')
            guessed_word = input().strip().upper()

            if is_valid_guess(guessed_word, word_size):
                break

        print()

        uncolored_indexes = []
        count_dict = get_count_dict(secret_word)
        for (index, char) in enumerate(guessed_word):
            if char == secret_word[index]:
                guesses[tries][index] = BGREEN + char + CEND
                count_dict[char] -= 1
            else:
                uncolored_indexes.append(index)

        for index in uncolored_indexes:
            char = guessed_word[index]
            if char in count_dict and count_dict.get(char) > 0:
                guesses[tries][index] = BYELLOW + char + CEND
                count_dict[char] -= 1
            else:
                guesses[tries][index] = BWHITE + char + CEND

        tries += 1

        if guessed_word == secret_word:
            victory = True
            break

    print_guesses(guesses, tries)
    print()

    if victory:
        print('Congratulations! You won!!')
    else:
        print('What a bummer :(')
        print(f'The word was "{secret_word}". Try again!')

    print_meanings_of_word(secret_word)

    if is_daily:
        save_daily_word_results(tries, word_size)


def main():
    show_title_and_rules()
    print(FBWHITE + '\nWhat do you want to do now?' + CEND)
    while check_play_or_exit() != EXIT:
        game_mode = check_game_mode()
        if game_mode in (CLASSIC, DAILY):
            difficulty = check_difficulty()
            if difficulty == EASY:
                word_size = 5
                file_name = EASY_WORDS_FILE
            elif difficulty == INTERMEDIATE:
                word_size = 6
                file_name = INTERMEDIATE_WORDS_FILE
            elif difficulty == HARD:
                word_size = 7
                file_name = HARD_WORDS_FILE

            is_daily = game_mode == DAILY
            play(word_size, file_name, is_daily)
        elif game_mode == THEMED:
            # Listar temas e lançar jogo
            pass


if __name__ == '__main__':
    main()
