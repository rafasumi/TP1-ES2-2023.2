import constants as consts
import sys
import time
from PyDictionary import PyDictionary


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

    print(consts.FBWHITE + '\nHow to play...' + consts.CEND)
    rules = "1. Letters that are in the answer and in the right place turn " + consts.BGREEN + "green" + consts.CEND + ".\n\
2. Letters that are in the answer but in the wrong place turn " + consts.BYELLOW + "yellow" + consts.CEND + ".\n\
3. Letters that are not in the answer turn " + consts.BWHITE + "gray" + consts.CEND + ".\n\
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
    print(consts.FBWHITE + '1)' + consts.CEND +
          consts.FBGREEN + ' Play' + consts.CEND)
    print(consts.FBWHITE + '2)' + consts.CEND +
          consts.FBRED + ' Exit' + consts.CEND + '\n')

    decision = get_numeric_option(1, 2)

    return decision


def check_game_mode():
    print(consts.FBWHITE + '\nChoose your game mode:' + consts.CEND)
    print(consts.FBWHITE + '1)' + consts.CEND +
          consts.FBCYAN + ' Classic' + consts.CEND)
    print(consts.FBWHITE + '2)' + consts.CEND +
          consts.FBBLUE + ' Daily Word' + consts.CEND)
    print(consts.FBWHITE + '3)' + consts.CEND +
          consts.FBMAGENTA + ' Themed' + consts.CEND + '\n')

    game_mode = get_numeric_option(1, 3)

    return game_mode


def check_difficulty():
    print(consts.FBWHITE + '\nChoose difficulty:' + consts.CEND)
    print(consts.FBWHITE + '1)' + consts.CEND +
          consts.FBGREEN + ' Easy' + consts.CEND)
    print(consts.FBWHITE + '2)' + consts.CEND +
          consts.FBYELLOW + ' Intermediate' + consts.CEND)
    print(consts.FBWHITE + '3)' + consts.CEND +
          consts.FBRED + ' Hard' + consts.CEND + '\n')

    difficulty = get_numeric_option(1, 3)

    print()

    return difficulty


def print_guesses(guesses, tries):
    for (index, guess) in enumerate(guesses):
        for letter in guess:
            if index == tries - 1:
                time.sleep(0.2)

            print(letter, end='')
            sys.stdout.flush()

        print()
        time.sleep(0.1)


def print_meanings_of_word(word):
    print(consts.FBWHITE + f'\nMeanings of {word}' + consts.CEND)

    dic = PyDictionary()
    meanings = dic.meaning(word)
    flat_meanings_list = [item for sublist in meanings.values()
                          for item in sublist]
    num_meanings = min(3, len(flat_meanings_list))

    for i in range(num_meanings):
        print(' - ' + flat_meanings_list[i])

    print()
