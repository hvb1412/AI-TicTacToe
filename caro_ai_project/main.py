import tkinter as tk
from gui.app import CaroGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = CaroGUI(root)
    # Kích thước cửa sổ vừa đủ cho bàn cờ 20x20
    root.geometry("800x850") 
    root.mainloop()