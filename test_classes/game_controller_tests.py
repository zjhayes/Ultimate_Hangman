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
        self.assertEqual(self.game.get_score(), "1")

    def test_get_score_returns_string(self):
        self.game.score = 1;
        self.assertEqual(self.game.get_score(), "1")

    def test_reset_game(self):
        self.game.available_choices = ['A', 'B', 'C']
        self.game.current_word = "123"
        self.game.wrong_guesses = 100
        self.game.correct_guesses = 100
        self.game.score = 100
        self.game.reset_game()
        actual_choices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                          'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.assertEqual(self.game.wrong_guesses, 0)
        self.assertEqual(self.game.correct_guesses, 0)
        self.assertEqual(self.game.score, 0)


if __name__ == '__main__':
    unittest.main()
