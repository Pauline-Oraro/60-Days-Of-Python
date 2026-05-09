# 🪙 Coin Flip Game — Mini Project

A fun command-line Python game where the user guesses the outcome of a coin flip. The game validates input, simulates the flip using randomness, and keeps playing until the user decides to stop.

---

## 📋 Project Overview

| Detail | Info |
|--------|------|
| **Project Type** | Mini Project — Command Line Game |
| **Difficulty** | Beginner |
| **Concepts Used** | `import random`, `input()`, `print()`, `while` loop, `break`, `continue`, `random.choice()`, `.lower()`, `.startswith()`, f-strings, input validation |

---

## 💻 Full Code

```python
import random

print("COIN FLIP GAME")
print("Guess heads or tails")

while True:
    guess = input("\nEnter your guess (heads/tails): ").lower()

    if guess != "heads" and guess != "tails":
        print("Please enter 'heads' or 'tails'")
        continue

    flip = random.choice(["heads", "tails"])

    print(f"\nCoin shows {flip}")

    if guess == flip:
        print("You won, you guessed correctly")
    else:
        print("Sorry, wrong guess, try again")

    again = input("\nPlay again? (yes/no): ").lower()
    if not again.startswith("y"):
        print("Goodbye")
        break
```

---

## 🔍 Step-by-Step Explanation

### Step 1 — Import the `random` Module

```python
import random
```

- The `random` module is a Python **built-in** — no installation needed
- Imported at the top of the file before any code that uses it
- Used for `random.choice()` which simulates the coin flip

> **Important:** Always place `import` statements at the **very top** of your file. Python reads top to bottom — calling `random.choice()` before the import raises a `NameError`.

---

### Step 2 — Display the App Title and Instructions

```python
print("COIN FLIP GAME")
print("Guess heads or tails")
```

- Two `print()` calls set up the title and brief instructions
- This gives the user context before the game begins
- Splitting the title and instructions across two lines keeps it clean and readable

---

### Step 3 — Start an Infinite Loop

```python
while True:
```

- Creates an **infinite loop** that keeps the game running
- The game repeats until the user explicitly chooses to stop
- The loop has **two exit points** — `break` when the user says no to playing again, and `continue` to restart the loop on invalid input

> **Important:** This loop uses both `break` and `continue` — two different loop control tools that serve opposite purposes. `continue` restarts the current iteration (skips invalid input), while `break` exits the loop entirely (ends the game).

---

### Step 4 — Get and Normalize the Guess

```python
guess = input("\nEnter your guess (heads/tails): ").lower()
```

- `input()` waits for the user to type their guess
- `.lower()` is chained **directly** onto `input()` — the result is immediately converted to lowercase before being stored in `guess`
- This means `"Heads"`, `"HEADS"`, and `"heads"` are all treated identically

> **Important:** Chaining `.lower()` directly onto `input()` is a clean, Pythonic pattern. Instead of writing two lines:
> ```python
> guess = input("Enter your guess: ")
> guess = guess.lower()
> ```
> It can be done in one:
> ```python
> guess = input("Enter your guess: ").lower()
> ```
> Both work, but the chained version is more concise.

---

### Step 5 — Validate the Input

```python
if guess != "heads" and guess != "tails":
    print("Please enter 'heads' or 'tails'")
    continue
```

- Checks that the user entered **only** `"heads"` or `"tails"`
- If neither condition is met — for example `"hi"`, `"1"`, or an empty string — the error message is shown
- `continue` restarts the loop from the top, skipping the flip entirely and asking for a new guess

> **Important:** `continue` jumps back to the **start of the while loop** — not to the next line. This means the coin is never flipped, no result is shown, and the user is simply asked again. Without `continue`, invalid input would fall through to the flip logic and cause confusing behaviour.

| User Input | Valid? | Action |
|------------|--------|--------|
| `"heads"` | ✅ Yes | Proceed to flip |
| `"tails"` | ✅ Yes | Proceed to flip |
| `"Heads"` | ✅ Yes | `.lower()` converts to `"heads"` — valid |
| `"coin"` | ❌ No | Show error, `continue` |
| `""` | ❌ No | Show error, `continue` |
| `"123"` | ❌ No | Show error, `continue` |

---

### Step 6 — Simulate the Coin Flip

```python
flip = random.choice(["heads", "tails"])
```

- `random.choice()` picks **one random item** from the list `["heads", "tails"]`
- Each outcome has exactly a **50% probability** — just like a real coin
- The result is stored in `flip`
- A different result may occur every time this line runs

