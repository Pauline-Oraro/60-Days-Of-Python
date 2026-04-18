# Python Regular Expressions (RegEx)

A **regular expression (regex)** is a sequence of characters that forms a search pattern. It is used to check if a string contains a specified pattern, extract matches, split strings, or replace text.

Python has a built-in package called `re` for working with regular expressions.

```python
import re
```

---

## 1. `re.search()` — Find the First Match

Searches the string for a match and returns a **match object** if found. If there is more than one match, only the **first occurrence** is returned. Returns `None` if no match is found.

```python
my_text = "The rain in Kenya"
my_search = re.search("^The.*Kenya$", my_text)

if my_search:
    print("yes we have a match")
else:
    print("no match")
# yes we have a match

print(my_search)
# <re.Match object; span=(0, 17), match='The rain in Kenya'>
```

---

## 2. Match Object Methods

When `re.search()` finds a match it returns a **match object** containing information about the result.

| Method | Description | Example Output |
|--------|-------------|----------------|
| `.span()` | Returns a tuple with the start and end positions of the match | `(11, 16)` |
| `.string` | Returns the original string passed into the function | `'The rain in Kenya'` |
| `.group()` | Returns the part of the string where the match was found | `'Kenya'` |

```python
my_search = re.search(r"\bK\w+", my_text)

print(my_search.span())   # (11, 16)
print(my_search.string)   # The rain in Kenya
print(my_search.group())  # Kenya
```

---

## 3. `re.findall()` — Find All Matches

Returns a **list** containing all matches. Returns an empty list if no match is found.

```python
my_text = "The rain in Kenya"
my_second_search = re.findall("ai", my_text)
print(my_second_search)  # ['ai']
```

---

## 4. `re.split()` — Split at Each Match

Returns a **list** where the string has been split at each match.

```python
my_third_search = re.split("\s", my_text)
print(my_third_search)  # ['The', 'rain', 'in', 'Kenya']
```

---

## 5. `re.sub()` — Replace Matches

Replaces all matches with the text of your choice and returns the modified string.

```python
my_fourth_search = re.sub("\s", "9", my_text)
print(my_fourth_search)  # The9rain9in9Kenya
```

---

## 6. Metacharacters

Metacharacters are characters with **special meaning** in regex patterns.

```python
this_text = "Python is a programming language. Python is popular."
```

| Metacharacter | Description | Example | Match |
|---------------|-------------|---------|-------|
| `[]` | A set of characters — matches any one character in the set | `[a-m]` | Any letter from a to m |
| `\` | Signals a special sequence or escapes a special character | `\d` | Any digit |
| `.` | Any character except a newline | `P..hon` | `Python` |
| `^` | Starts with | `^Python` | String starting with `Python` |
| `$` | Ends with | `popular.$` | String ending with `popular.` |
| `*` | Zero or more occurrences | `Pytho*n` | `Pythn`, `Python`, `Pythoon` |
| `+` | One or more occurrences | `Pytho+n` | `Python`, `Pythoon` (not `Pythn`) |
| `?` | Zero or one occurrence | `Pytho?n` | `Pythn` or `Python` |
| `{n}` | Exactly n occurrences | `Pytho{2}n` | `Pythoon` |

### Examples

```python
# [] — match any character from a to m
search_one = re.findall("[a-m]", this_text)
print(search_one)  # ['h', 'i', 'a', 'g', 'a', 'i', 'l', 'a', 'g', 'a', 'g', 'e', ...]

# \ — match any digit
search_two = re.findall("\d", this_text)
print(search_two)  # [] (no digits in this_text)

# . — any character except newline
search_three = re.findall("P..hon", this_text)
print(search_three)  # ['Python', 'Python']

# ^ — starts with
search_four = re.findall("^Python", this_text)
print(search_four)  # ['Python']

# $ — ends with
search_five = re.findall("popular.$", this_text)
print(search_five)  # ['popular.']

# * — zero or more occurrences of 'o'
search_six = re.findall("Pytho*n", this_text)
print(search_six)  # ['Python', 'Python']

# + — one or more occurrences of 'o'
search_seven = re.findall("Pytho+n", this_text)
print(search_seven)  # ['Python', 'Python']

# ? — zero or one occurrence of 'o'
search_eight = re.findall("Pytho?n", this_text)
print(search_eight)  # ['Python', 'Python']

# {n} — exactly 2 occurrences of 'o'
search_nine = re.findall("Pytho{2}n", this_text)
print(search_nine)  # [] (no 'Pythoon' in this_text)
```

---

## Quick Reference

| Function | Description | Returns |
|----------|-------------|---------|
| `re.search(pattern, str)` | Finds the first match | Match object or `None` |
| `re.findall(pattern, str)` | Finds all matches | List of matches |
| `re.split(pattern, str)` | Splits string at each match | List of substrings |
| `re.sub(pattern, replacement, str)` | Replaces all matches | Modified string |
