# Rock Paper Scissors — Python Game Documentation

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen)
![Type](https://img.shields.io/badge/Type-CLI%20Game-orange)

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Gameplay](#gameplay)
5. [Code Structure](#code-structure)
6. [Function Reference](#function-reference)
7. [Game Logic](#game-logic)
8. [Example Session](#example-session)

---

## Overview

This is a command-line implementation of the classic **Rock Paper Scissors** game written in Python. The player competes against the computer in a best-of-five series (first to 3 wins). The computer's choice is randomly generated, and results are displayed with a short animated delay to simulate suspense.

---

## Features

- Interactive CLI interface with emoji-enhanced prompts
- Randomised computer opponent
- Animated "thinking" delay for the computer's move
- Round-by-round score tracking
- Best-of-5 format (first to 3 wins takes the match)
- Input validation with helpful error messages
- Play-again prompt with recursive replay support

---

## Requirements

| Requirement | Detail |
|-------------|--------|
| Python version | 3.6 or higher |
| External libraries | None — uses only the standard library |
| Modules used | `random`, `time` |

---

## Gameplay

### Objective

Be the first player to win **3 rounds** against the computer.

### Game Rules

| Winner | Scenario |
|--------|----------|
| Rock 🪨 | Crushes Scissors ✂️ |
| Scissors ✂️ | Cuts Paper 📄 |
| Paper 📄 | Covers Rock 🪨 |

### Round Flow

1. The current round number and score are displayed.
2. The player selects Rock, Paper, or Scissors by entering `1`, `2`, or `3`.
3. The computer randomly picks its move (shown with a brief animated pause).
4. The round result is announced: **Win**, **Lose**, or **Tie**.
5. Scores update; play continues until one side reaches 3 wins.

### End of Game

After the match ends, the final score is shown and the player is prompted to play again.

---

## Code Structure

```
rock_paper_scissors.py
│
├── display_welcome()          # Prints title screen and rules
├── get_user_choice()          # Handles and validates player input
├── get_computer_choice()      # Generates a random computer move
├── convert_choice_to_text()   # Maps integer choice to display string
├── determine_winner()         # Computes round outcome
├── display_round_result()     # Prints the result with animation
├── play_game()                # Main game loop and score management
│
└── play_game()                # Entry point — called at bottom of script
```

---

## Function Reference

### `display_welcome()`

Prints the game title, emoji banner, and rules to the console.

- **Parameters:** None
- **Returns:** None
- **Side effects:** Console output only

---

### `get_user_choice() → int`

Displays a numbered menu and reads the player's move. Loops until a valid integer between 1 and 3 is entered.

- **Parameters:** None
- **Returns:** `int` — `1` (Rock), `2` (Paper), or `3` (Scissors)
- **Handles:** `ValueError` for non-numeric input; range check for out-of-bound integers

---

### `get_computer_choice() → int`

Generates the computer's move using `random.randint`.

- **Parameters:** None
- **Returns:** `int` — a random value in `{1, 2, 3}`

---

### `convert_choice_to_text(choice: int) → str`

Converts a numeric choice into a human-readable label with emoji.

- **Parameters:** `choice` — integer (`1`, `2`, or `3`)
- **Returns:** `str` — e.g., `"Rock 🪨"`, `"Paper 📄"`, `"Scissors ✂️"`

```python
options = {1: "Rock 🪨", 2: "Paper 📄", 3: "Scissors ✂️"}
```

---

### `determine_winner(user_choice: int, computer_choice: int) → str`

Evaluates both choices and returns the round outcome.

- **Parameters:**
  - `user_choice` — player's integer choice
  - `computer_choice` — computer's integer choice
- **Returns:** `str` — one of `"tie"`, `"user"`, or `"computer"`

**Win conditions checked:**

| User | Computer | Result |
|------|----------|--------|
| Rock (1) | Scissors (3) | `"user"` |
| Scissors (3) | Paper (2) | `"user"` |
| Paper (2) | Rock (1) | `"user"` |
| Any equal pair | — | `"tie"` |
| All other combinations | — | `"computer"` |

---

### `display_round_result(user_choice, computer_choice, result)`

Displays both players' choices and the round outcome. Includes a 1.5-second animated delay (3 dots × 0.5 s) before revealing the computer's pick.

- **Parameters:**
  - `user_choice` — player's integer choice
  - `computer_choice` — computer's integer choice
  - `result` — outcome string (`"tie"`, `"user"`, or `"computer"`)
- **Returns:** None
- **Side effects:** Console output + blocking `time.sleep()` calls

---

### `play_game()`

The main game controller. Manages the round loop, score tracking, and the play-again prompt. Calls itself recursively if the player chooses to replay.

- **Parameters:** None
- **Returns:** None
- **Loop condition:** Continues while both `user_score` and `computer_score` are below `target_score` (3)
- **Play-again:** Calls `play_game()` recursively on `"y"` input

---

## Game Logic

### Win Detection (Truth Table)

```
User \ Computer  | Rock | Paper | Scissors
-----------------+------+-------+---------
Rock             | Tie  | Loss  | Win
Paper            | Win  | Tie   | Loss
Scissors         | Loss | Win   | Tie
```

### Score Tracking

```python
user_score    = 0  # incremented on "user" result
computer_score = 0  # incremented on "computer" result
target_score  = 3  # first to reach this wins the match
```

Ties do **not** affect either score and do **not** advance the round counter.

> ⚠️ **Note:** The round counter (`round_num`) currently increments on every iteration including ties, which means the displayed round number can exceed the number of scored rounds in tie-heavy games.

---

## Example Session

```
==== ROCK PAPER SCISSORS ====
🪨  📄  ✂️

Rules:
- Rock crushes Scissors
- Scissors cuts Paper
- Paper covers Rock
- First to win 3 rounds is the champion!

----------------------------

=== Round 1 ===
Score: You 0 - 0 Computer

Make your choice:
1. Rock 🪨
2. Paper 📄
3. Scissors ✂️
Enter your choice (1-3): 1

You chose: Rock 🪨
Computer is choosing...
Computer chose: Scissors ✂️
You win this round! 🎉

=== Round 2 ===
Score: You 1 - 0 Computer
...

==== GAME OVER ====
Final Score: You 3 - 1 Computer
Congrats! You are the champion 🏆

Do you want to play again? (y/n):
```

---
