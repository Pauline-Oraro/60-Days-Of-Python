# 🔤 Guess the Word — Mini Project

A command-line word game where the player is shown a scrambled word and must figure out what it is. The game picks a random word from a list, shuffles its letters, and challenges the user to unscramble it. It keeps playing until the user decides to quit.

---

## 📋 Project Overview

| Detail | Info |
|--------|------|
| **Project Type** | Mini Project — Command Line Game |
| **Difficulty** | Beginner |
| **Concepts Used** | `import random`, lists, `while` loop, `break`, `random.choice()`, `random.shuffle()`, `list()`, `"".join()`, `input()`, `.lower()`, `.startswith()`, f-strings |

---

## 💻 Full Code

```python
import random

print("\n=== GUESS THE WORD! ===")
print("Unscramble the letters to find the word")

words = ["python", "coding", "programming", "computer", "technology", "fun", "learn"]

while True:
    original_word = random.choice(words)

    letters = list(original_word)
    random.shuffle(letters)
    scrambled = "".join(letters)

    print(f"\nScrambled word: {scrambled}")

    guess = input("What is the word?: ").lower()

    if guess == original_word:
        print("Congrats you win!")
    else:
        print(f"Sorry, the word was: {original_word}")

    again = input("Play again? (y/n): ").lower()
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
- Imported at the top of the file so it is available throughout the entire program
- Used for two functions: `random.choice()` to pick a word and `random.shuffle()` to scramble its letters

> **Important:** Always place `import` statements at the **very top** of your file. Python reads top to bottom — using `random` before importing it will raise a `NameError`.

---

### Step 2 — Display the Title and Instructions

```python
print("\n=== GUESS THE WORD! ===")
print("Unscramble the letters to find the word")
```

- `\n` at the start of the first `print()` adds a blank line before the title for clean terminal presentation
- `===` around the title adds visual emphasis — a simple way to make CLI output look polished
- The second line gives the player clear instructions before the game begins

---

### Step 3 — Define the Word List

```python
words = ["python", "coding", "programming", "computer", "technology", "fun", "learn"]
```

- A **list** of words that the game can randomly select from
- All words are in **lowercase** — this is important for the comparison in Step 8
- Defined **outside** the loop so it is created once and reused every round

> **Important:** The words are all lowercase to match the `.lower()` applied to the user's guess. Consistency in casing makes the comparison `guess == original_word` reliable. If the words were mixed case, a user typing `"python"` correctly could still fail the check.

---

### Step 4 — Start an Infinite Loop

```python
while True:
```

- Creates an **infinite loop** that runs a new round of the game each iteration
- The player controls how many rounds they play — the loop exits only when they type `"n"`
- Stopped with a `break` statement at the end of each round

---

### Step 5 — Pick a Random Word

```python
original_word = random.choice(words)
```

- `random.choice()` picks **one random word** from the `words` list
- Every word has an equal probability of being selected
- The chosen word is stored in `original_word` — preserved for the comparison and reveal later

> **Important:** `original_word` is saved **before** scrambling. The scrambling process modifies a separate variable (`letters` and then `scrambled`) — `original_word` stays unchanged so it can be compared to the user's guess and revealed if they are wrong.

---

### Step 6 — Scramble the Word

```python
letters = list(original_word)
random.shuffle(letters)
scrambled = "".join(letters)
```

This three-line block converts a word string into a shuffled string. Let's break each line down:

#### `letters = list(original_word)`

- `list()` splits the string into a **list of individual characters**
- Example: `"python"` → `["p", "y", "t", "h", "o", "n"]`
- Necessary because `random.shuffle()` works on **lists**, not strings
- Strings are **immutable** in Python — they cannot be rearranged in place

#### `random.shuffle(letters)`

- Randomly reorders the items in the `letters` list **in place**
- Modifies `letters` directly — does **not** return a new list
- Example: `["p", "y", "t", "h", "o", "n"]` → `["h", "n", "p", "o", "y", "t"]`

> **Important:** `random.shuffle()` returns `None`. A common mistake is writing `letters = random.shuffle(letters)` — this would set `letters` to `None`. The correct usage is `random.shuffle(letters)` with no assignment.

#### `scrambled = "".join(letters)`

- `"".join()` joins the shuffled list back into a **single string**
- The `""` separator means no character is placed between the letters
- Example: `["h", "n", "p", "o", "y", "t"]` → `"hnpoyt"`

**Full scrambling workflow:**
```
"python"
    ↓  list()
