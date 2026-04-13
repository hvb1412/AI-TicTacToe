# Caro AI (Gomoku) - Python Edition

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

## 📌 Overview
**Caro AI** is a Python-based implementation of the classic Gomoku (Extended Tic-Tac-Toe) board game played on a 20x20 grid. The core of this project features a highly optimized Artificial Intelligence (AI) opponent capable of dynamic threat analysis, offensive/defensive heuristic scoring, and deep move calculation using the **Minimax algorithm with Alpha-Beta Pruning**.

Originally written in Java, this project has been fully refactored into a clean, modern, and object-oriented Python architecture, complete with an automated CI/CD pipeline.

## ✨ Key Features
* **Smart AI Opponent:** Utilizes Minimax with Alpha-Beta pruning, enriched with complex heuristic evaluation (detecting open-threes, blocked-fours, and continuous attack patterns).
* **Opening Books:** Built-in early game strategies for the AI to ensure varied and robust openings.
* **Modern Architecture:** Clean MVC (Model-View-Controller) separation.
* **Undo Functionality:** Players can easily revert their last moves.
* **Interactive GUI:** Built with Python's native `Tkinter` library for a lightweight and responsive experience.
* **Automated CI/CD Pipeline:** Integrated GitHub Actions for automated unit testing (`pytest`), code linting (`flake8`), and automatic `.exe` generation for Windows.

## 🛠 Technologies Used
* **Language:** Python 3.10+
* **GUI Framework:** Tkinter
* **Testing & Linting:** `pytest`, `flake8`
* **DevOps:** GitHub Actions, PyInstaller

## 📂 Directory Structure

The project follows a modular, highly maintainable structure:

```text
caro_ai_project/
│
├── .github/workflows/          # GitHub Actions CI/CD configuration
│   └── main.yml
├── ai/                         # AI Engine Module
│   ├── __init__.py
│   ├── bot.py                  # Core decision-making (Minimax)
│   ├── heuristics.py           # Position evaluation & scoring logic
│   └── patterns.py             # Opening books & attack patterns
├── core/                       # Core Game Logic Module
│   ├── __init__.py
│   ├── models.py               # Point and Board classes
│   └── rules.py                # Vector-based win-condition checking
├── gui/                        # Graphical User Interface Module
│   ├── __init__.py
│   └── app.py                  # Tkinter application rendering
├── tests/                      # Automated Unit Tests
│   ├── __init__.py
│   └── test_rules.py
├── main.py                     # Application entry point
└── requirements.txt            # Python dependencies
````

## 🚀 Installation & Running Locally

### Prerequisites

Make sure you have **Python 3.10 or higher** installed on your system.

### Steps

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/hvb1412/AI-TicTacToe.git](https://github.com/hvb1412/AI-TicTacToe.git)
    cd caro_ai_project
    ```

2.  **Install dependencies:**
    *(Optional but recommended: Create a virtual environment first)*

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the game:**

    ```bash
    python main.py
    ```

## 🎮 How to Play

1.  The game is played on a 20x20 grid.
2.  You play as **X** (Red) and the AI plays as **O** (Blue).
3.  The objective is to be the first player to get an unbroken row of **five pieces** horizontally, vertically, or diagonally.
4.  Use the **"New Game"** button to restart the match (this will also alternate the starting player between you and the AI).
5.  Use the **"Undo"** button if you make a mistake.

## 📦 Automated Builds (CI/CD)

This project uses GitHub Actions to automatically build standalone executable files for Windows users.
If you do not want to install Python, simply go to the **[Actions tab](https://www.google.com/search?q=../../actions)** of this repository, select the latest successful build, and download the `CaroAI-Windows-Executable` artifact to play immediately\!

## 🔮 Future Improvements

While the AI is currently very strong, future updates may include:

  * **Transposition Tables (Zobrist Hashing):** To cache previously evaluated board states and significantly speed up the Minimax search depth.
  * **Difficulty Levels:** Allowing players to adjust the AI's search depth (e.g., Easy, Medium, Hard).
  * **Multiplayer Mode:** Adding socket programming for local LAN or online PvP matches.
  * **UI Upgrade:** Migrating from Tkinter to PyGame or PyQt for smoother animations and custom graphic assets.

-----

*Developed with ❤️ by HoangVanBinh - FullStack Engineering at Sun Asterisk. Feel free to fork, open issues, or submit PRs\!*
