# Number Guessing Game in Python

A beginner-friendly Python project where the computer randomly selects a number between **1 and 100**, and the player has **10 attempts** to guess it correctly.

---

# Features

- Random number generation
- User input handling
- Error handling using `try-except`
- Limited attempts system
- Hints for high and low guesses
- Replay option
- Beginner-friendly Python concepts

---

# Python Concepts Used

This project helps practice:

- Variables
- Loops (`while`)
- Conditional statements (`if`, `elif`, `else`)
- Functions from Python modules
- Exception handling
- User input
- Boolean flags

---

# Source Code

```python
import random

print("Welcome to the Number Guessing Game")
print("I am thinking of a number between 1 and 100. You have 10 attempts.")

playing = True

while playing:
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    game_over = False

    while attempts < max_attempts and not game_over:
        try:
            guess = int(
                input(f"Attempt {attempts + 1}/{max_attempts}. Enter your guess: ")
            )
        except ValueError:
            print("Please enter a valid number")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try a higher number!")

        elif guess > secret_number:
            print("Too high! Try a lower number!")

        else:
            print(
                f"Congrats, you guessed the number {secret_number} in {attempts} attempts"
            )
            game_over = True

        if attempts < max_attempts and not game_over:
            print(f"You have {max_attempts - attempts} attempts left!")

    if not game_over:
        print(f"Game over! The number was {secret_number}")

    play_again = input("Would you like to play again? (yes/no): ").lower()

    if play_again.startswith("y"):
        print("New game starting....\n")

    else:
        print("Goodbye")
        playing = False
```

---

# How the Program Works

## 1. Importing the Random Module

```python
import random
```

The `random` module allows Python to generate random numbers.

---

## 2. Displaying Welcome Messages

```python
print("Welcome to the Number Guessing Game")
```

These messages introduce the player to the game.

---

## 3. Generating the Secret Number

```python
secret_number = random.randint(1, 100)
```

This generates a random integer between **1 and 100**.

Example:

```python
57
```

---

## 4. Tracking Attempts

```python
attempts = 0
max_attempts = 10
```

- `attempts` keeps count of guesses
- `max_attempts` limits the player to 10 tries

---

## 5. Taking User Input

```python
guess = int(input("Enter your guess: "))
```

The player enters a number, which is converted into an integer.

---

## 6. Error Handling

```python
except ValueError:
```

Prevents the program from crashing if the user enters text instead of a number.

Example invalid input:

```text
hello
abc
@
```

---

## 7. Comparing the Guess

### Too Low

```python
if guess < secret_number:
```

### Too High

```python
elif guess > secret_number:
```

### Correct Guess

```python
else:
```

The game checks whether the guess is:

- Lower than the secret number
- Higher than the secret number
- Exactly correct

---

# Example Gameplay

```text
Welcome to the Number Guessing Game
I am thinking of a number between 1 and 100. You have 10 attempts.

Attempt 1/10. Enter your guess: 50
Too low! Try a higher number!
You have 9 attempts left!

Attempt 2/10. Enter your guess: 75
Too high! Try a lower number!
You have 8 attempts left!

Attempt 3/10. Enter your guess: 63
Congrats, you guessed the number 63 in 3 attempts
```

---

# Replay System

After the game ends, the player can choose to play again.

```python
play_again = input("Would you like to play again? (yes/no): ").lower()
```

If the answer starts with `"y"`:

```python
yes
y
yeah
yep
```

The game restarts.

---

# Skills You Gain From This Project

By completing this project, you practice:

- Python syntax
- Problem solving
- Game logic
- Input validation
- Loops and conditions
- Error handling

---

# Conclusion

This Number Guessing Game is an excellent beginner Python project that teaches important programming fundamentals while being fun and interactive.

It is a great project for improving logic-building and understanding how Python programs flow from start to finish.

Happy Coding
