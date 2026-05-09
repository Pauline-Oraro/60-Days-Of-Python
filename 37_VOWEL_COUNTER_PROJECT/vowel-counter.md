# 🔤 Vowel Counter — Mini Project

A command-line Python application that counts the number of vowels in any text the user enters. It uses a compact and elegant one-liner to do the counting and keeps running until the user types `quit`.

---

## 📋 Project Overview

| Detail | Info |
|--------|------|
| **Project Type** | Mini Project — Command Line App |
| **Difficulty** | Beginner–Intermediate |
| **Concepts Used** | `input()`, `print()`, `while` loop, `break`, `sum()`, generator expression, `for` loop, `if` condition, `.lower()`, f-strings |

---

## 💻 Full Code

```python
print("VOWEL COUNTER")

while True:
    text = input("\nEnter some text (or quit): ")

    if text.lower() == "quit":
        print("Goodbye")
        break

    vowels = sum(1 for char in text.lower() if char in "aeiou")
    print(f"That text has {vowels} vowels!")
```

---

## 🔍 Step-by-Step Explanation

### Step 1 — Display the App Title

```python
print("VOWEL COUNTER")
```

- Prints the name of the application to the terminal
- Immediately tells the user the purpose of the program

---

### Step 2 — Start an Infinite Loop

```python
while True:
```

- Creates an **infinite loop** that keeps running until the user types `"quit"`
- The correct pattern when the number of iterations is unknown in advance
- Stopped using a `break` statement inside the loop

> **Important:** Every `while True` loop must have a reachable `break` condition — otherwise the program runs forever and must be force-quit.

---

### Step 3 — Get the Text Input

```python
text = input("\nEnter some text (or quit): ")
```

- `input()` pauses the program and waits for the user to type text and press **Enter**
- The typed text is stored as a **string** in the variable `text`
- `\n` at the start of the prompt adds a blank line before each input — keeping the output visually clean as the loop repeats

> **Important:** `\n` is an **escape character** representing a new line. It creates visual spacing between entries, making repeated output much easier to read.

---

### Step 4 — Check for the Exit Condition

```python
if text.lower() == "quit":
    print("Goodbye")
    break
```

- `.lower()` converts the input to lowercase before comparing — so `"Quit"`, `"QUIT"`, and `"quit"` all trigger the exit
- If matched, `"Goodbye"` is printed and `break` exits the loop
- This check happens **before** counting vowels so `"quit"` is never processed as text

> **Important:** `.lower()` makes the exit **case-insensitive**. Without it, only the exact lowercase string `"quit"` would work — `"Quit"` or `"QUIT"` would be counted for vowels instead of exiting.

---

### Step 5 — Count the Vowels

```python
vowels = sum(1 for char in text.lower() if char in "aeiou")
```

This is the core of the program — a compact and powerful one-liner. Let's break it down fully.

#### Part 1 — `text.lower()`

```python
text.lower()
```

- Converts the entire input to lowercase before counting
- Ensures that uppercase vowels like `"A"`, `"E"`, `"I"`, `"O"`, `"U"` are counted too
- Example: `"Hello"` → `"hello"`, so `"H"` doesn't get missed as a vowel check issue

> **Important:** Without `.lower()`, the check `char in "aeiou"` would miss uppercase vowels because `"A"` is not in `"aeiou"`. Lowercasing first ensures case-insensitive counting.

#### Part 2 — `for char in text.lower()`

```python
for char in text.lower()
```

- Iterates over **every character** in the lowercased string one at a time
- Each character is temporarily stored in the variable `char`
- Example: `"hello"` → iterates `"h"`, `"e"`, `"l"`, `"l"`, `"o"`

#### Part 3 — `if char in "aeiou"`

```python
if char in "aeiou"
```

- For each character, checks whether it is one of the five vowels
- `"aeiou"` is used as a lookup string — `in` checks if the character exists within it
- Returns `True` for vowels, `False` for consonants, digits, spaces, and symbols

| Character | `char in "aeiou"` | Counted? |
|-----------|------------------|----------|
| `"h"` | `False` | No |
| `"e"` | `True` | Yes |
| `"l"` | `False` | No |
| `"o"` | `True` | Yes |
| `" "` | `False` | No |
| `"!"` | `False` | No |

