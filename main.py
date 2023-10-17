import constants as consts
import display
import game


def main():
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
            # Listar temas e lançar jogo
            pass


if __name__ == '__main__':
    main()
