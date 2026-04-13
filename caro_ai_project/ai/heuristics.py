# Điểm số Heuristic 
ATK_SCORES = [0, 55, 150, 501, 99999, 99999, 99999]
DEF_SCORES = [0, 50, 100, 200, 50000, 50000, 50000]

def evaluate_position(board, x, y, player):
    opponent = 3 - player 
    score = 0
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    
    board.grid[x][y] = player
    
    for dx, dy in directions:
        score += evaluate_line(board, x, y, dx, dy, player, ATK_SCORES)
        score += evaluate_line(board, x, y, dx, dy, opponent, DEF_SCORES)
        
    board.grid[x][y] = 0 
    
    if score >= 50000:
        return score + 20000
        
    return score

def evaluate_line(board, x, y, dx, dy, target_player, score_map):
    consecutive = 1
    blocked_ends = 0
    
    for step in (1, -1):
        nx, ny = x + step*dx, y + step*dy
        while board.grid[nx][ny] == target_player:
            consecutive += 1
            nx += step*dx
            ny += step*dy
        if board.grid[nx][ny] != 0:
            blocked_ends += 1
            
    if consecutive >= 5: 
        return score_map[4]
    if blocked_ends == 2: 
        return 0 
    
    return score_map[consecutive] if blocked_ends == 0 else score_map[consecutive] // 2