#### Part 4 — `1 for char in ... if ...` (Generator Expression)

```python
1 for char in text.lower() if char in "aeiou"
```

- This is a **generator expression** — a compact way to produce a sequence of values without creating a full list in memory
- For every character that passes the `if` condition (is a vowel), it generates the value `1`
- Non-vowels are simply skipped — they contribute nothing

> **Important:** A **generator expression** is similar to a **list comprehension** but more memory-efficient — it generates values one at a time rather than building a complete list. For large texts, this is significantly faster and uses less memory.

**Equivalent using a list comprehension (less efficient):**
```python
[1 for char in text.lower() if char in "aeiou"]
# → [1, 1, 1] for "hello" (e, l skipped, o counted)
# Actually → [1, 1] for "hello" (e and o are vowels)
```

**Equivalent using a traditional loop (more verbose):**
```python
count = 0
for char in text.lower():
    if char in "aeiou":
        count += 1
```

#### Part 5 — `sum()`

```python
sum(1 for char in text.lower() if char in "aeiou")
```

- `sum()` adds up all the `1`s generated by the generator expression
- Each `1` represents one vowel found — summing them gives the total vowel count
- The result is stored in `vowels`

**Full walkthrough with `"Hello World"`:**
```
text.lower() → "hello world"

Characters:  h  e  l  l  o     w  o  r  l  d
Vowel?:      ✗  ✓  ✗  ✗  ✓  ✗  ✗  ✓  ✗  ✗  ✗
Generates:      1        1        1
sum([1, 1, 1]) = 3
```

---

### Step 6 — Display the Result

```python
print(f"That text has {vowels} vowels!")
```

- An f-string embeds the `vowels` count directly into the output message
- The exclamation mark keeps the tone fun and engaging

---

## 📊 The Vowels

| Vowel | Uppercase | Counted after `.lower()`? |
|-------|-----------|--------------------------|
| a | A | ✅ Yes |
| e | E | ✅ Yes |
| i | I | ✅ Yes |
| o | O | ✅ Yes |
| u | U | ✅ Yes |

> **Note:** `y` is sometimes considered a vowel in English but is **not counted** here. This is intentional — `"aeiou"` covers the five standard vowels. You could add `"y"` to the string to include it.

---

## 📊 Example Output

### Example 1

```
VOWEL COUNTER

Enter some text (or quit): Hello World
That text has 3 vowels!
```

**Breakdown:** `e`, `o`, `o` → 3 vowels

### Example 2

```
VOWEL COUNTER

Enter some text (or quit): Python is amazing
That text has 6 vowels!
```

**Breakdown:** `o`, `i`, `a`, `a`, `i`, `g` — wait, let's check:
```
p-y-t-h-o-n- -i-s- -a-m-a-z-i-n-g
        ✓     ✓     ✓   ✓ ✓
vowels: o, i, a, a, i → 5 vowels
```

### Example 3 — Numbers and Symbols

```
VOWEL COUNTER

Enter some text (or quit): Hello! 123
That text has 2 vowels!
```

**Breakdown:** Only `e` and `o` are vowels — numbers and `!` are ignored

### Example 4 — Exit

```
VOWEL COUNTER

Enter some text (or quit): quit
Goodbye
```

---

## 🧠 Concepts Practised

| Concept | Where Used |
|---------|-----------|
| `print()` | Displaying the title and result |
| `input()` | Getting the text from the user |
| `while True` | Keeping the program running |
| `break` | Exiting when user types `"quit"` |
| `.lower()` | Case-insensitive exit check and vowel counting |
| Generator expression | Efficiently generating a `1` for each vowel |
| `for char in string` | Iterating over each character |
| `if char in "aeiou"` | Checking if a character is a vowel |
| `sum()` | Adding up all the `1`s to get the total |
| f-strings | Embedding the vowel count in the output |
| `\n` in prompt | Adding spacing between loop iterations |

---

## 👩‍💻 Author

**Pauline Oraro**
60 Days of Python Challenge — Vowel Counter Project
