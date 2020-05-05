# Zachary Hayes
from class_definitions.ui_controller import UIController
import math
from class_definitions.dictionary import Dictionary


class GameController:
    '''GameController class controls the game logic.'''

    def __init__(self):
        self.available_choices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                                  'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.dictionary = Dictionary()
        self.current_word = self.dictionary.get_random_word()
        self.wrong_guesses = 0
        self.correct_guesses = 0
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

    def get_score(self):
        return str(self.score)

    def make_guess(self, guess):
        '''Processes a guess, returns True if game is won/lost'''
        self.available_choices.remove(guess)
        if self.current_word.__contains__(guess.lower()):
            self.add_points(guess)
            self.correct_guesses += 1
            if self.correct_guesses == self.get_num_unique_char():
                return 1     # Game is won.
            else:
                return 0    # Game continues.
        else:
            self.wrong_guesses += 1
            if self.wrong_guesses >= self.max_guesses:
                return -1    # Game is lost.
            else:
                return 0     # Game continues.

    def reset_game(self):
        '''Resets game values to start new game.'''
        self.available_choices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                                  'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.current_word = self.dictionary.get_random_word()
        self.wrong_guesses = 0
        self.correct_guesses = 0
        self.score = 0

    def add_points(self, guess):
        '''Adds points based on guess. More points the harder the word, and fewer guesses made.
            Vowels get more points if correct guesses have already been made.'''
        vowels = ['A', 'E', 'I', 'O', 'U']
        default_score = 100
        self.score += default_score + default_score * max(0, (len(self.current_word) - self.wrong_guesses))
        if vowels.__contains__(guess):
            self.score += 50 * self.correct_guesses
        self.score = math.ceil(self.score)

    def get_num_unique_char(self):
        '''Returns number of unique characters in current word.'''
        unique_characters = set(self.current_word)
        return len(unique_characters)
