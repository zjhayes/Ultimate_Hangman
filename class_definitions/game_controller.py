# Zachary Hayes
from class_definitions.ui_controller import UIController
import math

class GameController:
    '''GameController class controls the game logic.'''

    def __init__(self):
        self.available_choices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                                  'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.current_word = "word"
        self.guesses_made = 0
        self.max_guesses = 10
        self.score = 0

    def get_word(self):
        word_progress = []
        for character in self.current_word:
            if self.available_choices.__contains__(character.upper()):
                word_progress.append('_')
            else:
                word_progress.append(character.upper())
        return word_progress

    def make_guess(self, guess):
        print(guess)
        self.available_choices.remove(guess)
        if self.current_word.__contains__(guess.lower()):
            self.add_points(guess)
            print(self.score)
            return True
        else:
            self.guesses_made += 1
            return False

    def add_points(self, guess):
        vowels = ['A', 'E', 'I', 'O', 'U']
        default_score = 100
        self.score += default_score + (default_score * (len(self.current_word) / self.guesses_made))
        if vowels.__contains__(guess):
            self.score += 50
        self.score = math.ceil(self.score)

# Driver

game = GameController()
gui = UIController(game)
