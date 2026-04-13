from .heuristics import evaluate_position
from core.models import Point

class AIBot:
    def __init__(self, ai_player=2):
        self.ai = ai_player
        self.human = 3 - ai_player

    def get_candidates(self, board, distance=2):
        candidates = []
        visited = set()
        for i in range(1, board.size + 1):
            for j in range(1, board.size + 1):
                if board.grid[i][j] in (1, 2):
                    for dx in range(-distance, distance + 1):
                        for dy in range(-distance, distance + 1):
                            nx, ny = i + dx, j + dy
                            if 1 <= nx <= board.size and 1 <= ny <= board.size:
                                if board.grid[nx][ny] == 0 and (nx, ny) not in visited:
                                    candidates.append(Point(nx, ny))
                                    visited.add((nx, ny))
        return candidates

    def get_best_move(self, board):
        if board.turn_count <= 1:
            return 10, 10

        candidates = self.get_candidates(board, distance=2 if board.turn_count > 2 else 1)
        
        max_score = -1
        best_points = []
        for p in candidates:
            p.score = evaluate_position(board, p.x, p.y, self.ai)
            max_score = max(max_score, p.score)
            
        for p in candidates:
            if p.score >= max_score * 0.85:
                best_points.append(p)

        if best_points:
            best_points.sort(key=lambda p: p.score, reverse=True)
            return best_points[0].x, best_points[0].y
            
        return candidates[0].x, candidates[0].y