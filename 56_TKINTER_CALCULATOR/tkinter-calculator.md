# Simple Calculator

A lightweight desktop calculator application built with Python's `tkinter` library. It provides a clean graphical interface for adding two numbers together.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Code Breakdown](#code-breakdown)
- [Error Handling](#error-handling)
- [Limitations](#limitations)

---

## Overview

This application launches a small desktop window where a user can input two numbers, click a button to add them, and instantly see the result — all without touching a terminal or command line.

---

## Features

- **Addition of two numbers** — supports integers and decimals
- **Input validation** — displays a friendly error message for non-numeric input
- **Clear button** — resets both input fields and the result label in one click
- **Minimal dependencies** — uses only Python's built-in `tkinter` library

---

## Requirements

| Requirement | Version      |
|-------------|--------------|
| Python      | 3.x          |
| tkinter     | Built-in     |
| OS          | Windows / macOS / Linux |

> **Note:** `tkinter` ships with most standard Python installations. If it is missing, see [Installation](#installation) below.

---

## Installation

### 1. Clone or download the repository

```bash
git clone https://github.com/your-username/simple-calculator.git
cd simple-calculator
```

Or simply download the `calculator.py` file directly.

### 2. Verify Python is installed

```bash
python --version
# or
python3 --version
```

### 3. Check that tkinter is available

```bash
python -m tkinter
```

A small test window should appear. If it does not, install `tkinter` for your platform:

- **Ubuntu / Debian:**
  ```bash
  sudo apt-get install python3-tk
  ```
- **Fedora:**
  ```bash
  sudo dnf install python3-tkinter
  ```
- **macOS (via Homebrew):**
  ```bash
  brew install python-tk
  ```
- **Windows:** Reinstall Python from [python.org](https://www.python.org/downloads/) and make sure the *tcl/tk and IDLE* option is checked during setup.

---

## Usage

Run the script from your terminal:

```bash
python calculator.py
# or
python3 calculator.py
```

A 300×250 window titled **"Simple Calculator"** will open.

### Step-by-step

1. Type the **first number** into the *First Number* field.
2. Type the **second number** into the *Second Number* field.
3. Click **"Add Numbers"** — the sum appears under the *Result* label.
4. Click **"Clear"** to reset all fields and start over.

---

## Project Structure

```
simple-calculator/
│
├── calculator.py   # Main application file
└── README.md       # Project documentation
```

---

## Code Breakdown

### `calculate_sum()`

```python
def calculate_sum():
    try:
        num1 = float(first_number.get())
        num2 = float(second_number.get())
        result = num1 + num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")
```

Reads the values from both `Entry` widgets, converts them to floats, computes the sum, and updates the result label. If either value cannot be converted, a `ValueError` is caught and a user-friendly message is shown instead.

---

### `clear_fields()`

```python
def clear_fields():
    first_number.delete(0, tk.END)
    second_number.delete(0, tk.END)
    result_label.config(text="Result: ")
```

Clears both input fields using `delete(0, tk.END)` and resets the result label to its default text.

---

### GUI Layout

| Widget            | Type     | Purpose                              |
|-------------------|----------|--------------------------------------|
| `title_label`     | Label    | Displays the app title               |
| `frame1`          | Frame    | Groups the first number label + entry|
| `frame2`          | Frame    | Groups the second number label + entry|
| `first_number`    | Entry    | Accepts the first numeric input      |
| `second_number`   | Entry    | Accepts the second numeric input     |
| `calculate_button`| Button   | Triggers `calculate_sum()`           |
| `result_label`    | Label    | Displays the result or error message |
| `clear_button`    | Button   | Triggers `clear_fields()`            |

---

## Error Handling

| Scenario                        | Behaviour                                      |
|---------------------------------|------------------------------------------------|
| One or both fields are empty    | Displays *"Please enter valid numbers"*        |
| Non-numeric text entered        | Displays *"Please enter valid numbers"*        |
| Valid integers or decimals      | Displays the computed sum                      |

---

## Limitations

- **Addition only** — the calculator does not support subtraction, multiplication, or division in its current form.
- **Two operands only** — only two numbers can be added at a time.
- **No keyboard shortcut** — pressing *Enter* does not trigger the calculation; the button must be clicked.

---
