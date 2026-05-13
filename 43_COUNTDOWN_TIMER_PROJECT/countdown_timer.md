# Countdown Timer in Python

A simple Python countdown timer project that counts down from a user-defined number of seconds to zero.

This beginner-friendly project demonstrates:

- Loops
- User input
- Exception handling
- Time delays
- Conditional statements

---

# Features

- Countdown from any number of seconds
- Real-time countdown display
- Input validation
- Restart option
- Beginner-friendly structure

---

# Python Concepts Used

This project helps practice:

- `while` loops
- `for` loops
- `try-except` blocks
- User input handling
- The `time` module
- Conditional statements

---

# Source Code

```python
import time

print("\n=== COUNTDOWN TIMER ====")
print("Count down from your chosen seconds!")

while True:
    try:
        seconds = int(input("\nEnter seconds to countdown from: "))

        if seconds <= 0:
            print("Please enter a positive number.")
            continue

        print(f"Starting countdown from {seconds} seconds!")

        for i in range(seconds, 0, -1):
            print(f"{i} seconds remaining...")
            time.sleep(1)

        print("\nCOUNTDOWN COMPLETE!")

        again = input("\nStart another countdown? (yes/no): ").lower()

        if not again.startswith("y"):
            print("Goodbye!")
            break

    except ValueError:
        print("Please enter a number.")
```

---

# How the Program Works

## 1. Importing the Time Module

```python
import time
```

The `time` module allows the program to pause execution using:

```python
time.sleep(1)
```

This creates the 1-second delay between countdown numbers.

---

# 2. Displaying the Welcome Message

```python
print("\n=== COUNTDOWN TIMER ====")
```

This introduces the countdown timer to the user.

---

# 3. Taking User Input

```python
seconds = int(input("\nEnter seconds to countdown from: "))
```

The user enters the number of seconds to count down from.

Example:

```text
10
```

---

# 4. Input Validation

```python
if seconds <= 0:
```

The program ensures the user enters a positive number.

Invalid examples:

```text
0
-5
```

---

# 5. Countdown Logic

```python
for i in range(seconds, 0, -1):
```

The loop:

- Starts from the entered number
- Counts backward to 1
- Decreases by 1 each time

Example:

```python
10, 9, 8, 7...
```

---

# 6. Delaying Each Second

```python
time.sleep(1)
```

Pauses the program for one second before continuing.

Without this line, the countdown would finish instantly.

---

# 7. Exception Handling

```python
except ValueError:
```

Prevents crashes if the user enters text instead of a number.

Example invalid inputs:

```text
hello
abc
@
```

---

# Example Output

```text
=== COUNTDOWN TIMER ====
Count down from your chosen seconds!

Enter seconds to countdown from: 5

Starting countdown from 5 seconds!

5 seconds remaining...
4 seconds remaining...
3 seconds remaining...
2 seconds remaining...
1 seconds remaining...

COUNTDOWN COMPLETE!
```

---

# Restart Feature

After the countdown finishes, the user can start another countdown.

```python
again = input("\nStart another countdown? (yes/no): ").lower()
```

If the answer starts with `"y"`:

```text
yes
y
yeah
```

The timer restarts.

Otherwise, the program exits.

---

# Beginner Challenge Ideas

Try modifying the project to:

1. Add a stopwatch mode
2. Display time in `MM:SS` format
3. Add background music
4. Save countdown history
5. Create a Pomodoro timer

---

# How to Run the Program

## Step 1: Install Python

Download Python from:

- https://www.python.org/

---

## Step 2: Save the File

Save the code as:

```text
main.py
```

---

## Step 3: Run the Program

Open the terminal and run:

```bash
python main.py
```

Or:

```bash
python3 main.py
```

---

# Skills You Gain From This Project

By building this project, you practice:

- Writing loops
- Managing program flow
- Handling errors
- Working with time delays
- Building interactive terminal programs

---

# Conclusion

This Countdown Timer project is a great beginner Python exercise for learning loops, timing, and user interaction.

It is simple, practical, and forms a strong foundation for more advanced timer and clock applications.

Happy Coding 🚀
