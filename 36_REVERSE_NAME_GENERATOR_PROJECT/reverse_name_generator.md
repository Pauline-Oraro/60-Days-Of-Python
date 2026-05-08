# 🔄 Reverse Name Generator — Mini Project

A fun command-line Python application that takes a name and reverses it — imagining what you'd be called in a parallel universe. The program keeps running until the user decides to stop.

---

## 📋 Project Overview

| Detail | Info |
|--------|------|
| **Project Type** | Mini Project — Command Line App |
| **Difficulty** | Beginner |
| **Concepts Used** | `input()`, `print()`, `while` loop, `break`, string slicing `[::-1]`, `.title()`, f-strings, `if` statements |

---

## 💻 Full Code

```python
print("REVERSE NAME GENERATOR")

while True:
    name = input("\nEnter a name: ")

    if not name:
        break

    reversed_name = name[::-1]
    print(f"Your reversed name is: {reversed_name}")
    print(f"In a parallel universe, they call you {reversed_name.title()}")

    answer = input("\nTry another name? (yes/no): ")
    if answer != "yes":
        break
```

---

## 🔍 Step-by-Step Explanation

### Step 1 — Display the App Title

```python
print("REVERSE NAME GENERATOR")
```

- Prints the application name to the terminal
- Immediately communicates the purpose of the program before any input is requested

---

### Step 2 — Start an Infinite Loop

```python
while True:
```

- Creates an **infinite loop** that keeps running until explicitly stopped
- Used here because the user decides how many names to reverse — the count is unknown in advance
- The loop has **two exit points** — an empty input and a `"no"` response

> **Important:** This loop has **two different `break` conditions** — one for an empty name input and one for when the user chooses not to continue. Having multiple exit points is perfectly valid and is a common pattern in interactive CLI apps.

---

### Step 3 — Get the Name Input

```python
name = input("\nEnter a name: ")
```

- `input()` pauses the program and waits for the user to type a name and press **Enter**
- The typed name is stored as a **string** in the variable `name`
- The `\n` at the start of the prompt adds a **blank line** before the input prompt — spacing the output neatly for readability

> **Important:** `\n` is an **escape character** that represents a new line. It adds visual breathing room between entries when the program loops, making the output easier to read.

---

### Step 4 — Handle Empty Input

```python
if not name:
    break
```

- `not name` evaluates to `True` when `name` is an **empty string** `""`
- If the user presses **Enter** without typing anything, the loop exits immediately
- This is a safe and intuitive way to let users quit — just press Enter

> **Important:** In Python, an **empty string** `""` is **falsy** — it evaluates to `False` in a boolean context. So `if not name` is equivalent to `if name == ""`. This is the Pythonic way to check for empty input.

| User Input | `not name` | Action |
|------------|-----------|--------|
| `"Pauline"` | `False` | Continue — process the name |
| `""` (just Enter) | `True` | `break` — exit the loop |

---

### Step 5 — Reverse the Name

```python
reversed_name = name[::-1]
```

- `[::-1]` is Python's **slice notation** used to reverse a string
- It means: start from the end, go to the beginning, step by `-1` (move backwards one character at a time)
- The reversed string is stored in `reversed_name`

**How `[::-1]` works:**

```
Slice syntax: [start : stop : step]
              [  -   :  -   :  -1 ]

"Pauline"[::-1]
→ reads each character from right to left
→ "eniluaP"
```

| Name | `name[::-1]` |
|------|-------------|
| `"Pauline"` | `"eniluaP"` |
| `"Kate"` | `"etaK"` |
| `"John"` | `"nhoJ"` |
| `"Anna"` | `"annA"` |
| `"Bob"` | `"boB"` |

> **Important:** `[::-1]` works on **any sequence** in Python — strings, lists, and tuples. It does not modify the original `name` variable — it returns a **new reversed string** which is then stored in `reversed_name`.

---

### Step 6 — Display the Reversed Name

```python
print(f"Your reversed name is: {reversed_name}")
print(f"In a parallel universe, they call you {reversed_name.title()}")
```

#### First Print — Raw Reversed Name

```python
print(f"Your reversed name is: {reversed_name}")
```

- Displays the reversed name exactly as produced by `[::-1]`
- The capitalisation from the original input is preserved but mirrored
- Example: `"Pauline"` → `"eniluaP"`

#### Second Print — Title Cased Reversed Name

```python
print(f"In a parallel universe, they call you {reversed_name.title()}")
```

- `.title()` capitalises the **first letter** of each word in the reversed string
- This gives the reversed name a proper name feel — more like an actual alternate-universe name
- Example: `"eniluaP"` → `"Eniluap"`

> **Important:** `.title()` is applied to the **already reversed** string, not the original. The order matters — reverse first, then format. The fun flavor text `"In a parallel universe"` makes the output feel playful and engaging — good UX storytelling for a simple app.

---

### Step 7 — Ask to Continue

```python
answer = input("\nTry another name? (yes/no): ")
if answer != "yes":
    break
```

- `input()` asks the user if they want to try another name
- If the user types anything **other than** `"yes"` — including `"no"`, `"No"`, or just pressing Enter — the loop exits
- Only the exact string `"yes"` keeps the loop running

> **Important:** The condition `answer != "yes"` is more lenient than checking `answer == "no"`. It exits for **any response that isn't `"yes"`** — including typos, blank input, or `"No"`. This makes the exit easier for the user since they don't have to type `"no"` precisely.

---

## 📊 How String Reversal Works

```
name = "Pauline"

Indices (forward):   P  a  u  l  i  n  e
                     0  1  2  3  4  5  6

Indices (backward):  P  a  u  l  i  n  e
                    -7 -6 -5 -4 -3 -2 -1

name[::-1] reads from index -1 to -7:
→ e, n, i, l, u, a, P
→ "eniluaP"
```

---

## 📊 Example Output

```
REVERSE NAME GENERATOR

Enter a name: Pauline
Your reversed name is: eniluaP
In a parallel universe, they call you Eniluap

Try another name? (yes/no): yes

Enter a name: Kate
Your reversed name is: etaK
In a parallel universe, they call you Etak

Try another name? (yes/no): yes

Enter a name: John
Your reversed name is: nhoJ
In a parallel universe, they call you Nhoj

Try another name? (yes/no): no
```

---

## 🧠 Concepts Practised

| Concept | Where Used |
|---------|-----------|
| `print()` | Displaying the title and results |
| `input()` | Getting the name and continue response |
| `while True` | Keeping the program running |
| `break` | Two exit conditions — empty input and `"no"` |
| `if not name` | Checking for empty string input |
| `[::-1]` | Reversing the string using slice notation |
| `.title()` | Capitalising the first letter of the reversed name |
| f-strings | Embedding variables in printed messages |
| `\n` in prompt | Adding spacing for cleaner output |
| `!=` operator | Exiting when the answer is not `"yes"` |

---

## 👩‍💻 Author

**Pauline Oraro**
60 Days of Python Challenge — Reverse Name Generator Project
