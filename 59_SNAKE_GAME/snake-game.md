# 🐍 Snake Game

A classic Snake Game built with Python's built-in `turtle` graphics library — no external dependencies required.

---

## 📋 Overview

Guide the snake to eat food, grow longer, and rack up points. The game ends (and resets) if the snake crashes into a wall or its own body. Your high score is tracked for the duration of the session.

---

## 🎮 Features

- **Smooth movement** with keyboard arrow key controls
- **Random food** — randomised shape (circle, square, triangle) and colour on each spawn
- **Growing snake** — a new orange body segment is added each time food is eaten
- **Score tracking** — live score and session high score displayed at the top of the window
- **Progressive difficulty** — the snake speeds up slightly with every food eaten
- **Collision detection** — handles wall collisions and self-collisions, resetting the game gracefully
- **Clean exit** — closing the window doesn't throw an error

---

## 🛠️ Requirements

- Python 3.x
- No external libraries needed — `turtle`, `random`, and `time` are all part of the Python standard library

---

## 🚀 Getting Started

1. **Clone or download** this repository.
2. **Run the game:**
   ```bash
   python snake_game.py
   ```
3. The game window (600×600, light blue background) will open immediately.

---

## 🕹️ Controls

| Key | Action |
|-----------|-------------|
| `↑` Up | Move up |
| `↓` Down | Move down |
| `←` Left | Move left |
| `→` Right | Move right |

> **Note:** The snake cannot reverse direction directly (e.g. if moving right, pressing left is ignored).

---

## ⚙️ How It Works

### Game Loop

The main `while` loop continuously updates the screen, checks for collisions, moves the snake body, and controls game speed via `time.sleep(d)`.

### Snake Movement

The head moves 20 pixels per tick in the current direction. Body segments follow by cascading positions from front to back each frame.

### Collision Logic

| Collision Type | Trigger | Result |
|---|---|---|
| **Wall** | Head `x` or `y` coordinate exceeds ±290 | Reset position, clear body, reset score |
| **Food** | Head within 20px of food | Relocate food, add body segment, increase score, speed up |
| **Self** | Any body segment within 20px of head | Reset position, clear body, reset score |

### Scoring

- **+10 points** per food eaten

- High score persists for the entire session (resets when the script is closed)
- Speed increases by `0.001s` per food eaten (starting at `0.1s` delay)

---

## 🔧 Customisation

| Variable | Location | What it controls |
|----------|----------|-----------------|
| `d = 0.1` | Top of file | Initial snake speed (lower = faster) |
| `sc.bgcolor(...)` | Window setup | Background colour |
| `h.color(...)` | Snake head setup | Head colour |
| `new_seg.color(...)` | Food collision block | Body segment colour |
| `600, 600` | `sc.setup(...)` | Window dimensions |

---
