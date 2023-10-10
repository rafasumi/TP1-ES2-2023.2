from random import choice
from sys import stdout
from time import sleep
from enchant import Dict
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

CLASSIC = 1
THEMED = 2
DAILYWORDLE = 3
DAILYPYDLE = 4
EASY = 1
INTERMEDIATE = 2
HARD = 3

def show_title_and_rules():
    
    welcome_text = "Welcome to..."
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

    colored_title = ""
    for (index,char) in enumerate(title):
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

    print(FBWHITE + "\nHow to play..." + CEND)
    rules = "1. Letters that are in the answer and in the right place turn " + BGREEN + "green" + CEND + ".\n\
2. Letters that are in the answer but in the wrong place turn " + BYELLOW + "yellow" + CEND + ".\n\
3. Letters that are not in the answer turn " + BWHITE + "gray" + CEND + ".\n\
4. Letters can appear more than once. So if your guess includes two of one letter, they may both turn yellow, both turn green, or one could be yellow and the other green.\n\
5. Each guess must be a valid word in the English dictionary. You can't guess ABCDE, for instance.\n"
    print(rules)

def check_play_or_exit(first_game=False):
    if not first_game:
        print(FBWHITE + "\nWhat do you want to do now?" + CEND)
    print(FBWHITE + "1)" + CEND + FBGREEN + " Play" + CEND)
    print(FBWHITE + "2)" + CEND + FBRED + " Exit" + CEND + "\n")
    print('Select: ', end='')
    decision = int(input().strip())
    if decision == 2:
        decision = 0
    return decision

def check_game_mode():
    print(FBWHITE + "\nChoose your game mode:" + CEND)
    print(FBWHITE + "1)" + CEND + FBCYAN + " Classic" + CEND)
    print(FBWHITE + "2)" + CEND + FBMAGENTA + " Themed" + CEND)
    print(FBWHITE + "3)" + CEND + FBYELLOW + " Daily Wordle" + CEND)
    print(FBWHITE + "4)" + CEND + FBBLUE + " Daily Pydle" + CEND + "\n")
    print('Select: ', end='')
    classic_or_themed = int(input().strip())
    return classic_or_themed

def check_difficulty():
    print(FBWHITE + "\nChoose difficulty:" + CEND)
    print(FBWHITE + "1)" + CEND + FBGREEN + " Easy" + CEND)
    print(FBWHITE + "2)" + CEND + FBYELLOW + " Intermediate" + CEND)
    print(FBWHITE + "3)" + CEND + FBRED + " Hard" + CEND + "\n")
    print('Select: ', end='')
    difficulty = int(input().strip())
    print()
    return difficulty

def get_count_dict(str):
    count_dict = dict()

    for char in str:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    return count_dict

def get_meaning_of_word(secret_word):
    dic = PyDictionary()
    meanings = dic.meaning(secret_word)
    print(FBWHITE + "\nMeanings: " + CEND)
    meanings_list = list(meanings.values())
    flat_meanings_list = [item for sublist in meanings_list for item in sublist]
    print(" - " + flat_meanings_list[0])
    print(" - " + flat_meanings_list[1])
    print(" - " + flat_meanings_list[2])


def get_secret_word(file_name):
    with open(file_name, encoding='utf-8') as words:
        return choice(words.readlines()).strip()


def is_valid_guess(word, word_size):
    english_dictionary = Dict('en_US')

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
                sleep(0.2)
            print(letter, end='')
            stdout.flush()
        print()
        sleep(0.1)


def play(word_size=5, file_name = 'data/words_5.txt'):
    max_tries = word_size + 1
    secret_word = get_secret_word(file_name)

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

        uncolored_indexes = list()
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

    get_meaning_of_word(secret_word)


def main():

    show_title_and_rules()
    first_game = True
    while check_play_or_exit(first_game):
        game_mode = check_game_mode()
        if game_mode == CLASSIC:
            difficulty = check_difficulty()
            if difficulty == EASY:
                word_size = 5
                file_name = 'data/words_5.txt'
                play()
                first_game = False
            elif difficulty == INTERMEDIATE:
                word_size = 6
                file_name = 'data/words_6.txt'
                play(word_size, file_name)
                first_game = False
            elif difficulty == HARD:
                word_size = 7
                file_name = 'data/words_7.txt'
                play(word_size, file_name)
                first_game = False
            else:
                # Tratamento de erro
                pass
        elif game_mode == THEMED:
            # Listar temas e lançar jogo
            first_game = False
            pass
        elif game_mode == DAILYWORDLE:
            # Daily Wordle
            first_game = False
            pass
        elif game_mode == DAILYPYDLE:
            # Daily Pydle
            first_game = False
            pass
        else:
            # Tratamento de erro
            pass

if __name__ == '__main__':
    main()
