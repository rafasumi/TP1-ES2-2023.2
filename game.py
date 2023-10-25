import csv
import os
import random
import readline

import enchant
import pandas as pd
from datetime import date

import constants as consts
import display


def get_count_dict(string):
    count_dict = {}

    for char in string:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    return count_dict


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


def save_daily_word_results(tries, word_size, victory):
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


def already_played_daily_word_today(word_size):
    if not os.path.exists(consts.SAVE_FILE):
        return False

    daily = pd.read_csv(consts.SAVE_FILE, sep=',')
    today_isoformat = date.today().isoformat()

    return ((daily.Date == today_isoformat) & (daily.WordSize == word_size)).any()


def init_color_dict():
    return {letter: consts.FBWHITE for letter in consts.LETTERS}


def compute_guess_colors(guessed_word, secret_word, count_dict, color_dict, guess_display):
    uncolored_indexes = []

    for (index, char) in enumerate(guessed_word):
        if char == secret_word[index]:
            guess_display[index] = consts.BGREEN + char + consts.CEND
            color_dict.update({char: consts.FBGREEN})
            count_dict[char] -= 1
        else:
            uncolored_indexes.append(index)

    for index in uncolored_indexes:
        char = guessed_word[index]
        if char in count_dict and count_dict.get(char) > 0:
            guess_display[index] = consts.BYELLOW + char + consts.CEND
            if color_dict[char] != consts.FBGREEN:
                color_dict.update({char: consts.FBYELLOW})
            count_dict[char] -= 1
        else:
            guess_display[index] = consts.BWHITE + char + consts.CEND
            color_dict.update({char: consts.FBLACK})


def play(word_size, file_name, is_daily=False):
    max_tries = word_size + 1
    if is_daily:
        if already_played_daily_word_today(word_size):
            print("You've already played today's word in this difficulty!\n")
            return

        secret_word = get_daily_word(file_name)
    else:
        secret_word = get_random_word(file_name)

    base_string = f'{consts.BWHITE}_{consts.CEND}'
    guesses = [[base_string]*word_size for _ in range(max_tries)]

    tries = 0
    victory = False

    color_dict = init_color_dict()

    while tries < max_tries:
        display.print_guesses(guesses, tries)
        print()
        display.print_colored_keyboard(color_dict)

        while True:
            guessed_word = input('Type your guess: ').strip().upper()

            if is_valid_guess(guessed_word, word_size):
                break

        print()

        count_dict = get_count_dict(secret_word)

        compute_guess_colors(guessed_word, secret_word, count_dict, color_dict, guesses[tries])

        tries += 1

        if guessed_word == secret_word:
            victory = True
            break

    display.print_guesses(guesses, tries)
    print()

    if victory:
        print('Congratulations!')
        display.print_winning_art()
    else:
        print('What a bummer :(')
        display.print_losing_art()
        print(f'The word was "{secret_word}". Try again!')

    display.print_meanings_of_word(secret_word)
    print()

    if is_daily:
        save_daily_word_results(tries, word_size, victory)
        display.print_statistics_and_distribution(word_size, max_tries, tries)
