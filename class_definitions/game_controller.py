# Zachary Hayes
from class_definitions.ui_controller import UIController


class GameController:
    '''GameController class controls the game logic.'''

    def __init__(self):
        self.available_choices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                                  'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.current_word = "word"
        self.guesses_made = 0

    def get_word(self):
        return self.current_word

    def make_guess(self, guess):
        print(guess)
        self.available_choices.remove(guess)
        if self.current_word.__contains__(guess.lower()):
            print("True")
        else:
            self.guesses_made += 1


# Driver

game = GameController()
gui = UIController(game)