> **Important:** `random.choice()` is the cleanest way to simulate a binary random event like a coin flip. An alternative would be `random.randint(0, 1)` and mapping `0` to `"heads"` and `1` to `"tails"`, but `random.choice()` is more readable and direct.

---

### Step 7 — Show the Result

```python
print(f"\nCoin shows {flip}")
```

- Displays the outcome of the coin flip with a blank line before it (`\n`) for visual spacing
- The f-string embeds the `flip` value directly into the message

---

### Step 8 — Compare Guess to Flip

```python
if guess == flip:
    print("You won, you guessed correctly")
else:
    print("Sorry, wrong guess, try again")
```

- Compares the user's `guess` directly to the `flip` result
- Since both are already lowercase strings, no conversion is needed here
- If they match — win message; if not — loss message

| `guess` | `flip` | `guess == flip` | Result |
|---------|--------|----------------|--------|
| `"heads"` | `"heads"` | `True` | You won! |
| `"heads"` | `"tails"` | `False` | Wrong guess |
| `"tails"` | `"tails"` | `True` | You won! |
| `"tails"` | `"heads"` | `False` | Wrong guess |

---

### Step 9 — Ask to Play Again

```python
again = input("\nPlay again? (yes/no): ").lower()
if not again.startswith("y"):
    print("Goodbye")
    break
```

- `input()` asks if the user wants to play another round
- `.lower()` is chained immediately — so `"Yes"`, `"YES"`, and `"yes"` all work
- `.startswith("y")` checks if the response **begins with** the letter `"y"`
- If it does **not** start with `"y"`, the game prints `"Goodbye"` and `break` exits the loop

> **Important:** `.startswith("y")` is more flexible than `== "yes"`. It accepts `"yes"`, `"yeah"`, `"yep"`, `"yup"` — any `"y"` response keeps the game going. Anything else — `"no"`, `"n"`, `"nope"`, blank, or a typo — ends the game. This is very user-friendly.

| User Input | `.lower()` | `.startswith("y")` | Action |
|------------|-----------|-------------------|--------|
| `"yes"` | `"yes"` | `True` | Play again |
| `"Yeah"` | `"yeah"` | `True` | Play again |
| `"yup"` | `"yup"` | `True` | Play again |
| `"no"` | `"no"` | `False` | Goodbye + `break` |
| `"nope"` | `"nope"` | `False` | Goodbye + `break` |
| `""` | `""` | `False` | Goodbye + `break` |

---

## 📊 Game Flow Diagram

```
Start
  ↓
Print title and instructions
  ↓
┌─────────────────────────────┐
│        while True           │
│  ↓                          │
│  Get guess → .lower()       │
│  ↓                          │
│  Valid? ──No──→ continue ───┐│
│  ↓ Yes                      ││
│  Flip coin (random.choice)  ││
│  ↓                          ││
│  Show result                ││
│  ↓                          ││
│  Win or Lose?               ││
│  ↓                          ││
│  Play again?                ││
│  starts with "y"? ──No──→ break
│  ↓ Yes                      │
│  Loop again ────────────────┘
  ↓
End
```

---

## 📊 Example Output

### Example 1 — Win

```
COIN FLIP GAME
Guess heads or tails

Enter your guess (heads/tails): heads

Coin shows heads
You won, you guessed correctly

Play again? (yes/no): yes
```

### Example 2 — Loss

```
Enter your guess (heads/tails): tails

Coin shows heads
Sorry, wrong guess, try again

Play again? (yes/no): yes
```

### Example 3 — Invalid Input

```
Enter your guess (heads/tails): coin
Please enter 'heads' or 'tails'

Enter your guess (heads/tails): heads

Coin shows tails
Sorry, wrong guess, try again

Play again? (yes/no): no
Goodbye
```

---

## 🧠 Concepts Practised

| Concept | Where Used |
|---------|-----------|
| `import random` | Importing the random module |
| `print()` | Displaying title, result, and messages |
| `input()` | Getting the guess and play-again response |
| `while True` | Keeping the game running |
| `break` | Ending the game when user says no |
| `continue` | Restarting the loop on invalid input |
| `.lower()` | Making input case-insensitive |
| Input validation | Checking guess is `"heads"` or `"tails"` |
| `random.choice()` | Simulating the 50/50 coin flip |
| `if/else` | Comparing guess to flip result |
| `.startswith()` | Flexible play-again detection |
| f-strings | Embedding values in output messages |
| `\n` in prompts | Adding spacing between rounds |

---

## 👩‍💻 Author

**Pauline Oraro**
60 Days of Python Challenge — Coin Flip Game Project
