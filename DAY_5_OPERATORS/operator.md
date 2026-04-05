# Python Operators

**Operators** are used to perform operations on variables and values. Python groups them into several categories.

---

## 1. Arithmetic Operators

Used with numeric values to perform common mathematical operations.

```python
valueOne = 400
valueTwo = 200
```

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `valueOne + valueTwo` | `600` |
| `-` | Subtraction | `valueOne - valueTwo` | `200` |
| `*` | Multiplication | `valueOne * valueTwo` | `80000` |
| `/` | Division | `valueOne / valueTwo` | `2.0` (always float) |
| `%` | Modulus | `valueOne % valueTwo` | `0` (remainder) |
| `**` | Exponentiation | `valueOne ** valueTwo` | `400²⁰⁰` |
| `//` | Floor Division | `valueOne // valueTwo` | `2` (integer result) |

> **Note:** `/` always returns a `float`. Use `//` when you need a whole number result.

---

## 2. Assignment Operators

Used to assign values to variables. Shorthand operators combine an arithmetic operation with assignment.

| Operator | Longhand Equivalent | Example | Result |
|----------|---------------------|---------|--------|
| `=` | — | `a = 5` | `5` |
| `+=` | `b = b + 3` | `b += 3` (b=7) | `10` |
| `-=` | `c = c - 2` | `c -= 2` (c=10) | `8` |
| `*=` | `d = d * 4` | `d *= 4` (d=3) | `12` |
| `/=` | `e = e / 2` | `e /= 2` (e=20) | `10.0` |
| `%=` | `f = f % 3` | `f %= 3` (f=10) | `1` |
| `//=` | `g = g // 2` | `g //= 2` (g=10) | `5` |
| `**=` | `h = h ** 2` | `h **= 2` (h=5) | `25` |

---

## 3. Comparison Operators

Used to compare two values. Always return a `bool` — either `True` or `False`.

```python
i = 5
j = 10
```

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `==` | Equal | `i == j` | `False` |
| `!=` | Not equal | `i != j` | `True` |
| `>` | Greater than | `i > j` | `False` |
| `<` | Less than | `i < j` | `True` |
| `>=` | Greater than or equal to | `i >= j` | `False` |
| `<=` | Less than or equal to | `i <= j` | `True` |

### Chaining Comparisons

Python allows comparison operators to be chained, making conditions more readable:

```python
k = 80
print(1 < k < 100)          # True — shorthand
print(1 < k and k < 100)    # True — equivalent longhand
```

---

## 4. Logical Operators

Used to combine conditional statements.

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `and` | Returns `True` if **both** statements are true | `l < 10 and l < 20` (l=5) | `True` |
| `or` | Returns `True` if **at least one** statement is true | `m < 10 or m < 20` (m=15) | `True` |
| `not` | Reverses the result | `not(n < 20)` (n=25) | `True` |

```python
l = 5
print(l < 10 and l < 20)  # True

m = 15
print(m < 10 or m < 20)   # True

n = 25
print(not(n < 20))         # True
print(not(n > 20))         # False
```

---

## 5. Identity Operators

Used to compare whether two variables point to the **same object in memory** — not just equal values.

```python
o = ["apples", "pineapples"]
p = ["apples", "pineapples"]
q = o
```

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `is` | `True` if both variables are the same object | `o is q` | `True` |
| `is` | `True` if both variables are the same object | `o is p` | `False` |
| `is not` | `True` if both variables are NOT the same object | `o is not p` | `True` |

> **Key distinction:** `o` and `p` hold identical values but are stored at different memory locations, so `o is p` is `False`. `q = o` makes `q` point to the exact same object as `o`, so `o is q` is `True`.

---

## 6. Membership Operators

Used to test whether a value is present in a sequence (e.g. a list, string, or tuple).

```python
r = ["apples", "pineapples"]
```

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `in` | `True` if value is present in the sequence | `"apples" in r` | `True` |
| `in` | `True` if value is present in the sequence | `"bananas" in r` | `False` |
| `not in` | `True` if value is NOT present in the sequence | `"bananas" not in r` | `True` |

---

## 7. Bitwise Operators

Used to compare numbers at the **binary (bit) level**.

| Operator | Name | Description | Example | Result |
|----------|------|-------------|---------|--------|
| `&` | AND | Sets bit to `1` if **both** bits are `1` | `6 & 3` | `2` |
| `\|` | OR | Sets bit to `1` if **either** bit is `1` | `6 \| 3` | `7` |
| `^` | XOR | Sets bit to `1` if **only one** of the bits is `1` | `6 ^ 3` | `5` |

```python
print(6 & 3)   # 2
print(6 | 3)   # 7
print(6 ^ 3)   # 5
```

> **How it works (binary):**
> - `6` = `110`, `3` = `011`
> - `&` → `010` = **2**
> - `|` → `111` = **7**
> - `^` → `101` = **5**
