import threading

from playsound import playsound

class Soundtrack:
    def _background_music_loop(self):
        while True:
            playsound('assets/sound/here_comes_the_sun.ogg', block=True)

    def start(self):
        music_thread = threading.Thread(
        target=self._background_music_loop, daemon=True, name='backgroundMusic')
        music_thread.start()
