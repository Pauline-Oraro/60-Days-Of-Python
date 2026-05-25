# Tkinter Hello World App

A beginner-friendly desktop GUI application built with Python's `tkinter` library. The app greets the user by name, or falls back to a default greeting if no name is provided.

---

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [How to Run](#how-to-run)
- [Code Breakdown](#code-breakdown)
  - [Imports](#imports)
  - [The `say_hello` Function](#the-say_hello-function)
  - [Window Configuration](#window-configuration)
  - [UI Widgets](#ui-widgets)
  - [Main Loop](#main-loop)
- [Application Flow](#application-flow)
- [Widget Reference](#widget-reference)
- [Customisation Ideas](#customisation-ideas)

---

## Overview

This application creates a 300×200 pixel desktop window that:

1. Displays a welcome title.
2. Accepts a name as text input from the user.
3. Shows a personalised greeting on button click — or `"Hello, World"` if the input is empty.

---

## Prerequisites

| Requirement | Details |
|---|---|
| Python Version | 3.x (3.6+ recommended) |
| External Libraries | None — `tkinter` is bundled with standard Python |
| Operating System | Windows, macOS, or Linux |

> **Note:** On some Linux distributions, `tkinter` may need to be installed separately:
> ```bash
> sudo apt-get install python3-tk   # Debian/Ubuntu
> sudo dnf install python3-tkinter  # Fedora
> ```

---

## How to Run

1. Save the script as `hello_app.py`.
2. Open a terminal in the same directory.
3. Execute:

```bash
python hello_app.py
```

The GUI window will open immediately.

---

## Code Breakdown

### Imports

```python
import tkinter as tk
```

Imports the `tkinter` module and aliases it as `tk` for convenience. `tkinter` is Python's standard library for building desktop GUIs, wrapping the Tcl/Tk toolkit.

---

### The `say_hello` Function

```python
def say_hello():
    name = name_entry.get()

    if name:
        greeting_label.config(text=f"Hello, {name}")
    else:
        greeting_label.config(text="Hello, World")
```

This is the **event handler** triggered when the button is clicked.

| Step | Description |
|---|---|
| `name_entry.get()` | Reads the current text from the `Entry` widget and stores it in `name` |
| `if name:` | Evaluates to `True` if the string is non-empty |
| `greeting_label.config(...)` | Dynamically updates the label's `text` property at runtime |
| Fallback | If no name is entered, defaults to `"Hello, World"` |

---

### Window Configuration

```python
window = tk.Tk()
window.title("My first Tkinter App")
window.geometry("300x200")
window.resizable(False, False)
```

| Line | Purpose |
|---|---|
| `tk.Tk()` | Creates the **root window** — the main application container |
| `.title(...)` | Sets the text shown in the OS window title bar |
| `.geometry("300x200")` | Sets the window dimensions to **300px wide × 200px tall** |
| `.resizable(False, False)` | Locks the window size; the two `False` values disable horizontal and vertical resizing respectively |

---

### UI Widgets

Widgets are the visual building blocks of the interface. Each is packed vertically with padding using the `.pack()` geometry manager.

#### Title Label

```python
title_label = tk.Label(window, text="Welcome to Tkinter!", font=("Arial", 16))
title_label.pack(pady=10)
```

- Displays a static heading at the top of the window.
- `font=("Arial", 16)` sets the font family to Arial at size 16.
- `pady=10` adds 10px of vertical padding above and below the widget.

---

#### Name Entry Field

```python
name_entry = tk.Entry(window, width=20)
name_entry.pack(pady=10)
```

- A single-line text input field where the user types their name.
- `width=20` sets the field to 20 characters wide.
- The entered value is later retrieved using `name_entry.get()` inside `say_hello`.

---

#### Button

```python
hello_button = tk.Button(window, text="Say Hello", command=say_hello)
hello_button.pack(pady=10)
```

- Triggers the `say_hello` function when clicked.
- `command=say_hello` binds the function **without** calling it immediately (no parentheses).

---

#### Greeting Label

```python
greeting_label = tk.Label(window, text="", font=("Arial", "12"))
greeting_label.pack(pady=10)
```

- Starts with an empty `text=""` so nothing is shown on launch.
- Updated dynamically by `say_hello` via `.config(text=...)`.
- Font is Arial size 12.

---

### Main Loop

```python
window.mainloop()
```

Starts the **Tkinter event loop** — a continuous process that:

- Keeps the window open and visible.
- Listens for user interactions (clicks, key presses, etc.).
- Dispatches events to the appropriate handlers (e.g., calling `say_hello` on button click).

The program will remain running until the user closes the window.

---

## Application Flow

```
App Launches
     │
     ▼
Window renders with title, entry field, and button
     │
     ▼
User types a name into the Entry field (optional)
     │
     ▼
User clicks "Say Hello"
     │
     ├─── Name entered? ──YES──▶ Display "Hello, <name>"
     │
     └─── No name? ────────────▶ Display "Hello, World"
```

---

## Widget Reference

| Widget | Variable | Type | Role |
|---|---|---|---|
| Root window | `window` | `tk.Tk` | Main application container |
| Title text | `title_label` | `tk.Label` | Static welcome heading |
| Text input | `name_entry` | `tk.Entry` | Collects user's name |
| Action button | `hello_button` | `tk.Button` | Triggers the greeting logic |
| Output text | `greeting_label` | `tk.Label` | Displays the greeting result |

---

## Customisation Ideas

- **Default placeholder text** — Use `name_entry.insert(0, "Enter your name...")` to pre-fill the entry field.
- **Keyboard shortcut** — Bind the Enter key to the button: `window.bind("<Return>", lambda e: say_hello())`.
- **Clear button** — Add a button that resets both the entry field and greeting label.
- **Colour themes** — Add `bg` and `fg` parameters to widgets for custom background and text colours.
- **Centre the window** — Calculate screen dimensions and use `.geometry(f"{w}x{h}+{x}+{y}")` to centre on launch.