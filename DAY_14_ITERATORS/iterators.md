# Python Iterators

An **iterator** is an object that contains a countable number of values and can be traversed through one value at a time.

In Python, an iterator implements the **iterator protocol** which consists of two methods:

| Method | Description |
|--------|-------------|
| `__iter__()` | Returns the iterator object itself |
| `__next__()` | Returns the next value in the sequence |

---

## 1. Iterable Objects

Lists, tuples, dictionaries, strings, and sets are all **iterable objects** — meaning you can get an iterator from them using the built-in `iter()` function.

> **Iterable** = an object you *can* loop over.  
> **Iterator** = the object that *does* the looping, one step at a time.

---

## 2. Using `iter()` and `next()`

Use `iter()` to create an iterator from an iterable, then use `next()` to retrieve values one at a time.

### Iterating a Tuple

```python
mytuple = ("kate", "mercedes", "hailey")
myit = iter(mytuple)

print(next(myit))  # kate
print(next(myit))  # mercedes
print(next(myit))  # hailey
```

### Iterating a String

Strings are iterable — each character is a value in the sequence.

```python
mystring = "pauline"
myit = iter(mystring)

print(next(myit))  # p
print(next(myit))  # a
print(next(myit))  # u
print(next(myit))  # l
print(next(myit))  # i
print(next(myit))  # n
print(next(myit))  # e
```

> **Note:** Calling `next()` after all values have been returned will raise a `StopIteration` exception.

---

## 3. Looping Through an Iterable with `for`

The `for` loop handles iteration automatically — it calls `iter()` to create the iterator and `next()` on each loop cycle behind the scenes.

### Iterating a List

```python
my_grocery_list = ["milk", "eggs", "bread", "butter", "cheese"]

for x in my_grocery_list:
    print(x)
# milk
# eggs
# bread
# butter
# cheese
```

### Iterating a String

```python
my_name = "Oraro"

for y in my_name:
    print(y)
# O
# r
# a
# r
# o
```

---

## `iter()` + `next()` vs `for` Loop

| | `iter()` + `next()` | `for` loop |
|-|---------------------|-----------|
| **Control** | Manual — one value at a time | Automatic — all values |
| **Use case** | When you need fine-grained control over iteration | When you want to loop through all values simply |
| **StopIteration** | Must handle manually | Handled automatically |
| **Code length** | More verbose | More concise |
