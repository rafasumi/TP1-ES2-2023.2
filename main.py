from src.Pydle import Pydle


def main():
    Pydle().start_game_loop()


if __name__ == '__main__':
    try:
        main()
    except EOFError:
        pass
    except KeyboardInterrupt:
        pass
