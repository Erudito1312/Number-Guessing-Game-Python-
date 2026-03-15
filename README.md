# Number Guessing Game (Python)

A simple command-line number guessing game written in Python. The game generates a random number between **1 and 100**, and the player must guess it. After each guess the program tells the player whether the correct number is **higher** or **lower**.

The game also tracks your **personal best score** (lowest number of tries) and saves it in a file so it persists between program runs.

## Features

- Random number generation
- Input validation (only numbers allowed)
- Replay system
- Persistent **high score tracking**
- Automatic creation of score file on first run
- Protection against corrupted or invalid score files

## How the Game Works

1. The program loads the current record from 'Score.txt'.
2. A random number between **1 and 100** is generated.
3. The player keeps guessing until the correct number is found.
4. The program tells the player:
   - **Higher** if the guess is too low
   - **Lower** if the guess is too high
5. The number of tries is counted.
6. If the player beats the current record, the new score is saved.

## How to Run

Run the game from the terminal:

```bash
python game.py
```
