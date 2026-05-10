# 🎨 Color Mixer — Mini Project

A command-line Python application that tells you what color you get when you mix two colors together. With 29 color combinations built in, it simulates real-world color mixing using a dictionary of tuple keys. The program keeps running until the user decides to stop.

---

## 📋 Project Overview

| Detail | Info |
|--------|------|
| **Project Type** | Mini Project — Command Line App |
| **Difficulty** | Beginner–Intermediate |
| **Concepts Used** | Dictionaries, tuples as keys, `input()`, `while` loop, `break`, `.lower()`, `.strip()`, f-strings, `in` operator, method chaining |

---

## 💻 Full Code

```python
print("COLOR MIXER")

color_mixes = {
    ("red", "blue"):             "purple",
    ("red", "yellow"):           "orange",
    ("blue", "yellow"):          "green",
    ("blue", "green"):           "teal",
    ("white", "red"):            "pink",
    ("red", "green"):            "brown",
    ("white", "blue"):           "light blue",
    ("white", "yellow"):         "cream",
    ("white", "green"):          "mint",
    ("white", "purple"):         "lavender",
    ("white", "orange"):         "peach",
    ("white", "black"):          "gray",
    ("black", "red"):            "maroon",
    ("black", "blue"):           "navy",
    ("black", "yellow"):         "olive",
    ("black", "green"):          "dark green",
    ("black", "orange"):         "brown",
    ("black", "purple"):         "dark purple",
    ("red", "orange"):           "vermillion",
    ("yellow", "green"):         "chartreuse",
    ("blue", "purple"):          "indigo",
    ("orange", "yellow"):        "amber",
    ("orange", "red"):           "scarlet",
    ("pink", "purple"):          "mauve",
    ("pink", "orange"):          "salmon",
    ("yellow", "purple"):        "muddy brown",
    ("orange", "blue"):          "slate gray",
}

while True:
    color1 = input("\nEnter first color: ").lower().strip()
    color2 = input("Enter second color: ").lower().strip()

    mix = None

    if (color1, color2) in color_mixes:
        mix = color_mixes[(color1, color2)]
    elif (color2, color1) in color_mixes:
        mix = color_mixes[(color2, color1)]

    if mix:
        print(f"When you mix {color1} and {color2}, you get {mix}!")
    else:
        print("I don't know what those colors make when mixed")

    if not input("\nMix more colors? (y/n): ").lower().startswith("y"):
        print("Goodbye")
        break
```

---

## 🔍 Step-by-Step Explanation

### Step 1 — Display the App Title

```python
print("COLOR MIXER")
```

- Prints the application name to the terminal before any interaction begins
- Communicates the purpose of the program immediately

---

### Step 2 — Define the Color Mix Dictionary

```python
color_mixes = {
    ("red", "blue"): "purple",
    ("red", "yellow"): "orange",
    ...
}
```

This is the most interesting data structure in the program — a dictionary where the **keys are tuples**.

#### Why Tuples as Keys?

- Dictionary keys must be **immutable** (unchangeable) — strings, numbers, and tuples qualify; lists do not
- A tuple `("red", "blue")` represents a **pair of colors** perfectly as a single key
- This allows the lookup `color_mixes[("red", "blue")]` to directly return `"purple"`

> **Important:** Lists **cannot** be dictionary keys because they are mutable. Tuples **can** because they are immutable. This is one of the most practical real-world uses of tuples — grouping related values into an immutable key.

#### Dictionary Structure

```
Key (Tuple)           →  Value (Result Color)
("red", "blue")       →  "purple"
("blue", "yellow")    →  "green"
("white", "black")    →  "gray"
```

---

### Step 3 — Full Color Mix Reference Table

| Colors Mixed | Result |
|-------------|--------|
| 🔴 Red + 🔵 Blue | Purple |
| 🔴 Red + 🟡 Yellow | Orange |
| 🔵 Blue + 🟡 Yellow | Green |
| 🔵 Blue + 🟢 Green | Teal |
| ⚪ White + 🔴 Red | Pink |
| 🔴 Red + 🟢 Green | Brown |
| ⚪ White + 🔵 Blue | Light Blue |
| ⚪ White + 🟡 Yellow | Cream |
| ⚪ White + 🟢 Green | Mint |
| ⚪ White + 🟣 Purple | Lavender |
| ⚪ White + 🟠 Orange | Peach |
| ⚪ White + ⚫ Black | Gray |
| ⚫ Black + 🔴 Red | Maroon |
| ⚫ Black + 🔵 Blue | Navy |
| ⚫ Black + 🟡 Yellow | Olive |
| ⚫ Black + 🟢 Green | Dark Green |
| ⚫ Black + 🟠 Orange | Brown |
| ⚫ Black + 🟣 Purple | Dark Purple |
| 🔴 Red + 🟠 Orange | Vermillion |
| 🟡 Yellow + 🟢 Green | Chartreuse |
| 🔵 Blue + 🟣 Purple | Indigo |
| 🟠 Orange + 🟡 Yellow | Amber |
| 🟠 Orange + 🔴 Red | Scarlet |
| 🩷 Pink + 🟣 Purple | Mauve |
| 🩷 Pink + 🟠 Orange | Salmon |
| 🟡 Yellow + 🟣 Purple | Muddy Brown |
| 🟠 Orange + 🔵 Blue | Slate Gray |

---

