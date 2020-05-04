# Zachary Hayes
from class_definitions.ui_controller import UIController


class GameController:
    '''GameController class controls the game logic.'''

    def __init__(self):
        pass

    def get_word(self):
        return "word"


# Driver

game = GameController()
gui = UIController(game)
