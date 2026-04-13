def check_win(board, x, y, player):
    # 4 hướng: Ngang, Dọc, Chéo chính, Chéo phụ
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    
    for dx, dy in directions:
        count = 1
        # Đếm về phía trước
        nx, ny = x + dx, y + dy
        while 1 <= nx <= board.size and 1 <= ny <= board.size and board.grid[nx][ny] == player:
            count += 1
            nx += dx
            ny += dy
            
        # Đếm về phía sau
        nx, ny = x - dx, y - dy
        while 1 <= nx <= board.size and 1 <= ny <= board.size and board.grid[nx][ny] == player:
            count += 1
            nx -= dx
            ny -= dy
            
        if count >= 5:
            return True
    return False