["p", "y", "t", "h", "o", "n"]
    ↓  random.shuffle()
["h", "n", "p", "o", "y", "t"]
    ↓  "".join()
"hnpoyt"
```

---

### Step 7 — Show the Scrambled Word

```python
print(f"\nScrambled word: {scrambled}")
```

- Displays the scrambled word to the player
- `\n` before the text adds visual spacing from the previous round's output
- The f-string embeds the `scrambled` value directly into the message

---

### Step 8 — Get the Player's Guess

```python
guess = input("What is the word?: ").lower()
```

- `input()` waits for the player to type their answer and press **Enter**
- `.lower()` is chained directly — converts the guess to lowercase immediately
- This means `"Python"`, `"PYTHON"`, and `"python"` all match `original_word`

> **Important:** `.lower()` on the guess ensures **case-insensitive comparison**. Since `original_word` is already lowercase, applying `.lower()` to the guess means they will always be in the same case when compared.

---

### Step 9 — Check the Guess and Display the Result

```python
if guess == original_word:
    print("Congrats you win!")
else:
    print(f"Sorry, the word was: {original_word}")
```

- Compares `guess` to `original_word` using `==`
- Both are lowercase strings at this point — a reliable direct comparison
- If the guess is correct — congratulations message
- If wrong — reveals the original word using an f-string so the player learns

| `guess` | `original_word` | `guess == original_word` | Result |
|---------|----------------|--------------------------|--------|
| `"python"` | `"python"` | `True` | Congrats! |
| `"pytohn"` | `"python"` | `False` | Reveal word |
| `"PYTHON"` | `"python"` | `False` | Reveal word |
| `"Python"` after `.lower()` | `"python"` | `True` | Congrats! |

---

### Step 10 — Ask to Play Again

```python
again = input("Play again? (y/n): ").lower()
if not again.startswith("y"):
    print("Goodbye")
    break
```

- `input()` gets the player's response, `.lower()` normalizes it
- `.startswith("y")` accepts `"y"`, `"yes"`, `"yeah"`, `"yup"` — any `"y"` response continues
- `not` reverses the check — if the response does **not** start with `"y"`, the game ends
- `break` exits the `while True` loop

---

## 📊 Scrambling Visualized

```
Word Bank: ["python", "coding", "programming", "computer", "technology", "fun", "learn"]

random.choice() → "computer"

list("computer") → ["c", "o", "m", "p", "u", "t", "e", "r"]

random.shuffle() → ["t", "e", "c", "u", "r", "o", "m", "p"]

"".join()       → "tecuoromp"

Display: "Scrambled word: tecuoromp"
```

---

## 📊 Example Output

### Example 1 — Correct Guess

```
=== GUESS THE WORD! ===
Unscramble the letters to find the word

Scrambled word: gnidoc
What is the word?: coding
Congrats you win!
Play again? (y/n): y
```

### Example 2 — Wrong Guess

```
Scrambled word: tnohyp
What is the word?: thinop
Sorry, the word was: python
Play again? (y/n): y
```

### Example 3 — Case Insensitive Win

```
Scrambled word: nmgriropgma
What is the word?: Programming
Congrats you win!
Play again? (y/n): n
Goodbye
```

### Example 4 — Short Word

```
Scrambled word: nuf
What is the word?: fun
Congrats you win!
Play again? (y/n): n
Goodbye
```

> Short words like `"fun"` are easier — there are only 6 possible arrangements of 3 letters. Longer words like `"programming"` with 11 letters have thousands of possible scrambles.

---

## 🧠 Concepts Practised

| Concept | Where Used |
|---------|-----------|
| `import random` | Importing the random module |
| Lists | Storing the word bank and splitting the word into characters |
| `while True` | Keeping the game running for multiple rounds |
| `break` | Ending the game when player declines another round |
| `random.choice()` | Picking a random word from the list |
| `list()` | Splitting the string into individual characters |
| `random.shuffle()` | Randomly reordering the character list in place |
| `"".join()` | Reassembling the characters into a string |
| `input()` | Getting the player's guess and play-again response |
| `.lower()` | Case-insensitive guess comparison |
| `if/else` | Checking correct vs incorrect guess |
| `.startswith()` | Flexible play-again detection |
| f-strings | Embedding values in output messages |
| `\n` in strings | Adding blank lines for visual spacing |

---

## 👩‍💻 Author

**Pauline Oraro**
60 Days of Python Challenge — Guess The Word Project
