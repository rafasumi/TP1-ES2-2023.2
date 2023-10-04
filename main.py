from random import choice
from sys import stdout
from time import sleep
from enchant import Dict

CCORRECT = '\33[1;30;42m'
CPARTIAL = '\33[1;30;103m'
CWRONG = '\33[1;30;47m'
CEND = '\33[0m'


def get_count_dict(str):
    count_dict = dict()

    for char in str:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    return count_dict


def get_secret_word():
    with open('data/words_5.txt', encoding='utf-8') as words:
        return choice(words.readlines()).strip()


def is_valid_guess(word, word_size):
    english_dictionary = Dict('en_US')

    if len(word) != word_size:
        print('Your guess must have 5 characters!')
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


def play(max_tries=6, word_size=5):
    secret_word = get_secret_word()

    base_string = f'{CWRONG}_{CEND}'
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
                guesses[tries][index] = CCORRECT + char + CEND
                count_dict[char] -= 1
            else:
                uncolored_indexes.append(index)

        for index in uncolored_indexes:
            char = guessed_word[index]
            if char in count_dict and count_dict.get(char) > 0:
                guesses[tries][index] = CPARTIAL + char + CEND
                count_dict[char] -= 1
            else:
                guesses[tries][index] = CWRONG + char + CEND

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



def main():
    max_tries = 6
    word_size = 5

    play(max_tries, word_size)


if __name__ == '__main__':
    main()
