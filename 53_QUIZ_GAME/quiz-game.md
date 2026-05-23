# 🎮 Ultimate Quiz Challenge

A fun, interactive command-line quiz game built in Python that tests your knowledge across multiple categories with multiple-choice questions.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [How to Play](#how-to-play)
- [Quiz Categories](#quiz-categories)
- [Scoring System](#scoring-system)
- [Code Overview](#code-overview)

---

## Overview

The Ultimate Quiz Challenge is a terminal-based Python quiz application that presents players with multiple-choice questions across four knowledge categories. Players earn points for correct answers and receive a performance rating at the end of each round, with the option to play again.

---

## Features

- **4 distinct quiz categories** — General Knowledge, Movies & TV Shows, Science & Nature, and Video Games
- **Random Mix mode** — draws questions from all categories at once
- **Randomized question order** — questions are shuffled each round for replayability
- **Instant feedback** — tells you whether your answer was correct or wrong after each question
- **Score tracking** — accumulates your total score across multiple rounds
- **Performance rating** — gives you a custom message based on your final percentage
- **Input validation** — gracefully handles invalid inputs without crashing

---

## How to Play

1. **Launch** the game — a welcome screen and instructions are displayed.
2. **Select a category** by entering a number from 1 to 5.
3. **Answer each question** by typing `A`, `B`, `C`, or `D` and pressing Enter.
4. **View your results** — your score, correct answers, and a performance rating appear after the last question.
5. **Play again** — type `yes` to start a new round or `no` to exit.

---

## Quiz Categories

| # | Category | Questions |
|---|----------|-----------|
| 1 | General Knowledge | 5 |
| 2 | Movies and TV Shows | 5 |
| 3 | Science and Nature | 5 |
| 4 | Video Games | 5 |
| 5 | Random Mix (all categories) | 20 |

---

## Scoring System

| Result | Points |
|--------|--------|
| Correct answer | +10 points |
| Wrong answer | +0 points |

**Performance ratings** based on your end-of-round percentage:

| Score % | Rating |
|---------|--------|
| 100% | 🏆 PERFECT SCORE! You're a quiz master! |
| 80% – 99% | ⭐ EXCELLENT! You really know your stuff! |
| 60% – 79% | 👍 GOOD JOB! You've got decent knowledge! |
| 40% – 59% | 🙂 NOT BAD! There's room for improvement. |
| 0% – 39% | 📚 KEEP LEARNING! Practice makes perfect! |

---

## Code Overview

| Function | Description |
|----------|-------------|
| `display_welcome()` | Prints the welcome banner and game instructions |
| `display_categories()` | Lists the available quiz categories |
| `get_user_choice()` | Prompts for and validates the user's category selection (1–5) |
| `load_questions()` | Returns a dictionary containing all question banks by category |
| `run_quiz(category_data)` | Runs a full quiz round — shuffles questions, handles answers, and displays results |
| `main()` | Entry point — controls the game loop and play-again logic |

---
