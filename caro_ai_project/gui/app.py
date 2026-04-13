import tkinter as tk
from tkinter import messagebox
from core.models import Board
from core.rules import check_win
from ai.bot import AIBot

class CaroGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Caro AI - Python Edition")
        self.board = Board(size=20)
        self.ai_bot = AIBot(ai_player=2)
        self.buttons = [[None for _ in range(22)] for _ in range(22)]
        
        self.setup_ui()

    def setup_ui(self):
        top_frame = tk.Frame(self.root)
        top_frame.pack(side=tk.TOP, pady=10)
        
        self.lbl_status = tk.Label(top_frame, text="Lượt của X", font=('Arial', 14, 'bold'))
        self.lbl_status.pack(side=tk.LEFT, padx=20)
        
        tk.Button(top_frame, text="New Game", command=self.new_game).pack(side=tk.LEFT, padx=5)
        tk.Button(top_frame, text="Undo", command=self.undo_move).pack(side=tk.LEFT, padx=5)

        grid_frame = tk.Frame(self.root)
        grid_frame.pack(side=tk.TOP)
        
        for i in range(1, 21):
            for j in range(1, 21):
                btn = tk.Button(grid_frame, width=3, height=1, font=('Arial', 12, 'bold'),
                                command=lambda x=i, y=j: self.handle_click(x, y))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn

    def handle_click(self, x, y):
        if self.board.place_piece(x, y, 1):
            self.buttons[x][y].config(text="X", fg="red")
            if check_win(self.board, x, y, 1):
                messagebox.showinfo("Kết quả", "Bạn đã chiến thắng!")
                self.disable_board()
                return
            
            self.lbl_status.config(text="Lượt của O (AI đang nghĩ...)")
            self.root.update()
            
            self.machine_turn()

    def machine_turn(self):
        mx, my = self.ai_bot.get_best_move(self.board)
        self.board.place_piece(mx, my, 2)
        self.buttons[mx][my].config(text="O", fg="blue")
        
        if check_win(self.board, mx, my, 2):
            messagebox.showinfo("Kết quả", "AI đã chiến thắng!")
            self.disable_board()
            return
            
        self.lbl_status.config(text="Lượt của X")

    def undo_move(self):
        last_o = self.board.undo()
        if last_o: self.buttons[last_o[0]][last_o[1]].config(text="")
        
        last_x = self.board.undo()
        if last_x: self.buttons[last_x[0]][last_x[1]].config(text="")
        
        self.lbl_status.config(text="Lượt của X")

    def disable_board(self):
        for i in range(1, 21):
            for j in range(1, 21):
                self.buttons[i][j].config(state=tk.DISABLED)

    def new_game(self):
        self.board = Board(size=20)
        for i in range(1, 21):
            for j in range(1, 21):
                self.buttons[i][j].config(text="", state=tk.NORMAL)
        self.lbl_status.config(text="Lượt của X")