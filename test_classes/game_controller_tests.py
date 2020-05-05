import unittest
from class_definitions import game_controller as g


class GameControllerTests(unittest.TestCase):

    def setUp(self):
        self.game = g.GameController()
        self.current_word = "test"

    def tearDown(self):
        del self.game

    def test_get_score_returns_string(self):
        self.game.score = 1;
        self.assertEqual("1", self.game.get_score())

    def test_reset_game(self):
        self.game.available_choices = ['A', 'B', 'C']
        self.game.current_word = "123"
        self.game.wrong_guesses = 100
        self.game.correct_guesses = 100
        self.game.score = 100
        self.game.reset_game()
        actual_choices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                          'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.assertEqual(actual_choices, self.game.available_choices)
        self.assertEqual(0, self.game.wrong_guesses)
        self.assertEqual(0, self.game.correct_guesses)
        self.assertEqual(0, self.game.score)
        self.assertNotEqual("123", self.game.current_word)

    def test_add_points(self):
        self.game.score = 0
        self.game.wrong_guesses = 0
        self.game.correct_guesses = 1
        self.game.current_word = "test"
        self.game.add_points('E')
        self.assertEqual(550, self.game.score)
        self.game.add_points('T')
        self.assertEqual(1050, self.game.score)

    def test_get_num_unique_char(self):
        self.game.current_word = "hippo"
        self.assertEqual(4, self.game.get_num_unique_char())

    def test_make_guess(self):
        self.game.available_choices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                                       'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.game.current_word = "test"
        self.game.score = 0
        self.game.correct_guesses = 0
        self.game.wrong_guesses = 0
        self.assertEqual(0, self.game.make_guess('T'))
        self.assertEqual(0, self.game.make_guess('E'))
        self.assertEqual(1, self.game.make_guess('S'))


if __name__ == '__main__':
    unittest.main()
