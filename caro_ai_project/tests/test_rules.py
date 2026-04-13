# tests/test_rules.py
from core.models import Board
from core.rules import check_win

def test_check_win_horizontal():
    board = Board(size=20)
    # Giả lập X (1) đánh 5 quân ngang
    for j in range(1, 6):
        board.place_piece(5, j, 1)
    
    # Kiểm tra tại vị trí quân cuối cùng
    assert check_win(board, 5, 5, 1) == True
    assert check_win(board, 5, 5, 2) == False # O không thắng