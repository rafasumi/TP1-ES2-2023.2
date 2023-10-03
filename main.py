from random import choice
from enchant import Dict

CCORRECT = '\33[1;30;42m'
CPARTIAL = '\33[1;30;103m'
CWRONG = '\33[1;30;47m'
CEND = '\33[0m'


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


def play(max_tries=6, word_size=5):
    secret_word = get_secret_word()

    base_string = f'{CWRONG}_{CEND}' * word_size
    guesses = [base_string] * max_tries

    tries = 0

    print(secret_word)

    while tries < max_tries:
        for guess in guesses:
            print(guess)

        while True:
            print('Type your guess: ', end='')
            guessed_word = input().strip().upper()

            if is_valid_guess(guessed_word, word_size):
                break

        styled_guess = ''
        for (index, char) in enumerate(guessed_word):
            if char == secret_word[index]:
                styled_guess += CCORRECT
            elif char in secret_word:
                styled_guess += CPARTIAL
            else:
                styled_guess += CWRONG

            styled_guess += char + CEND

        guesses[tries] = styled_guess
        tries += 1

        if guessed_word == secret_word:
            break

    for guess in guesses:
        print(guess)


def main():
    max_tries = 6
    word_size = 5

    play(max_tries, word_size)


if __name__ == '__main__':
    main()
