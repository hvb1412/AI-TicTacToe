from core.models import Board
from core.rules import check_win

def test_check_win_horizontal():
    board = Board(size=20)
    for j in range(1, 6):
        board.place_piece(5, j, 1)
    
    assert check_win(board, 5, 5, 1) == True
    assert check_win(board, 5, 5, 2) == False

def test_check_win_vertical():
    board = Board(size=20)
    for i in range(1, 6):
        board.place_piece(i, 5, 2)
    
    assert check_win(board, 5, 5, 2) == True