# Tic-Tac-Toe – Minimax AI (Tkinter)

This project is an implementation of the Tic-Tac-Toe game with an AI opponent based on the Minimax algorithm.
The goal of the project is to demonstrate decision-making in an adversarial environment by evaluating possible game states and selecting optimal moves.
The graphical user interface is implemented in Python using the Tkinter library.

## How the Game Works

- The human player plays as "X"
- The AI opponent plays as "O"
- After the player makes a move, the AI calculates the best possible move using the Minimax algorithm and plays automatically

## Minimax Algorithm

The Minimax algorithm explores all possible game states to determine the optimal move.

Game state evaluation:
- AI win ("O") → +1
- Player win ("X") → -1
- Draw → 0

The AI always chooses the move that maximizes its outcome while assuming that the opponent plays optimally.

## Technologies Used

- Python 3
- Tkinter (GUI)

## Project Purpose

This project was created as part of the course *Introduction to Artificial Intelligence*.
It serves as a practical example of using the Minimax algorithm for building a predictive AI opponent in a simple game environment.

## Author

Marino Barnjak
