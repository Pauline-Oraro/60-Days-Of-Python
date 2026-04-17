# Python Exception Handling

When an error occurs — called an **exception** — Python normally stops and generates an error message. The `try` statement allows you to handle exceptions gracefully so your program can continue running.

---

## The Four Blocks

| Block | Purpose |
|-------|---------|
| `try` | Tests a block of code for errors |
| `except` | Handles the error if one occurs |
| `else` | Runs if **no** error occurred in the `try` block |
| `finally` | Runs **always**, regardless of whether an error occurred |

---

## 1. `try` and `except`

If the `try` block raises an error, the `except` block is executed instead of crashing the program.

```python
try:
    print(x)
except:
    print("An exception occurred")
# An exception occurred
```

---

## 2. Multiple `except` Blocks

You can define as many `except` blocks as you need to handle different types of errors specifically.

```python
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
# Variable x is not defined
```

> **How it works:** Python checks each `except` block from top to bottom and executes the first one that matches the error. The bare `except:` at the end acts as a catch-all fallback.

---

## 3. `else` — Run Code When No Error Occurs

The `else` block runs only if the `try` block completed **without** raising any errors.

```python
try:
    print("hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
# hello
# Nothing went wrong
```

---

## 4. `finally` — Always Runs

The `finally` block executes **regardless** of whether an error occurred or not. It is commonly used for cleanup tasks like closing files or database connections.

```python
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")
# Something went wrong
# The 'try except' is finished
```

---

## 5. Full Structure

All four blocks used together:

```python
try:
    # code to test
except NameError:
    # runs if a NameError occurs
except:
    # runs if any other error occurs
else:
    # runs if no error occurred
finally:
    # always runs
```

---

## 6. Raising Exceptions (`raise`)

You can deliberately throw an exception using the `raise` keyword — useful for enforcing rules or validating input. You can specify the type of error and a custom message.

### Raising a General Exception

```python
x = 1
if x < 0:
    raise Exception("Sorry, no numbers below zero")
```

### Raising a Specific Error Type

```python
y = "hello"
if not type(y) is int:
    raise TypeError("Only integers are allowed")
```

```
TypeError: Only integers are allowed
```

---

## Common Exception Types to Catch or Raise

| Exception | When to Use |
|-----------|-------------|
| `Exception` | General-purpose base exception |
| `NameError` | Undefined variable or function name |
| `TypeError` | Wrong data type for an operation |
| `ValueError` | Correct type but invalid value |
| `IndexError` | List index out of range |
| `KeyError` | Dictionary key not found |
| `ZeroDivisionError` | Division by zero |
| `FileNotFoundError` | File does not exist |

---

## Quick Reference

```python
try:
    print(x)                          # test this code
except NameError:
    print("x is not defined")        # handle NameError specifically
except:
    print("Something went wrong")    # handle anything else
else:
    print("No errors!")              # runs if try succeeded
finally:
    print("Always runs")             # runs no matter what

# Raise a custom exception
if not type(value) is int:
    raise TypeError("Only integers are allowed")
```
