# 🧙 Fantasy Name Generator — Mini Project

A command-line Python application that generates unique fantasy character names by randomly combining prefixes and suffixes. The user chooses how many names to generate, and the program produces them instantly.

---

## 📋 Project Overview

| Detail | Info |
|--------|------|
| **Project Type** | Mini Project — Command Line App |
| **Difficulty** | Beginner |
| **Concepts Used** | `import random`, lists, `input()`, `int()`, `for` loop, `range()`, `random.choice()`, f-strings |

---

## 💻 Full Code

```python
import random

first_parts = ["Sky", "Star", "Moon", "Sun", "Fire", "Ice"]
last_parts  = ["rider", "walker", "hunter", "seeker", "dancer", "keeper", "singer"]

print("FANTASY NAME GENERATOR")

count = int(input("How many names do you want? "))

for _ in range(count):
    first_name = random.choice(first_parts)
    last_name  = random.choice(last_parts)
    print(f"{first_name}{last_name}")
```

---

## 🔍 Step-by-Step Explanation

### Step 1 — Import the `random` Module

```python
import random
```

- The `random` module is a Python **built-in** — no installation needed
- It must be imported at the **very top** of the file before any code that uses it
- Here it powers `random.choice()` which selects a random item from a list

> **Important:** Always place `import` statements at the top of your file. Python reads top to bottom — using `random.choice()` before importing `random` will raise a `NameError`.

---

### Step 2 — Define the Name Parts

```python
first_parts = ["Sky", "Star", "Moon", "Sun", "Fire", "Ice"]
last_parts  = ["rider", "walker", "hunter", "seeker", "dancer", "keeper", "singer"]
```

- Two **lists** store the building blocks of each fantasy name
- `first_parts` contains **prefixes** — evocative nature and element words
- `last_parts` contains **suffixes** — action and role words
- These lists are defined **outside** the loop so they are created once and reused on every iteration

| List | Items | Count |
|------|-------|-------|
| `first_parts` | `"Sky"`, `"Star"`, `"Moon"`, `"Sun"`, `"Fire"`, `"Ice"` | 6 |
| `last_parts` | `"rider"`, `"walker"`, `"hunter"`, `"seeker"`, `"dancer"`, `"keeper"`, `"singer"` | 7 |

> **Important:** With 6 first parts and 7 last parts, the generator can produce **6 × 7 = 42 unique combinations**. Adding more words to either list multiplies the possibilities — 10 first parts and 10 last parts gives 100 combinations.

---

### Step 3 — Display the App Title

```python
print("FANTASY NAME GENERATOR")
```

- Prints the application name to the terminal before any interaction
- Sets the tone and tells the user what the program does

---

### Step 4 — Get the Number of Names

```python
count = int(input("How many names do you want? "))
```

- `input()` pauses the program and waits for the user to type a number
- `input()` always returns a **string** — `int()` converts it to an integer so it can be used in `range()`
- The result is stored in `count`

> **Important:** If the user types something that is not a number (e.g. `"five"`), `int()` will raise a `ValueError` and crash the program. In a production app you would wrap this in a `try/except` block to handle invalid input gracefully.

---

### Step 5 — Loop and Generate Names

```python
for _ in range(count):
    first_name = random.choice(first_parts)
    last_name  = random.choice(last_parts)
    print(f"{first_name}{last_name}")
```

#### The `for` Loop with `range()`

```python
for _ in range(count):
```

- `range(count)` generates a sequence of numbers from `0` to `count - 1`
- The loop runs exactly `count` times — once for each name the user requested
- `_` is used as the loop variable instead of `i` or `x` because the loop variable itself is **never used** inside the loop — we only need the loop to run a certain number of times

> **Important:** Using `_` as a variable name is a Python convention that signals to other developers "I need this loop to run N times, but I don't actually need the loop counter value." It makes the intent of the code clearer.

#### Picking a Random First Part

```python
first_name = random.choice(first_parts)
```

- `random.choice()` picks **one random item** from the `first_parts` list
- Each item has an equal probability of being selected — `1 in 6` chance
- A different item may be chosen on every loop iteration

#### Picking a Random Last Part

```python
last_name = random.choice(last_parts)
```

- Same as above but from the `last_parts` list
- Each item has a `1 in 7` chance of being selected
- The choice is **independent** of `first_name` — any combination is possible

#### Printing the Generated Name

```python
print(f"{first_name}{last_name}")
```

- The f-string joins `first_name` and `last_name` **directly** with no space or separator between them
- This creates compound words like `"Starwalker"`, `"Moonhunter"`, `"Icekeeper"`
- One name is printed per loop iteration

> **Important:** There is **no space** between `{first_name}` and `{last_name}` in the f-string. This is intentional — fantasy names are typically one joined compound word. Adding a space would produce `"Star walker"` instead of `"Starwalker"`.

---

## 📊 How the Name Generation Works

```
first_parts = ["Sky", "Star", "Moon", "Sun", "Fire", "Ice"]
last_parts  = ["rider", "walker", "hunter", "seeker", "dancer", "keeper", "singer"]

random.choice(first_parts) → "Moon"
random.choice(last_parts)  → "dancer"
f"{first_name}{last_name}" → "Moondancer"
```

### All 42 Possible Combinations

|  | rider | walker | hunter | seeker | dancer | keeper | singer |
|--|-------|--------|--------|--------|--------|--------|--------|
| **Sky** | Skyrider | Skywalker | Skyhunter | Skyseeker | Skydancer | Skykeeper | Skysinger |
| **Star** | Starrider | Starwalker | Starhunter | Starseeker | Stardancer | Starkeeper | Starsinger |
| **Moon** | Moonrider | Moonwalker | Moonhunter | Moonseeker | Moondancer | Moonkeeper | Moonsinger |
| **Sun** | Sunrider | Sunwalker | Sunhunter | Sunseeker | Sundancer | Sunkeeper | Sunsinger |
| **Fire** | Firerider | Firewalker | Firehunter | Fireseeker | Firedancer | Firekeeper | Firesinger |
| **Ice** | Icerider | Icewalker | Icehunter | Iceseeker | Icedancer | Icekeeper | Icesinger |

---

## 📊 Example Outputs

### Example 1 — 3 Names

```
FANTASY NAME GENERATOR
How many names do you want? 3
Starwalker
Moonhunter
Icekeeper
```

### Example 2 — 5 Names

```
FANTASY NAME GENERATOR
How many names do you want? 5
Sunseeker
Skydancer
Firerider
Moonwalker
Starsinger
```

### Example 3 — Same Name Twice (Possible)

```
FANTASY NAME GENERATOR
How many names do you want? 4
Skywalker
Icekeeper
Skywalker
Moondancer
```

---

## 🧠 Concepts Practised

| Concept | Where Used |
|---------|-----------|
| `import random` | Importing the random module |
| Lists | Storing the name prefixes and suffixes |
| `print()` | Displaying the title and generated names |
| `input()` | Getting the desired number of names |
| `int()` | Converting string input to an integer |
| `for` loop | Repeating the name generation `count` times |
| `range()` | Generating the loop's iteration count |
| `_` variable | Signalling the loop counter is unused |
| `random.choice()` | Picking a random item from a list |
| f-strings | Joining the two name parts into one word |

---

## 👩‍💻 Author

**Pauline Oraro**
60 Days of Python Challenge — Random Name Generator Project
