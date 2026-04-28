# Python File Handling

Python has built-in functions for **creating**, **reading**, **updating**, and **deleting** files. The key function for working with files is the `open()` function.

```python
from pathlib import Path
```

---

## 1. The `open()` Function

`open()` takes two parameters: **filename** and **mode**.

```python
open(filename, mode)
```

### File Modes

| Mode | Name | Description |
|------|------|-------------|
| `"r"` | Read | Default. Opens for reading. Raises an error if the file does not exist. |
| `"a"` | Append | Opens for appending. Creates the file if it does not exist. |
| `"w"` | Write | Opens for writing. Creates the file if it does not exist. Overwrites existing content. |
| `"x"` | Create | Creates the specified file. Raises an error if the file already exists. |

### File Type Modes

| Mode | Description |
|------|-------------|
| `"t"` | Text mode — Default value |
| `"b"` | Binary mode |

---

## 2. Reading a File

### Reading the Whole File

```python
file = open(Path(__file__).parent / "demofile.txt")
print(file.read())   # returns the entire file content
file.close()
```

### Reading a Specific Number of Characters

```python
file = open(Path(__file__).parent / "demofile.txt")
print(file.read(5))  # returns only the first 5 characters
file.close()
```

### Reading One Line at a Time

```python
file = open(Path(__file__).parent / "demofile.txt")
print(file.readline())  # returns the first line
file.close()
```

> **Best practice:** Always close the file after you are done with it using the `.close()` method to free up system resources.

---

## 3. Using the `with` Statement

The `with` statement is the recommended way to open files. It automatically closes the file when the block is done — even if an error occurs — so you don't need to call `.close()` manually.

```python
with open(Path(__file__).parent / "demofile.txt") as my_file:
    print(my_file.read())
```

---

## 4. Writing to a File

To write to an existing file, pass `"a"` (append) or `"w"` (write) as the mode.

### Append — Adds to the End of the File

```python
with open(Path(__file__).parent / "demofile.txt", "a") as this_file:
    this_file.write(" Now the file has more content!")

# verify the result
with open(Path(__file__).parent / "demofile.txt") as this_file:
    print(this_file.read())
```

### Write — Overwrites Existing Content

```python
with open(Path(__file__).parent / "demofile.txt", "w") as this_file:
    this_file.write("This replaces all existing content.")
```

| Mode | Effect on Existing Content |
|------|---------------------------|
| `"a"` | Keeps existing content, adds new content at the end |
| `"w"` | Wipes existing content and replaces it |

---

## 5. Deleting a File

To delete a file, import the `os` module and use `os.remove()`.

```python
import os

os.remove("demofile.txt")
```

> **Tip:** Check if the file exists before deleting to avoid an error:

```python
import os

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")
```

---

## Quick Reference

| Task | Code |
|------|------|
| Open and read a file | `open("file.txt")` or `open("file.txt", "r")` |
| Read entire content | `file.read()` |
| Read n characters | `file.read(n)` |
| Read one line | `file.readline()` |
| Close a file | `file.close()` |
| Open with auto-close | `with open("file.txt") as f:` |
| Append to a file | `open("file.txt", "a")` |
| Overwrite a file | `open("file.txt", "w")` |
| Create a new file | `open("file.txt", "x")` |
| Delete a file | `os.remove("file.txt")` |
