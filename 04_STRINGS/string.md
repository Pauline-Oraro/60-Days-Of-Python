# Python Strings

A **string** in Python is a sequence of Unicode characters enclosed in single or double quotation marks. `'hello'` and `"hello"` are identical.

---

## 1. Assigning Strings

```python
a = "string"
print(a)  # string
```

---

## 2. Multiline Strings

Assign a multiline string using triple quotes (`"""` or `'''`).

```python
b = """lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud 
exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."""
print(b)
```

---

## 3. Strings as Arrays

Strings are arrays of Unicode characters. Python has no separate character type — a single character is just a string of length 1. Use square brackets `[]` to access individual characters.

```python
c = "Hello world"
print(c[1])  # e
```

---

## 4. Looping Through a String

Use a `for` loop to iterate over each character in a string.

```python
for y in "banana":
    print(y)
# b
# a
# n
# a
# n
# a
```

---

## 5. String Length

Use the built-in `len()` function to get the length of a string.

```python
l = "python"
print(len(l))  # 6
```

---

## 6. Checking for Substrings

### `in` — check if a character or phrase exists

```python
text = "Python is a programming language"
print("a" in text)  # True
```

### `not in` — check if a character or phrase does NOT exist

```python
textTwo = "Javascript is a programming language"
print("python" not in textTwo)  # True
```

---

## 7. String Slicing

Return a range of characters using the slice syntax `[start:end]`. The start index is **inclusive** and the end index is **exclusive**.

```python
slice = "this is a string data type"

print(slice[2:5])  # is  (characters at index 2, 3, 4)
print(slice[:5])   # this  (from start to index 4)
print(slice[5:])   # is a string data type (from index 5 to end)
```

> **Note:** The first character has index `0`.

---

## 8. Built-in String Methods

Python provides a rich set of methods for manipulating strings.

```python
myVariable = "Coding is fun"

# Convert to uppercase
print(myVariable.upper())    # CODING IS FUN

# Convert to lowercase
print(myVariable.lower())    # coding is fun

# Remove leading and trailing whitespace
myVariableTwo = "   Hello world   "
print(myVariableTwo.strip()) # Hello world

# Replace a substring
print(myVariable.replace("fun", "awesome"))  # Coding is awesome

# Split into a list
print(myVariable.split(" "))  # ['Coding', 'is', 'fun']
```

| Method | Description |
|--------|-------------|
| `.upper()` | Converts all characters to uppercase |
| `.lower()` | Converts all characters to lowercase |
| `.strip()` | Removes leading and trailing whitespace |
| `.replace(old, new)` | Replaces a substring with another |
| `.split(separator)` | Splits the string into a list |

---

## 9. String Concatenation

Use the `+` operator to join two or more strings together.

```python
stringOne   = "Hello"
stringTwo   = "Python"
stringThree = stringOne + " " + stringTwo
print(stringThree)  # Hello Python
```

---

## 10. F-Strings (Formatted Strings)

Prefix a string with `f` and use curly braces `{}` as placeholders for variables or expressions.

```python
age = 20
txt = f"My name is Kate and I am {age} years old"
print(txt)  # My name is Kate and I am 20 years old
```

> F-strings were introduced in Python 3.6 and are the recommended way to format strings.

---

## 11. Escape Characters

Use a backslash `\` to insert characters that would otherwise be illegal inside a string.

```python
txtTwo = "We are the so-called \"Wakanda\" from Africa"
print(txtTwo)  # We are the so-called "Wakanda" from Africa
```

### Common Escape Characters

| Escape | Result |
|--------|--------|
| `\"` | Double quote |
| `\'` | Single quote |
| `\\` | Backslash |
| `\n` | New line |
| `\t` | Tab |
