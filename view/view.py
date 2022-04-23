from controller.game import Window


class View:

    def __init__(self):
        window = Window(800, 600, "The Horse Game")
        window.game_loop()
        window.game_exit()
