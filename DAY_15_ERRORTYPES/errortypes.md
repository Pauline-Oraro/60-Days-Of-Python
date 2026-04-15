# Python Errors

When code fails to run, the Python interpreter raises an **error**. Understanding the different types of errors is an important part of becoming a proficient Python programmer.

---

## Overview

| Error Type | Caused By |
|------------|-----------|
| `SyntaxError` | Code that breaks Python's language rules |
| `NameError` | Using a variable or function that hasn't been defined |
| `IndexError` | Accessing a list index that doesn't exist |
| `ModuleNotFoundError` | Importing a module that can't be found |
| `AttributeError` | Accessing an attribute that doesn't exist on an object |
| `KeyError` | Accessing a dictionary key that doesn't exist |
| `TypeError` | Performing an operation on incompatible data types |
| `ImportError` | Failing to import a name from a module |
| `ValueError` | Passing a value that is the wrong type for an operation |
| `ZeroDivisionError` | Dividing a number by zero |

---

## 1. SyntaxError

Occurs when code does not follow the rules of the Python language — such as a missing parenthesis, missing colon, or misspelled keyword.

```python
# Missing closing parenthesis — raises SyntaxError
print("pauline"
```

```
SyntaxError: '(' was never closed
```

---

## 2. NameError

Occurs when a variable or function name is used that has not been defined. Usually caused by a typo or using a variable before assigning it a value.

```python
# 'age' has never been defined — raises NameError
print(age)
```

```
NameError: name 'age' is not defined
```

---

## 3. IndexError

Occurs when trying to access an index that is out of range for a list or other sequence.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[3])  # valid indexes are 0, 1, 2 — raises IndexError
```

```
IndexError: list index out of range
```

> **Reminder:** List indexes start at `0`, so a list with 3 items has valid indexes `0`, `1`, and `2` only.

---

## 4. ModuleNotFoundError

Occurs when the Python interpreter cannot find a module being imported — usually due to a typo in the module name or the module not being installed.

```python
# 'maths' does not exist — the correct module is 'math'
import maths
print(maths.pi)
```

```
ModuleNotFoundError: No module named 'maths'
```

---

## 5. AttributeError

Occurs when trying to access an attribute or method that does not exist on an object.

```python
class Person:
    def __init__(self, name):
        self.name = name

person = Person("Alice")
print(person.name)  # Alice — works fine

# 'age' was never defined on the Person class — raises AttributeError
print(person.age)
```

```
AttributeError: 'Person' object has no attribute 'age'
```

---

## 6. KeyError

Occurs when trying to access a dictionary key that does not exist.

```python
my_dict = {"name": "Alice", "age": 30}
print(my_dict["name"])    # Alice — works fine

# "gender" is not a key in the dictionary — raises KeyError
print(my_dict["gender"])
```

```
KeyError: 'gender'
```

> **Tip:** Use `.get()` to safely access a key without raising an error — it returns `None` if the key doesn't exist: `my_dict.get("gender")`.

---

## 7. TypeError

Occurs when an operation is attempted on incompatible data types.

```python
# Cannot add an integer and a string — raises TypeError
print(4 + "5")
```

```
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

> **Fix:** Convert to a matching type first — `print(4 + int("5"))` or `print(str(4) + "5")`.

---

## 8. ImportError

Occurs when Python finds the module but cannot import the specific name or function requested from it.

```python
# 'mathh' does not exist — raises ImportError
import mathh
print(mathh.pi)
```

```
ModuleNotFoundError: No module named 'mathh'
```

> **Note:** `ModuleNotFoundError` is a subclass of `ImportError`. You'll see `ImportError` specifically when a module exists but the item being imported from it does not.

---

## 9. ValueError

Occurs when a function receives an argument of the correct type but with an invalid value.

```python
# "hello" cannot be converted to an integer — raises ValueError
print(int("hello"))
```

```
ValueError: invalid literal for int() with base 10: 'hello'
```

> **Valid example:** `int("42")` works fine because `"42"` is a valid integer in string form.

---

## 10. ZeroDivisionError

Occurs when a number is divided by zero.

```python
# Cannot divide by zero — raises ZeroDivisionError
print(5 / 0)
```

```
ZeroDivisionError: division by zero
```

---

## Quick Tips for Debugging Errors

- **Read the error message carefully** — Python tells you exactly what went wrong and on which line.
- **Check for typos** — most `NameError`, `KeyError`, and `ModuleNotFoundError` come down to spelling.
- **Check your indexes** — remember lists start at `0`.
- **Check data types** — `TypeError` and `ValueError` often mean you need to convert a value first.
- **Use `.get()` on dictionaries** — avoids `KeyError` when you're unsure a key exists.
