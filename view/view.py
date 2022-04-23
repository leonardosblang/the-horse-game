from controller.game import Window
#create a view class
class View:

    def __init__(self):
        window = Window(800, 600, "The Horse Game")
        window.game_loop()
        window.game_exit()

