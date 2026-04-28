# Python Modules

A **module** is a file containing a set of functions and variables you want to include in your application. Modules help organise code and make it reusable across different programs.

---

## 1. Creating a Module

To create a module, save your code in a file with the `.py` extension.

For example, a file named `module.py` might contain:

```python
# module.py

def greeting(name):
    print("Hello,", name)

person1 = {
    "name": "Pauline",
    "age": 20,
    "country": "Kenya"
}
```

> Modules can contain **functions**, **variables**, **classes**, and any other valid Python code.

---

## 2. Importing a Module

Use the `import` statement to use a module in your application.

```python
import module

module.greeting("Pauline")   # Hello, Pauline
```

### Accessing Variables from a Module

```python
a = module.person1["age"]
print(a)   # 20
```

---

## 3. Creating an Alias (`as`)

You can give a module a shorter name using the `as` keyword when importing.

```python
import module as md

name = md.person1["name"]
print(name)   # Pauline
```

> Aliases are especially useful for modules with long names (e.g. `import numpy as np`).

---

## 4. Built-in Modules

Python comes with several built-in modules that you can import at any time without installing anything.

```python
import platform

x = platform.system()
print(x)   # e.g. Windows, Linux, or Darwin (macOS)
```

### Common Built-in Modules

| Module | Description |
|--------|-------------|
| `platform` | Access system and platform information |
| `math` | Mathematical functions (`sqrt`, `pi`, etc.) |
| `random` | Generate random numbers |
| `datetime` | Work with dates and times |
| `os` | Interact with the operating system |
| `sys` | System-specific parameters and functions |
| `json` | Parse and write JSON data |

---

## 5. The `dir()` Function

The built-in `dir()` function lists all function names and variable names available in a module.

```python
import platform

y = dir(platform)
print(y)
# ['DEV_NULL', '_UNIXCONFDIR', '__builtins__', ..., 'system', 'uname', 'version', ...]
```

> This is handy for exploring an unfamiliar module and discovering what it offers.

---

## 6. Importing Specific Items (`from`)

Use the `from` keyword to import only a specific part of a module instead of the whole thing.

```python
from module import person1

print(person1["country"])   # Kenya
```

> When using `from`, you access the imported item **directly** by name — no need for the `module.` prefix.

---

## Quick Reference

| Syntax | Description | Example |
|--------|-------------|---------|
| `import module` | Import the whole module | `import platform` |
| `import module as alias` | Import with a shorter alias | `import module as md` |
| `from module import item` | Import a specific item only | `from module import person1` |
| `dir(module)` | List all names in a module | `dir(platform)` |
| `module.function()` | Call a function from a module | `module.greeting("Pauline")` |
| `module.variable` | Access a variable from a module | `module.person1["age"]` |
