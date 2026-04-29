# 🔤 Text Capitalizer — Mini Project

A simple command-line Python application that takes a user's text input and transforms it into one of four different capitalization formats. A great beginner project for practising string methods and conditional logic.

---

## 📋 Project Overview

| Detail | Info |
|--------|------|
| **Project Type** | Mini Project — Command Line App |
| **Difficulty** | Beginner |
| **Concepts Used** | `input()`, `print()`, string methods, `if/elif`, variables |

---

## 💻 Full Code

```python
print("TEXT CAPITALIZER")

text = input("Enter some text: ")
print("1. UPPERCASE")
print("2. lowercase")
print("3. Title case")
print("4. Sentence case")

choice = input("Choose a format (1-4): ")

if choice == "1":
    print(text.upper())
elif choice == "2":
    print(text.lower())
elif choice == "3":
    print(text.title())
elif choice == "4":
    print(text.capitalize())
```

---

## 🔍 Step-by-Step Explanation

### Step 1 — Display the App Title

```python
print("TEXT CAPITALIZER")
```

- Prints the name of the application to the terminal
- Gives the user an immediate idea of what the program does before any interaction begins
- **Good practice:** Always label CLI apps clearly — it makes them feel more polished and user-friendly

---

### Step 2 — Get the User's Text

```python
text = input("Enter some text: ")
```

- `input()` pauses the program and waits for the user to type text and press **Enter**
- The typed text is stored as a **string** in the variable `text`

> **Important:** `input()` always returns a **string**. This is perfect here because all string methods work on strings. No type conversion is needed.

---

### Step 3 — Display the Menu Options

```python
print("1. UPPERCASE")
print("2. lowercase")
print("3. Title case")
print("4. Sentence case")
```

- Four `print()` statements display a numbered menu to the user
- Each option shows a preview of what the format looks like right in its label — `UPPERCASE`, `lowercase`, `Title case`, `Sentence case`
- This is a **self-documenting menu** — the user can instantly see what each option will do without needing extra explanation

> **Good design tip:** Showing a live preview of each option in the menu (like writing the option name in its own format) is a small but effective UX touch that reduces confusion.

---

### Step 4 — Get the User's Format Choice

```python
choice = input("Choose a format (1-4): ")
```

- `input()` waits for the user to type a number between 1 and 4
- The result is stored as a **string** in `choice` — `"1"`, `"2"`, `"3"`, or `"4"`
- It is stored as a string, not an integer, because it is compared using `==` to string literals in the next step

> **Important:** `choice` is compared as a **string** (`"1"`, `"2"`) not an integer (`1`, `2`). This is why we do not wrap it in `int()`. If you converted `choice` to an integer and compared it to `"1"`, the condition would always be `False`.

---

### Step 5 — Apply the Chosen Format

```python
if choice == "1":
    print(text.upper())
elif choice == "2":
    print(text.lower())
elif choice == "3":
    print(text.title())
elif choice == "4":
    print(text.capitalize())
```

Python checks each condition from top to bottom and executes the **first matching branch** only.

#### Option 1 — `.upper()`

```python
if choice == "1":
    print(text.upper())
```

- Converts **every character** in the string to uppercase
- Example: `"hello world"` → `"HELLO WORLD"`
- Useful for headings, labels, or emphasis

#### Option 2 — `.lower()`

```python
elif choice == "2":
    print(text.lower())
```

- Converts **every character** in the string to lowercase
- Example: `"Hello World"` → `"hello world"`
- Useful for normalising input before comparison (e.g. email addresses)

#### Option 3 — `.title()`

```python
elif choice == "3":
    print(text.title())
```

- Capitalizes the **first letter of every word**, lowercases the rest
- Example: `"hello world"` → `"Hello World"`
- Useful for names, book titles, headings

> **Important:** `.title()` capitalizes after **any non-letter character**, which can produce unexpected results with apostrophes. For example: `"it's fine"` → `"It'S Fine"`. Python's `str.title()` is a simple implementation — for more accurate title casing you'd use the `titlecase` library.

#### Option 4 — `.capitalize()`

```python
elif choice == "4":
    print(text.capitalize())
```

- Capitalizes only the **very first character** of the entire string, lowercases the rest
- Example: `"hello world"` → `"Hello world"`
- Example: `"HELLO WORLD"` → `"Hello world"`
- Useful for sentences, paragraphs, or correcting ALL CAPS input

---

## 📊 String Methods Comparison

| Method | What It Does | Example Input | Example Output |
|--------|-------------|---------------|----------------|
| `.upper()` | All characters UPPERCASE | `"hello world"` | `"HELLO WORLD"` |
| `.lower()` | All characters lowercase | `"HELLO WORLD"` | `"hello world"` |
| `.title()` | First letter of Every Word capitalised | `"hello world"` | `"Hello World"` |
| `.capitalize()` | Only the very first character capitalised | `"hello world"` | `"Hello world"` |

---

## 📊 Example Outputs

### Example 1 — UPPERCASE

```
TEXT CAPITALIZER
Enter some text: python is amazing
1. UPPERCASE
2. lowercase
3. Title case
4. Sentence case
Choose a format (1-4): 1
PYTHON IS AMAZING
```

### Example 2 — lowercase

```
TEXT CAPITALIZER
Enter some text: PYTHON IS AMAZING
1. UPPERCASE
2. lowercase
3. Title case
4. Sentence case
Choose a format (1-4): 2
python is amazing
```

### Example 3 — Title Case

```
TEXT CAPITALIZER
Enter some text: python is amazing
1. UPPERCASE
2. lowercase
3. Title case
4. Sentence case
Choose a format (1-4): 3
Python Is Amazing
```

### Example 4 — Sentence Case

```
TEXT CAPITALIZER
Enter some text: PYTHON IS AMAZING
1. UPPERCASE
2. lowercase
3. Title case
4. Sentence case
Choose a format (1-4): 4
Python is amazing
```

---

## 🧠 Concepts Practised

| Concept | Where Used |
|---------|-----------|
| `print()` | Displaying the title, menu, and result |
| `input()` | Getting the user's text and format choice |
| Variables | Storing `text` and `choice` |
| String methods | `.upper()`, `.lower()`, `.title()`, `.capitalize()` |
| `if/elif` | Checking which option the user selected |
| String comparison | Comparing `choice` to `"1"`, `"2"`, etc. |

---

## 👩‍💻 Author

**Pauline Oraro**
60 Days of Python Challenge — Text Formatter Project
