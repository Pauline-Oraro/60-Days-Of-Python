# 🔎 Character Type Checker — Mini Project

A simple command-line Python application that takes a single character as input and identifies whether it is a **letter**, a **digit**, or a **special character**. A great beginner project for practising string methods and conditional logic.

---

## 📋 Project Overview

| Detail | Info |
|--------|------|
| **Project Type** | Mini Project — Command Line App |
| **Difficulty** | Beginner |
| **Concepts Used** | `input()`, `print()`, string methods, `if/elif/else`, variables |
| **Lines of Code** | ~9 |

---

## 💻 Full Code

```python
print("CHARACTER TYPE CHECKER")

char = input("Enter a single character: ")

if char.isalpha():
    print("This is a letter.")
elif char.isdigit():
    print("This is a digit.")
else:
    print("This is a special char.")
```

---

## 🔍 Step-by-Step Explanation

### Step 1 — Display the App Title

```python
print("CHARACTER TYPE CHECKER")
```

- Prints the name of the application to the terminal
- Immediately tells the user the purpose of the program before any input is requested
- **Good practice:** A clear title makes CLI apps feel more professional and intentional

---

### Step 2 — Get the Character Input

```python
char = input("Enter a single character: ")
```

- `input()` pauses the program and waits for the user to type something and press **Enter**
- The typed character is stored as a **string** in the variable `char`
- No type conversion is needed — string methods work directly on strings

> **Important:** `input()` always returns a **string**, even if the user types a number like `"5"`. This is actually useful here because `.isdigit()` works on string characters, not integer values.

> **Note:** The program trusts the user to enter only one character. If the user types multiple characters (e.g. `"ab"`), `.isalpha()` would still return `True` because all characters are letters. In a production app you would validate that exactly one character was entered.

---

### Step 3 — Check if It Is a Letter

```python
if char.isalpha():
    print("This is a letter.")
```

- `.isalpha()` returns `True` if **all characters** in the string are alphabetic (a–z, A–Z)
- Returns `False` if the string contains digits, spaces, or special characters
- Works with both **uppercase** and **lowercase** letters

| Input | `.isalpha()` | Reason |
|-------|-------------|--------|
| `"a"` | `True` | Lowercase letter |
| `"Z"` | `True` | Uppercase letter |
| `"3"` | `False` | Digit, not a letter |
| `"@"` | `False` | Special character |
| `" "` | `False` | Space is not a letter |

---

### Step 4 — Check if It Is a Digit

```python
elif char.isdigit():
    print("This is a digit.")
```

- Only runs if `.isalpha()` returned `False`
- `.isdigit()` returns `True` if **all characters** in the string are numeric digits (0–9)
- Returns `False` for letters, spaces, and special characters

| Input | `.isdigit()` | Reason |
|-------|-------------|--------|
| `"5"` | `True` | Numeric digit |
| `"0"` | `True` | Numeric digit |
| `"a"` | `False` | Letter, not a digit |
| `"#"` | `False` | Special character |
| `"3.5"` | `False` | Decimal point is not a digit |

> **Important:** `.isdigit()` returns `False` for `"3.5"` because the `.` (decimal point) is not a digit character. It only recognises whole number characters `0`–`9`.

---

### Step 5 — Handle Everything Else

```python
else:
    print("This is a special char.")
```

- The `else` block is the **fallback** — it catches anything that is neither a letter nor a digit
- This includes: `@`, `#`, `$`, `%`, `!`, `?`, spaces, punctuation marks, and symbols
- No condition is needed — if both `.isalpha()` and `.isdigit()` returned `False`, it must be a special character

> **Important:** The `else` block is what makes the logic **complete and exhaustive** — every possible input is handled. Without it, special characters would produce no output at all.

---

## 📊 String Methods Used

| Method | Returns `True` When... | Returns `False` When... |
|--------|----------------------|------------------------|
| `.isalpha()` | All characters are letters (a–z, A–Z) | Contains digits, spaces, or symbols |
| `.isdigit()` | All characters are digits (0–9) | Contains letters, spaces, or symbols |

### Other Useful Related Methods

| Method | Description | Example |
|--------|-------------|---------|
| `.isalnum()` | `True` if all characters are letters **or** digits | `"abc123"` → `True` |
| `.isspace()` | `True` if all characters are whitespace | `" "` → `True` |
| `.isupper()` | `True` if all letters are uppercase | `"ABC"` → `True` |
| `.islower()` | `True` if all letters are lowercase | `"abc"` → `True` |
| `.isprintable()` | `True` if all characters are printable | `"hello!"` → `True` |

---

## 📊 Example Outputs

### Example 1 — Letter

```
CHARACTER TYPE CHECKER
Enter a single character: p
This is a letter.
```

### Example 2 — Digit

```
CHARACTER TYPE CHECKER
Enter a single character: 7
This is a digit.
```

### Example 3 — Special Character

```
CHARACTER TYPE CHECKER
Enter a single character: @
This is a special char.
```

### Example 4 — Space

```
CHARACTER TYPE CHECKER
Enter a single character:  
This is a special char.
```

> A space is neither a letter nor a digit, so it falls into the `else` branch.

---

## 🧠 Concepts Practised

| Concept | Where Used |
|---------|-----------|
| `print()` | Displaying the title and result |
| `input()` | Getting the user's character |
| Variables | Storing `char` |
| `.isalpha()` | Checking if the character is a letter |
| `.isdigit()` | Checking if the character is a digit |
| `if/elif/else` | Handling the three possible character types |
| String methods | Identifying character properties |

---

## 👩‍💻 Author

**Pauline Oraro**
60 Days of Python Challenge — Check Char Type Project