### Step 4 — Start an Infinite Loop

```python
while True:
```

- Keeps the program running so the user can mix as many colors as they want
- Exited with `break` when the user says no to mixing more colors

---

### Step 5 — Get and Normalize Color Inputs

```python
color1 = input("\nEnter first color: ").lower().strip()
color2 = input("Enter second color: ").lower().strip()
```

Two methods are chained directly onto `input()`:

#### `.lower()`
- Converts the input to lowercase
- Ensures `"Red"`, `"RED"`, and `"red"` all match the dictionary keys

#### `.strip()`
- Removes any leading or trailing **whitespace** the user may have accidentally typed
- Ensures `"  red  "` becomes `"red"` — an exact match for the dictionary key

> **Important:** `.strip()` is essential for reliable dictionary lookups. Without it, a user typing an accidental space (`" red"`) would fail to find `("red", "blue")` in the dictionary even though the input looks correct. Always strip user input before using it as a lookup key.

---

### Step 6 — Initialize the Result as `None`

```python
mix = None
```

- `mix` is set to `None` before the lookup attempt
- `None` acts as a **flag** — if no match is found, `mix` stays `None`
- Used in the `if mix:` check below to decide what message to display

> **Important:** Initializing `mix = None` before the `if/elif` block is a clean pattern for handling optional results. It ensures the variable always exists regardless of whether a match was found, preventing a `NameError` if neither condition triggers.

---

### Step 7 — Look Up the Color Combination

```python
if (color1, color2) in color_mixes:
    mix = color_mixes[(color1, color2)]
elif (color2, color1) in color_mixes:
    mix = color_mixes[(color2, color1)]
```

This two-step lookup solves a real usability problem — **order independence**.

#### Why Two Checks?

The dictionary stores combinations in one specific order: `("red", "blue")`. But a user might type blue first and red second. Without the second check, `"blue"` + `"red"` would not be found even though the mix exists.

**First check:** Try the colors in the order the user entered them
```python
if (color1, color2) in color_mixes:
```

**Second check:** Try the reverse order
```python
elif (color2, color1) in color_mixes:
```

> **Important:** This makes the app **order-independent** — `"red"` + `"blue"` and `"blue"` + `"red"` both return `"purple"`. This is a small but critical UX decision. In real color mixing, order doesn't matter — the app correctly reflects that.

| User Input | Checked First | Checked Second | Found? |
|------------|--------------|----------------|--------|
| red + blue | `("red","blue")` ✅ | — | Yes |
| blue + red | `("blue","red")` ❌ | `("red","blue")` ✅ | Yes |
| red + water | `("red","water")` ❌ | `("water","red")` ❌ | No |

---

### Step 8 — Display the Result

```python
if mix:
    print(f"When you mix {color1} and {color2}, you get {mix}!")
else:
    print("I don't know what those colors make when mixed")
```

- `if mix:` evaluates to `True` when `mix` holds a color string and `False` when it is `None`
- A successful match gets a friendly, descriptive result message
- An unknown combination gets a graceful fallback message — the program never crashes on unknown input

> **Important:** `if mix:` works here because `None` is **falsy** in Python and a non-empty string is **truthy**. This is the Pythonic way to check whether an optional value was set.

---

### Step 9 — Ask to Continue

```python
if not input("\nMix more colors? (y/n): ").lower().startswith("y"):
    print("Goodbye")
    break
```

- Chains `input()` → `.lower()` → `.startswith("y")` in one line
- If the response does **not** start with `"y"`, the loop exits
- Accepts `"y"`, `"yes"`, `"yeah"`, `"yup"` — any `"y"` response continues

---

## 📊 Example Outputs

### Example 1 — Known Combination

```
COLOR MIXER

Enter first color: red
Enter second color: blue
When you mix red and blue, you get purple!

Mix more colors? (y/n): y
```

### Example 2 — Reverse Order (Order Independent)

```
Enter first color: blue
Enter second color: red
When you mix blue and red, you get purple!
```

### Example 3 — Unknown Combination

```
Enter first color: red
Enter second color: water
I don't know what those colors make when mixed

Mix more colors? (y/n): n
Goodbye
```

### Example 4 — Case and Space Handling

```
Enter first color:   RED  
Enter second color:  Blue 
When you mix red and blue, you get purple!
```

> `.lower()` handles the caps, `.strip()` removes the spaces — the lookup still works perfectly.

---

## 🧠 Concepts Practised

| Concept | Where Used |
|---------|-----------|
| Dictionaries | Storing all color mix combinations |
| Tuples as dictionary keys | Representing color pairs as immutable keys |
| `print()` | Displaying the title and results |
| `input()` | Getting color names from the user |
| `while True` | Keeping the mixer running |
| `break` | Exiting when user is done |
| `.lower()` | Case-insensitive color matching |
| `.strip()` | Removing accidental whitespace from input |
| `in` operator | Checking if a tuple exists as a dictionary key |
| `None` as a flag | Tracking whether a match was found |
| `if mix:` (truthiness) | Checking a result without `== None` |
| Method chaining | Combining `input()`, `.lower()`, `.startswith()` |
| f-strings | Embedding color names in the output message |
| Order-independent lookup | Checking both `(a,b)` and `(b,a)` in the dictionary |

---

## 👩‍💻 Author

**Pauline Oraro**
60 Days of Python Challenge — Color Mixer Project
