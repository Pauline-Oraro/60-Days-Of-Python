# 👟 Step Counter — Mini Project

A simple command-line Python application that helps users track their daily step progress. The user enters their daily step goal and the steps taken so far, and the app calculates whether they've reached their goal or how many steps remain.

---

---

## 💻 Full Code

```python
print("STEP COUNTER")

daily_goal = int(input("What is your daily step goal? "))
current_steps = int(input("How many steps have you taken today? "))

remaining_steps = daily_goal - current_steps

if remaining_steps > 0:
    print(f"You need {remaining_steps} more steps to reach your goal!")
else:
    print(f"Congratulations! You have exceeded your goal by {-remaining_steps} steps!")
```

---

## 🔍 Step-by-Step Explanation

### Step 1 — Display the App Title

```python
print("STEP COUNTER")
```

- The first thing the program does is print a title to the terminal
- This is a simple UX touch that tells the user what the application does before it asks for any input
- **Good practice:** Always label your CLI apps clearly so users know what they're interacting with

---

### Step 2 — Get the Daily Step Goal

```python
daily_goal = int(input("What is your daily step goal? "))
```

- `input()` pauses the program and waits for the user to type something and press **Enter**
- `input()` always returns a **string** by default — even if the user types a number
- `int()` converts the string to an **integer** so we can do math with it
- The result is stored in the variable `daily_goal`

> **Important:** If the user types something that is not a number (e.g. `"hello"`), the program will crash with a `ValueError`. In a production app you would wrap this in a `try/except` block to handle invalid input gracefully.

---

### Step 3 — Get the Current Steps Taken

```python
current_steps = int(input("How many steps have you taken today? "))
```

- Same pattern as Step 2 — `input()` gets the value, `int()` converts it
- Stored in the variable `current_steps`
- This represents how many steps the user has actually walked so far today

---

### Step 4 — Calculate Remaining Steps

```python
remaining_steps = daily_goal - current_steps
```

- Subtracts `current_steps` from `daily_goal`
- The result is stored in `remaining_steps`
- This value can be **positive** (goal not yet reached), **zero** (goal exactly met), or **negative** (goal exceeded)

| Scenario | `remaining_steps` value |
|----------|------------------------|
| Goal not reached | Positive number (e.g. `2500`) |
| Goal exactly met | `0` |
| Goal exceeded | Negative number (e.g. `-2000`) |

> **Important:** The sign of `remaining_steps` is what drives the logic in the next step. A negative result means the user has gone **beyond** their goal.

---

### Step 5 — Display the Result

```python
if remaining_steps > 0:
    print(f"You need {remaining_steps} more steps to reach your goal!")
else:
    print(f"Congratulations! You have exceeded your goal by {-remaining_steps} steps!")
```

#### The `if` Branch — Goal Not Yet Reached

```python
if remaining_steps > 0:
    print(f"You need {remaining_steps} more steps to reach your goal!")
```

- Runs when the user still has steps left to walk
- Uses an **f-string** to insert the `remaining_steps` value directly into the message

#### The `else` Branch — Goal Met or Exceeded

```python
else:
    print(f"Congratulations! You have exceeded your goal by {-remaining_steps} steps!")
```

- Runs when `remaining_steps` is `0` or **negative**
- `-remaining_steps` converts the negative number to a positive one for clean display
- For example: if `remaining_steps = -2000`, then `-remaining_steps = 2000`

> **Important:** The `-` before `remaining_steps` in the `else` branch is a **negation operator**, not subtraction. It flips the sign of the number — turning a negative into a positive — so the output message makes sense to the user.

---

## 📊 Example Outputs

### Example 1 — Goal Not Reached

```
STEP COUNTER
What is your daily step goal? 10000
How many steps have you taken today? 7500
You need 2500 more steps to reach your goal!
```

**Behind the scenes:**
```
remaining_steps = 10000 - 7500 = 2500
2500 > 0 → True → first branch runs
```

---

### Example 2 — Goal Exceeded

```
STEP COUNTER
What is your daily step goal? 10000
How many steps have you taken today? 12000
Congratulations! You have exceeded your goal by 2000 steps!
```

**Behind the scenes:**
```
remaining_steps = 10000 - 12000 = -2000
-2000 > 0 → False → else branch runs
-(-2000) = 2000 → displayed to user
```

---

### Example 3 — Goal Exactly Met

```
STEP COUNTER
What is your daily step goal? 10000
How many steps have you taken today? 10000
Congratulations! You have exceeded your goal by 0 steps!
```

**Behind the scenes:**
```
remaining_steps = 10000 - 10000 = 0
0 > 0 → False → else branch runs
```

> **Note:** When the goal is exactly met, the `else` branch runs and displays `0 steps`. You could improve this by adding an `elif remaining_steps == 0` branch with a dedicated message like *"Perfect! You hit your goal exactly!"*

---

---

## 🧠 Concepts Practised

| Concept | Where Used |
|---------|-----------|
| `print()` | Displaying output to the user |
| `input()` | Reading user input from the terminal |
| `int()` | Converting string input to an integer |
| Variables | Storing `daily_goal`, `current_steps`, `remaining_steps` |
| Arithmetic (`-`) | Calculating remaining steps |
| Negation (`-variable`) | Converting negative to positive for display |
| `if/else` | Choosing which message to show |
| f-strings | Embedding variables inside printed messages |

---

## 👩‍💻 Author

**Pauline Oraro**
60 Days of Python Challenge — Step Counter Project
