from hand_battle.board import Board
from hand_battle.card import Card


def test_board_initialization():
    board = Board('2h3h4h5h6h')
    assert [Card(str(i) + 'h') for i in range(2, 7)] == board.cards