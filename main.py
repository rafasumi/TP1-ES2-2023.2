import threading

from playsound import playsound

import constants as consts
import display
import game


def background_music_loop():
    while True:
        playsound('assets/sound/here_comes_the_sun.ogg', block=True)


def main():
    music_thread = threading.Thread(
        target=background_music_loop, daemon=True, name='backgroundMusic')
    music_thread.start()

    display.show_title_and_rules()
    print(consts.FBWHITE + '\nWhat do you want to do now?' + consts.CEND)
    while display.check_play_or_exit() != consts.EXIT:
        game_mode = display.check_game_mode()
        if game_mode in (consts.CLASSIC, consts.DAILY):
            difficulty = display.check_difficulty()
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
            game.play(word_size, file_name, is_daily)
        elif game_mode == consts.THEMED:
            theme = display.check_theme()
            word_size = 5
            if theme == consts.FOOD:
                file_name = consts.FOOD_WORDS_FILE
            elif theme == consts.MUSIC:
                file_name = consts.MUSIC_WORDS_FILE
            elif theme == consts.BODY:
                file_name = consts.BODY_WORDS_FILE
            elif theme == consts.SPORTS:
                file_name = consts.SPORTS_WORDS_FILE
            game.play(word_size, file_name)


if __name__ == '__main__':
    try:
        main()
    except EOFError:
        pass
    except KeyboardInterrupt:
        pass
