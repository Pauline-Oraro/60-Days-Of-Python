# Python `range()`

The built-in `range()` function returns an **immutable sequence of numbers**, commonly used for looping a specific number of times. The sequence has its own data type called `range`.

> **Note:** A `range` object is not directly displayable. It is often converted to a list using `list()` for display purposes.

---

## 1. Syntax

```python
range(start, stop, step)
```

| Argument | Required | Description | Default |
|----------|----------|-------------|---------|
| `stop` | Yes | The sequence ends **before** this value | — |
| `start` | No | Where the sequence begins | `0` |
| `step` | No | The difference between each number | `1` |

---

## 2. One Argument — `range(stop)`

The single argument represents the **stop** value. The sequence starts at `0` by default.

```python
first_range = range(10)
print(first_range)        # range(0, 10)
print(list(first_range))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## 3. Two Arguments — `range(start, stop)`

The first argument is the **start** value and the second is the **stop** value.

```python
second_range = range(1, 10)
print(second_range)        # range(1, 10)
print(list(second_range))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## 4. Three Arguments — `range(start, stop, step)`

The third argument is the **step** value — the difference between each number in the sequence.

```python
third_range = range(1, 10, 2)
print(third_range)        # range(1, 10, 2)
print(list(third_range))  # [1, 3, 5, 7, 9]
```

---

## 5. Using `range()` in `for` Loops

Ranges are most commonly used in `for` loops to iterate over a sequence of numbers.

```python
for i in range(10):
    print(i)
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```

---

## 6. Slicing a Range

Ranges can be sliced to extract a subsequence, just like lists.

```python
sliced_range = range(10)

print(sliced_range[2])    # 2       (single item at index 2)
print(sliced_range[2:5])  # range(2, 5)  (items at index 2, 3, 4)
print(sliced_range[:3])   # range(0, 3)  (first 3 items)
```

---

## 7. Membership Testing (`in`)

Use the `in` operator to check if a number is present in a range — much faster than checking a list.

```python
fourth_range = range(0, 10, 2)  # [0, 2, 4, 6, 8]

print(5 in fourth_range)  # False
print(6 in fourth_range)  # True
print(7 in fourth_range)  # False
print(8 in fourth_range)  # True
```

---

## 8. Getting the Length (`len()`)

Use `len()` to get the total number of elements in a range.

```python
print(len(fourth_range))  # 5  (0, 2, 4, 6, 8)
```

---

## Quick Reference

| Syntax | Example | Result |
|--------|---------|--------|
| `range(stop)` | `range(5)` | `[0, 1, 2, 3, 4]` |
| `range(start, stop)` | `range(2, 6)` | `[2, 3, 4, 5]` |
| `range(start, stop, step)` | `range(1, 10, 2)` | `[1, 3, 5, 7, 9]` |
| `len(range)` | `len(range(0, 10, 2))` | `5` |
| `x in range` | `6 in range(0, 10, 2)` | `True` |
| `range[i]` | `range(10)[3]` | `3` |
| `list(range)` | `list(range(4))` | `[0, 1, 2, 3]` |
