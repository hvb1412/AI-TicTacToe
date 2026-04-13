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