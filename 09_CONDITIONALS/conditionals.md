# Python Conditions & If Statements

Python supports the standard logical conditions from mathematics and uses them in **if statements**, **loops**, and **expressions**.

| Condition | Symbol |
|-----------|--------|
| Equals | `==` |
| Not equals | `!=` |
| Less than | `<` |
| Less than or equal to | `<=` |
| Greater than | `>` |
| Greater than or equal to | `>=` |

---

## 1. The `if` Statement

The `if` statement evaluates a condition that results in `True` or `False`. If true, the indented block executes; if false, it is skipped.

> **Note:** Python uses **indentation** to define scope. Missing indentation will raise an error.

```python
a = 100
b = 200
if b > a:
    print("b is greater than a")

number = 15
if number > 0:
    print("The number is positive")
```

### Multiple Statements in an `if` Block

All statements inside the block must be indented at the same level.

```python
age = 20
if age >= 18:
    print("You are an adult")
    print("You can vote")
    print("You have full legal rights")
```

### Boolean Variables in `if` Statements

Boolean variables can be used directly without a comparison operator.

```python
logged_in = True
if logged_in:
    print("Welcome back to your account")
```

> **Falsy values:** `0`, empty strings `""`, `None`, and empty collections `[]`, `{}`, `()` are all treated as `False`. Everything else is `True`.

---

## 2. The `elif` Statement

`elif` ("else if") lets you check multiple conditions. Python evaluates them **top to bottom** and executes the **first matching block only** — even if multiple conditions are true.

```python
c = 44
d = 44
if d > c:
    print("d is greater than c")
elif c == d:
    print("c and d are equal")  # This runs
```

### Multiple `elif` Conditions

```python
score = 85
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")   # This runs
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
```

```python
day = 4
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")   # This runs
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
```

---

## 3. The `else` Statement

`else` is the **fallback** — it executes when none of the preceding `if` or `elif` conditions are true. It must always come **last**.

```python
e = 200
f = 100
if f > e:
    print("f is greater than e")
elif e == f:
    print("e and f are equal")
else:
    print("e is greater than f")  # This runs
```

```python
myNumber = 5
if myNumber % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")    # This runs
```

```python
temperature = 22
if temperature > 30:
    print("it is hot outside")
elif temperature > 20:
    print("it is warm outside")   # This runs
elif temperature > 10:
    print("it is cool outside")
else:
    print("it is cold outside")
```

---

## 4. Shorthand `if` (Ternary Expressions)

### One-Line `if`

```python
i = 5
j = 2
if i > j: print("i is greater than j")
```

### One-Line `if/else`

```python
k = 2
l = 350
print("k") if k > l else print("l")  # prints "l"
```

### Assign a Value Based on a Condition

```python
m = 10
n = 20
bigger = m if m > n else n
print("Bigger is", bigger)  # Bigger is 20
```

---

## 5. Logical Operators in Conditions

| Operator | Description | Returns `True` when... |
|----------|-------------|----------------------|
| `and` | Both conditions | **Both** are true |
| `or` | Either condition | **At least one** is true |
| `not` | Reverses result | The condition is **false** |

> **Evaluation order:** `not` is evaluated first, then `and`, then `or`.

```python
o, p, q = 200, 33, 500

# and
if o > p and q > o:
    print("Both conditions are true")

# or
if o > p or o > q:
    print("At least one of the conditions is true")

# not
if not p > q:
    print("p is not greater than q")
```

### Combining Multiple Logical Operators

```python
myAge = 25
is_student = False
has_discount_code = True

if (myAge < 18 or myAge > 65) and not is_student or has_discount_code:
    print("Discount applies")
```

---

## 6. Nested `if` Statements

You can place `if` statements inside other `if` statements.

```python
x = 41
if x > 10:
    print("above ten")
    if x > 20:
        print("and also above 20")
    else:
        print("but not above 20")
```

```python
studentAge = 16
has_license = True

if studentAge >= 18:
    if has_license:
        print("you can drive")
    else:
        print("You need a license")
else:
    print("you are too young to drive")  # This runs
```

---

## 7. The `pass` Statement

`if` statements cannot be empty. Use `pass` as a **placeholder** when logic hasn't been implemented yet. It is a null operation — nothing happens when it executes.

```python
z = 44
y = 200
if y > z:
    pass   # TODO: implement this later
```

**Common use cases for `pass`:**

- Placeholder during development before logic is written
- Empty functions or classes planned for later implementation
- Structuring code without triggering syntax errors

---

## 8. The `match` Statement

The `match` statement (introduced in **Python 3.10**) is a cleaner alternative to long `if/elif/else` chains. The expression is evaluated once and compared against each `case`.

Use `_` as the last case to catch anything that doesn't match — equivalent to `else`.

```python
day = 5
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")     # This runs
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
```

### `if/elif` vs `match` — When to Use Which

| Scenario | Recommended |
|----------|-------------|
| Comparing a single variable to multiple exact values | `match` |
| Complex conditions with ranges or logical operators | `if/elif` |
| Python version below 3.10 | `if/elif` |
