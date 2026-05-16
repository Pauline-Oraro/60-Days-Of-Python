# 🧠 Memory Sequence Game

A terminal-based memory training game written in Python. Players watch a growing sequence of numbers appear one by one and must recall them in exact order. Each successful round adds another number to the sequence, progressively testing the player's short-term memory.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [Gameplay](#gameplay)
- [Code Structure](#code-structure)
- [Function Reference](#function-reference)
- [Game Logic Walkthrough](#game-logic-walkthrough)
- [Error Handling](#error-handling)

---

## Overview

| Property        | Details                        |
|----------------|-------------------------------|
| Language        | Python 3                       |
| Type            | Terminal / CLI Game            |
| Difficulty      | Progressively increases        |
| Input Method    | Keyboard (space-separated numbers) |
| Dependencies    | Standard library only          |

---

## Features

- Progressively growing number sequences (starts at 1, grows by 1 each round)
- Numbers are revealed one at a time with timed delays for a clean reveal effect
- Cross-platform screen clearing (works on Windows, macOS, and Linux)
- Input validation with clear error messaging
- Play-again prompt after each game session
- Tracks the round number and sequence length throughout the session

---

## Requirements

- Python 3.6 or higher
- No third-party packages — uses only the Python standard library:
  - `random` — generates random integers for the sequence
  - `time` — controls display timing between number reveals
  - `os` — handles cross-platform terminal clearing

---

## How to Run

1. Save the script as `memory_game.py`.
2. Open a terminal in the file's directory.
3. Run the script:

```bash
python memory_game.py
```

> On some systems you may need to use `python3` instead of `python`.

---

## Gameplay

### Starting the Game

When launched, the game displays a welcome screen and the rules, then waits for the player to press **Enter** to begin.

```
MEMORY SEQUENCE GAME
Remember the sequence and type it back!
Rules
- Watch as numbers appear one by one
- After the sequence is shown, type it back in order
- Each round adds one more number to remember
- How far can you go? 🏆

Press Enter to start...
```

### Each Round

1. A new random number (1–9) is appended to the sequence.
2. The screen clears, and the round number is announced.
3. Each number in the sequence flashes on screen one at a time, with a brief pause before and after each reveal.
4. After all numbers have been shown, the player is prompted to type the full sequence back, separating each number with a space.

**Example — Round 3:**
```
Round 3
Remember this sequence of 3 numbers:

4
(screen clears)
7
(screen clears)
2
(screen clears)

Now repeat the sequence by typing each number, separated by spaces:
> 4 7 2
Correct!, You remembered all 3 numbers!
```

### Losing

If the player enters the wrong sequence, the game ends and reveals the correct answer:

```
Game Over! You remembered all 2 numbers
The correct sequence was: 4 7 2
```

### Play Again

After any game-ending event (wrong answer or invalid input), the player is prompted:

```
Play again? (yes/no):
```

Entering `y` or `yes` (case-insensitive) resets the game. Any other input exits gracefully.

---

## Code Structure

```
memory_game.py
│
├── Imports
│   ├── random
│   ├── time
│   └── os
│
├── clear_screen()          # Helper function — clears terminal output
│
├── Welcome Screen          # Prints title, rules, and waits for Enter
│
└── Game Loop (while not game_over)
    ├── Append new random number to sequence
    ├── Display sequence numbers one by one (timed)
    ├── Collect player input
    ├── Validate and compare input to sequence
    ├── Update round count or set game_over
    └── Prompt for play-again on game end
```

---

## Function Reference

### `clear_screen()`

```python
def clear_screen():
    "Clear the terminal screen."
    os.system("cls" if os.name == "nt" else "clear")
```

| Property    | Details                                              |
|-------------|------------------------------------------------------|
| Parameters  | None                                                 |
| Returns     | None                                                 |
| Side Effect | Clears all text currently visible in the terminal    |
| Platform    | `cls` on Windows (`os.name == "nt"`), `clear` on Unix/macOS |

Called before revealing each round's sequence and between each individual number reveal to create an animated flash effect.

---

## Game Logic Walkthrough

### Initialization

```python
sequence = []       # Holds the current number sequence for this session
current_round = 1   # Tracks which round the player is on
game_over = False   # Controls the main game loop
```

### Round Start — Sequence Growth

```python
sequence.append(random.randint(1, 9))
```

Each round, a new random integer between **1 and 9 (inclusive)** is added to the end of the sequence. The sequence persists and grows throughout the session.

### Number Reveal — Timed Display

```python
for number in sequence:
    time.sleep(0.7)   # Pause before showing the number
    print(f"{number}")
    time.sleep(0.7)   # Pause after showing the number
    clear_screen()    # Clear for next number
```

Each digit is shown for 0.7 seconds, then the screen is cleared. This creates a one-at-a-time flash effect that prevents the player from seeing multiple numbers simultaneously.

### Input Collection & Parsing

```python
player_answer = input(">")
player_sequence = [int(num) for num in player_answer.split()]
```

The player types all numbers separated by spaces (e.g., `3 7 1 5`). The input is split on whitespace and each token is cast to an integer. If any token is not a valid integer, a `ValueError` is caught.

### Sequence Comparison

```python
if player_sequence == sequence:
    # Correct: increment round, continue
else:
    # Wrong: reveal answer, end game
```

Python's list equality check (`==`) compares both the values and the order of elements, so the player must recall the sequence in the exact correct order.

### Play-Again Logic

```python
play_again = input("Play again? (yes/no): ").lower()
if play_again.startswith("y"):
    sequence = []
    current_round = 1
    game_over = False
```

Resetting sets `game_over = False`, which allows the `while` loop to continue. The sequence and round counter are both fully reset, starting a fresh game.

---

## Error Handling

| Scenario | Handling |
|---|---|
| Player enters letters or symbols | `ValueError` is caught; game ends with "Please enter numbers only" message |
| Player enters nothing (empty input) | `split()` returns an empty list; comparison fails and game ends normally |

---

## Example Session

```
MEMORY SEQUENCE GAME
Remember the sequence and type it back!
...
Press Enter to start...

Round 1
Remember this sequence of 1 numbers:
3

Now repeat the sequence by typing each number, separated by spaces:
> 3
Correct!, You remembered all 1 numbers!

Round 2
Remember this sequence of 2 numbers:
3
8

Now repeat the sequence by typing each number, separated by spaces:
> 3 5
Game Over! You remembered all 1 numbers
The correct sequence was: 38

Play again? (yes/no): no
Thanks for playing! Goodbye!
```

---
