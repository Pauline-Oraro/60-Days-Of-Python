# 🎨 Simple Drawing App

A lightweight, interactive drawing application built with Python and Tkinter. Draw freely on a canvas, pick any color, and switch between pen sizes — no installation beyond Python required.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [Using the App](#using-the-app)
- [Code Structure](#code-structure)
- [Function Reference](#function-reference)
- [Customization](#customization)
- [Known Limitations](#known-limitations)

---

## Overview

Simple Drawing App is a desktop GUI application that lets you draw smooth freehand lines on a white canvas. It uses Python's built-in `tkinter` library for the interface and `tkinter.colorchooser` for color picking — no third-party packages needed.

---

## Features

- ✏️ **Freehand drawing** — click and drag to draw smooth lines
- 🎨 **Color picker** — choose any color via a native color dialog
- 📏 **Three pen sizes** — Small (2px), Medium (5px), and Large (10px)
- 🗑️ **Clear canvas** — wipe the canvas clean with one click
- 🪟 **Resizable window** — canvas expands to fill the window

---

## Requirements

| Requirement | Details |
|---|---|
| Python version | 3.x (3.6 or higher recommended) |
| External libraries | None — uses only the Python standard library |
| OS | Windows, macOS, or Linux |

> **Note:** `tkinter` ships with most Python installations. If it's missing on Linux, install it with:
> ```bash
> sudo apt-get install python3-tk
> ```

---

## How to Run

1. **Save the script** — copy the code into a file named `drawing_app.py`.

2. **Open a terminal** in the folder containing the file.

3. **Run the script:**
   ```bash
   python drawing_app.py
   ```
   Or on systems where Python 3 is explicit:
   ```bash
   python3 drawing_app.py
   ```

4. The drawing window will open immediately — no further setup needed.

---

## Using the App

### Drawing
- **Click and hold** the left mouse button anywhere on the white canvas.
- **Drag** the mouse to draw a freehand line.
- Release the mouse button to stop drawing.

### Changing Color
- Click the **"Choose Color"** button in the toolbar.
- A native color picker dialog will open.
- Select your desired color and confirm — the button background will update to reflect the active color.

### Changing Pen Size
Use the three buttons in the **Pen Size** section of the toolbar:

| Button | Stroke Width |
|--------|-------------|
| Small  | 2 px        |
| Medium | 5 px (default) |
| Large  | 10 px       |

### Clearing the Canvas
- Click **"Clear Canvas"** to erase all drawings and start fresh.

---

## Code Structure

```
drawing_app.py
│
├── Global state
│   ├── current_x, current_y   # Tracks the mouse position between events
│   ├── color                  # Active drawing color (default: "black")
│   └── pen_size               # Active pen width in pixels (default: 5)
│
├── Event handlers
│   ├── start_position(event)  # Records where a stroke begins
│   └── draw_line(event)       # Draws a line segment as the mouse moves
│
├── UI actions
│   ├── change_color()         # Opens color picker, updates active color
│   ├── clear_canvas()         # Deletes all canvas items
│   ├── change_pen_size(size)  # Sets pen_size to the given value
│   ├── set_small_pen()        # Sets pen size to 2
│   ├── set_medium_pen()       # Sets pen size to 5
│   └── set_large_pen()        # Sets pen size to 10
│
└── UI layout
    ├── window                 # Root Tk window (800×600)
    ├── title_label            # App title at the top
    ├── toolbar                # Horizontal frame holding all controls
    │   ├── color_button       # Color picker button
    │   ├── clear_button       # Clear canvas button
    │   └── size_frame         # Frame grouping pen size buttons
    ├── canvas                 # The drawing surface (white background)
    └── instruction_label      # Usage hint at the bottom
```

---

## Function Reference

### `start_position(event)`

Called when the user **presses** the left mouse button on the canvas (`<Button-1>`).  
Records the initial `(x, y)` coordinates so the first line segment starts from the correct position.

### `draw_line(event)`

Called continuously while the user **drags** the mouse (`<B1-Motion>`).  
Draws a rounded, smooth line segment from the last recorded position to the current mouse position, then updates the stored coordinates.

### `change_color()`

Opens the system color chooser dialog. If the user confirms a color, updates the global `color` variable and changes the button's background to match.

### `clear_canvas()`

Calls `canvas.delete("all")` to remove every drawn element from the canvas.

### `change_pen_size(new_size)`

Updates the global `pen_size` variable to `new_size`. Called internally by the three size-setter functions.

### `set_small_pen()` / `set_medium_pen()` / `set_large_pen()`

Convenience wrappers that call `change_pen_size()` with values `2`, `5`, and `10` respectively.

---

## Customization

You can tweak the following values directly in the source code:

| What to change | Where in the code | Example |
|---|---|---|
| Default pen color | `color = "black"` | `color = "blue"` |
| Default pen size | `pen_size = 5` | `pen_size = 3` |
| Window dimensions | `window.geometry("800x600")` | `window.geometry("1024x768")` |
| Canvas background | `tk.Canvas(..., bg="white")` | `bg="lightyellow"` |
| Custom pen sizes | Values in `set_small/medium/large_pen()` | `change_pen_size(15)` |
| Font style | `font=("Arial", 16)` | `font=("Courier", 14)` |

---

## Known Limitations

- **No save/export** — drawings cannot be saved to a file in the current version.
- **No undo** — there is no way to undo the last stroke.
- **No eraser** — to remove parts of a drawing you must clear the entire canvas.
- **No shapes** — only freehand lines are supported; there are no rectangle, circle, or line tools.
- **Single pen style** — the pen is always round and smooth; dash or texture styles are not available.
