class Point:
    def __init__(self, x, y, score=0.0, rank=0):
        self.x = x
        self.y = y
        self.score = score
        self.rank = rank

class Board:
    def __init__(self, size=20):
        self.size = size
        # Khởi tạo ma trận 22x22, viền ngoài là -1, bên trong là 0
        self.grid = [[-1 if i == 0 or i == size+1 or j == 0 or j == size+1 else 0 
                      for j in range(size + 2)] for i in range(size + 2)]
        self.turn_count = 0
        self.history = [] # Dùng cho chức năng Undo

    def place_piece(self, x, y, player):
        if self.grid[x][y] == 0:
            self.grid[x][y] = player
            self.history.append((x, y))
            self.turn_count += 1
            return True
        return False

    def undo(self):
        if self.history:
            x, y = self.history.pop()
            self.grid[x][y] = 0
            self.turn_count -= 1
            return x, y
        return None