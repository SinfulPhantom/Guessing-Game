from mock import MagicMock, patch
from guessing_game import Game

GAME = Game(1, 20, 5)


@patch('guessing_game.sleep', return_value=None)
@patch('guessing_game.input')
def test_welcome_sequence(mock_input, mock_sleep):
    mock_input.return_value = 'Jeff'
    GAME.begin_guessing = MagicMock()
    GAME.welcome_sequence()
    assert GAME.name == 'Jeff'


@patch('guessing_game.input')
def test_grab_guess(mock_input):
    mock_input.return_value = 5
    GAME.grab_guess()
    assert GAME.guess == 5
