# 🎓 Grade Calculator — Mini Project

A command-line Python application that collects multiple test scores from the user, calculates the running average after each entry, and assigns a letter grade. The program keeps running until the user types `done`.

---

## 📋 Project Overview

| Detail | Info |
|--------|------|
| **Project Type** | Mini Project — Command Line App |
| **Difficulty** | Beginner–Intermediate |
| **Concepts Used** | `input()`, `print()`, lists, `while` loop, `break`, `float()`, `sum()`, `len()`, f-strings, `if/elif/else` |

---

## 💻 Full Code

```python
print("GRADE CALCULATOR")

scores = []

while True:
    score = input("Enter a test score (or 'done'): ")
    if score.lower() == "done":
        print("Goodbye")
        break

    scores.append(float(score))
    average = sum(scores) / len(scores)
    print(f"Average score: {average:.1f}")

    if average >= 90:
        print("Grade: A")
    elif average >= 80:
        print("Grade: B")
    elif average >= 70:
        print("Grade: C")
    else:
        print("Grade: D or F")
```

---

## 🔍 Step-by-Step Explanation

### Step 1 — Display the App Title

```python
print("GRADE CALCULATOR")
```

- Prints the application name to the terminal
- Signals to the user what the program does before any interaction begins

---

### Step 2 — Create an Empty List to Store Scores

```python
scores = []
```

- An empty **list** is created to hold all the scores the user will enter
- Lists are used here because the number of scores is unknown in advance — the user decides when to stop
- Each new score will be **appended** to this list as the program runs

> **Important:** The list is created **outside** the loop so it persists across every iteration. If it were inside the loop, it would be reset to empty every time — losing all previous scores.

---

### Step 3 — Start an Infinite Loop

```python
while True:
```

- `while True` creates an **infinite loop** — it runs forever until explicitly stopped
- This is the correct pattern when you don't know in advance how many times the loop should run
- The loop is stopped using a `break` statement when the user types `"done"`

> **Important:** Every `while True` loop **must** have a `break` condition somewhere inside it — otherwise the program will run forever and need to be force-quit.

---

### Step 4 — Get the Score Input

```python
score = input("Enter a test score (or 'done'): ")
```

- `input()` prompts the user to enter a score or type `"done"` to exit
- The result is stored as a **string** in `score`
- The prompt tells the user both options clearly — good UX design

---

### Step 5 — Check for the Exit Condition

```python
if score.lower() == "done":
    print("Goodbye")
    break
```

- `.lower()` converts the input to lowercase before comparing — so `"Done"`, `"DONE"`, `"done"` all work the same way
- If the user typed `"done"` (in any case), `"Goodbye"` is printed and `break` exits the loop
- This check happens **before** any score processing — so `"done"` is never treated as a number

> **Important:** `.lower()` is applied before the comparison to make the exit condition **case-insensitive**. Without it, typing `"Done"` or `"DONE"` would not trigger the exit and Python would try to convert it to a float — causing a crash.

---

### Step 6 — Add the Score to the List

```python
scores.append(float(score))
```

- `float(score)` converts the string input to a **floating-point number** so decimal scores like `85.5` are supported
- `.append()` adds the converted score to the end of the `scores` list
- After this line, the list grows by one item with each loop iteration

| After Entry | `scores` list |
|-------------|---------------|
| Score 1: `85` | `[85.0]` |
| Score 2: `90` | `[85.0, 90.0]` |
| Score 3: `78` | `[85.0, 90.0, 78.0]` |

> **Important:** `float()` is used instead of `int()` to support decimal scores like `92.5`. Using `int()` would truncate decimals and lose precision.

---

### Step 7 — Calculate the Running Average

```python
average = sum(scores) / len(scores)
print(f"Average score: {average:.1f}")
```

- `sum(scores)` adds up all the numbers in the list
- `len(scores)` returns the count of items in the list
- Dividing sum by count gives the **arithmetic mean (average)**
- `{average:.1f}` in the f-string formats the number to **1 decimal place**

**Example calculation after 3 scores (85, 90, 78):**
```
sum([85.0, 90.0, 78.0]) = 253.0
len([85.0, 90.0, 78.0]) = 3
average = 253.0 / 3 = 84.33...
Displayed as: 84.3
```

> **Important:** The average is recalculated **every time** a new score is added — this is called a **running average**. The user sees how their grade changes in real time after each entry.

> **Important:** `:.1f` is a **format specifier** in an f-string. The `f` means float, and `.1` means show 1 decimal place. Without it, the average would print as a long decimal like `84.33333333333333`.

---

### Step 8 — Assign and Display the Letter Grade

```python
if average >= 90:
    print("Grade: A")
elif average >= 80:
    print("Grade: B")
elif average >= 70:
    print("Grade: C")
else:
    print("Grade: D or F")
```

- Python checks each condition from top to bottom and runs the **first matching branch**
- The grading scale checks from highest to lowest — this order matters

| Average Score | Grade |
|--------------|-------|
| 90 and above | A |
| 80 – 89.9 | B |
| 70 – 79.9 | C |
| Below 70 | D or F |

> **Important:** The conditions are ordered from **highest to lowest** deliberately. If you checked `>= 70` first, a score of `95` would match it and print `"Grade: C"` — which is wrong. Always check the most restrictive condition first when using `elif` chains.

---

## 📊 Example Output

```
GRADE CALCULATOR
Enter a test score (or 'done'): 85
Average score: 85.0
Grade: B

Enter a test score (or 'done'): 92
Average score: 88.5
Grade: B

Enter a test score (or 'done'): 78
Average score: 85.0
Grade: B

Enter a test score (or 'done'): 96
Average score: 87.8
Grade: B

Enter a test score (or 'done'): done
Goodbye
```

**Behind the scenes:**
```
After score 1:  sum([85])           / 1 = 85.0
After score 2:  sum([85, 92])       / 2 = 88.5
After score 3:  sum([85, 92, 78])   / 3 = 85.0
After score 4:  sum([85, 92, 78, 96]) / 4 = 87.75 → displayed as 87.8
```

---

## 🧠 Concepts Practised

| Concept | Where Used |
|---------|-----------|
| `print()` | Displaying the title, average, and grade |
| `input()` | Getting the score or exit command |
| Lists `[]` | Storing all entered scores |
| `.append()` | Adding each new score to the list |
| `while True` | Running the loop until the user exits |
| `break` | Stopping the loop when `"done"` is entered |
| `float()` | Converting string input to a decimal number |
| `sum()` | Adding up all scores in the list |
| `len()` | Counting the number of scores |
| f-strings & `:.1f` | Formatting the average to 1 decimal place |
| `.lower()` | Making the exit check case-insensitive |
| `if/elif/else` | Assigning the correct letter grade |

---

## 👩‍💻 Author

**Pauline Oraro**
60 Days of Python Challenge — Grade Calculator Project
