# Python Dates & `datetime`

A date in Python is not a built-in data type, but you can import the `datetime` module to work with dates and times as date objects.

A date object can contain: **year**, **month**, **day**, **hour**, **minute**, **second**, and **microsecond**.

---

## 1. Getting the Current Date & Time

Use `datetime.datetime.now()` to get the current date and time.

```python
import datetime

today = datetime.datetime.now()
print(today)
# e.g. 2025-01-11 14:35:22.123456
```

### Accessing Specific Parts of a Date

```python
print(today.year)            # e.g. 2025
print(today.strftime("%A"))  # e.g. Saturday (full weekday name)
```

---

## 2. Creating a Specific Date

Use the `datetime()` class constructor to create a custom date. It requires at least three parameters: **year**, **month**, and **day**.

```python
my_birthday = datetime.datetime(2001, 1, 11)
print(my_birthday)
# 2001-01-11 00:00:00
```

---

## 3. Formatting Dates with `strftime()`

The `strftime()` method formats a date object into a human-readable string. You pass a **format code** to control the output.

```python
print(today.strftime("%B %d, %Y"))
# e.g. January 11, 2025
```

### Common `strftime()` Format Codes

| Code | Description | Example |
|------|-------------|---------|
| `%Y` | Year (4 digits) | `2025` |
| `%y` | Year (2 digits) | `25` |
| `%m` | Month as a number | `01` |
| `%B` | Full month name | `January` |
| `%b` | Short month name | `Jan` |
| `%d` | Day of the month | `11` |
| `%A` | Full weekday name | `Saturday` |
| `%a` | Short weekday name | `Sat` |
| `%H` | Hour (24-hour) | `14` |
| `%I` | Hour (12-hour) | `02` |
| `%M` | Minute | `35` |
| `%S` | Second | `22` |
| `%p` | AM or PM | `PM` |

---

## Quick Reference

```python
import datetime

# Current date and time
today = datetime.datetime.now()

# Create a specific date
my_birthday = datetime.datetime(2001, 1, 11)

# Format a date as a readable string
print(today.strftime("%B %d, %Y"))   # January 11, 2025
print(today.strftime("%A"))           # Saturday
print(today.year)                     # 2025
```
