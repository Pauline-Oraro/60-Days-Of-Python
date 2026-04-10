# Python Loops

Python has two primitive loop commands: **`while` loops** and **`for` loops**.

---

## 1. While Loop

Executes a set of statements **as long as a condition is true**. The loop requires a relevant variable to be defined beforehand — typically an indexing variable.

```python
i = 1
while i < 6:
    print(i)
    i += 1
# prints 1, 2, 3, 4, 5
```

> **Important:** Always remember to increment the variable inside the loop, otherwise the loop will run forever (infinite loop).

---

### `break` — Stop the Loop Early

Stops the loop even if the `while` condition is still true.

```python
i = 1
while i < 6:
    print(i)
    if i == 3:
        break   # stops when i reaches 3
    i += 1
# prints 1, 2, 3
```

---

### `continue` — Skip to the Next Iteration

Stops the **current** iteration and jumps to the next one.

```python
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue   # skips printing 3
    print(i)
# prints 1, 2, 4, 5, 6
```

---

### `else` — Run Code When Condition Becomes False

The `else` block runs **once** when the while condition is no longer true.

```python
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
# prints 1, 2, 3, 4, 5 then "i is no longer less than 6"
```

---

## 2. For Loop

Used for iterating over a **sequence** — a list, tuple, dictionary, set, or string.

```python
fruits = ["apple", "banana", "kiwi"]
for x in fruits:
    print(x)
# apple
# banana
# kiwi
```

### Iterating Over a String

Strings are iterable objects containing a sequence of characters.

```python
for x in "watermelon":
    print(x)
# w, a, t, e, r, m, e, l, o, n (each on a new line)
```

---

### `break` — Stop Before Looping All Items

```python
vegetables = ["broccoli", "kales", "spinach"]

# break after printing the matched item
for y in vegetables:
    print(y)
    if y == "kales":
        break
# broccoli, kales

# break before printing the matched item
for z in vegetables:
    if z == "kales":
        break
    print(z)
# broccoli
```

---

### `continue` — Skip an Item

```python
for x in vegetables:
    if x == "kales":
        continue   # skips "kales"
    print(x)
# broccoli, spinach
```

---

### The `range()` Function

Used to loop through a set of code a specified number of times. Returns a sequence of numbers starting at `0` by default, incrementing by `1`.

| Syntax | Description |
|--------|-------------|
| `range(stop)` | `0` up to (not including) `stop` |
| `range(start, stop)` | `start` up to (not including) `stop` |
| `range(start, stop, step)` | `start` to `stop` with custom increment |

```python
# Default — starts at 0
for a in range(7):
    print(a)
# 0, 1, 2, 3, 4, 5, 6

# With a start value
for b in range(3, 6):
    print(b)
# 3, 4, 5

# With a custom step/increment
for c in range(2, 30, 4):
    print(c)
# 2, 6, 10, 14, 18, 22, 26
```

---

### `else` — Run Code When Loop Finishes

The `else` block runs once after the loop completes all its iterations.

```python
for d in range(7):
    print(d)
else:
    print("Finally finished!")
# 0, 1, 2, 3, 4, 5, 6
# Finally finished!
```

---

### Nested Loops

A loop inside a loop. The **inner loop** executes fully for **each iteration** of the outer loop.

```python
color  = ["red", "yellow", "blue"]
fruits = ["apple", "banana", "blueberries"]

for e in color:
    for f in fruits:
        print(e, f)
# red apple
# red banana
# red blueberries
# yellow apple
# yellow banana
# ...and so on
```

---

### `pass` — Empty Loop Placeholder

`for` loops cannot be empty. Use `pass` to avoid a syntax error when the loop body hasn't been implemented yet.

```python
for x in [0, 1, 2, 3]:
    pass   # TODO: implement later
```

---

## Quick Reference

| Statement | `while` Loop | `for` Loop |
|-----------|-------------|-----------|
| `break` | Stops the loop early | Stops the loop early |
| `continue` | Skips current iteration | Skips current iteration |
| `else` | Runs when condition becomes false | Runs when all iterations complete |
| `pass` | Prevents empty loop error | Prevents empty loop error |
