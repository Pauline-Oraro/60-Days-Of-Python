# 🍅 Pomodoro Timer

A terminal-based Pomodoro productivity timer written in Python. It guides you through focused work sessions and scheduled breaks using the Pomodoro Technique, with cross-platform support and optional custom configuration.

---

## Table of Contents

- [Overview](#overview)
- [How It Works](#how-it-works)
- [Functions](#functions)
  - [clear_screen()](#clear_screen)
  - [format_time(seconds)](#format_timeseconds)
  - [countdown(seconds, label)](#countsdownseconds-label)
  - [pomodoro_timer()](#pomodoro_timer-1)
- [Configuration](#configuration)
  - [Default Settings](#default-settings)
  - [Custom Settings](#custom-settings)
- [Flow Diagram](#flow-diagram)
- [Platform Support](#platform-support)
- [Usage](#usage)
- [Error Handling](#error-handling)

---

## Overview

The **Pomodoro Technique** is a time management method that alternates between focused work intervals and short rest periods. After a set number of cycles, a longer break is taken to allow deeper recovery.

This script implements the technique entirely in the terminal — no GUI or external libraries required (except `winsound` on Windows for audio alerts).

---

## How It Works

1. The program launches and prompts the user to use default or custom settings.
2. A **work session** countdown begins.
3. After each work session, the user is prompted to start either a **short break** or a **long break** (depending on how many cycles have completed).
4. This loop continues indefinitely until the user presses `Ctrl+C` to exit.

---

## Functions

### `clear_screen()`

Clears the terminal screen in a cross-platform way.

```python
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
```

| Detail | Value |
|---|---|
| **Parameters** | None |
| **Returns** | None |
| **Windows command** | `cls` |
| **Unix/macOS command** | `clear` |

Uses Python's `platform.system()` to detect the OS at runtime and issue the appropriate shell command.

---

### `format_time(seconds)`

Converts a raw integer of seconds into a human-readable `MM:SS` string.

```python
def format_time(seconds):
    minutes = seconds // 60
    seconds_remainder = seconds % 60
    return f"{minutes:02d}:{seconds_remainder:02d}"
```

| Parameter | Type | Description |
|---|---|---|
| `seconds` | `int` | Total number of seconds to format |

**Returns:** `str` — Zero-padded time string in `MM:SS` format.

**Examples:**

| Input | Output |
|---|---|
| `90` | `"01:30"` |
| `300` | `"05:00"` |
| `45` | `"00:45"` |

---

### `countdown(seconds, label)`

Runs the main countdown loop, printing a live timer to the terminal and alerting the user when the session ends.

```python
def countdown(seconds, label):
    for remaining in range(seconds, 0, -1):
        clear_screen()
        print(f"\n {label}  ")
        print(f"\n⏳ Time remaining: {format_time(remaining)}")
        ...
        time.sleep(1)
    clear_screen()
    print(f"\n✅ {label} completed")
    # Plays beep on Windows, prints 🔔 on Unix/macOS
```

| Parameter | Type | Description |
|---|---|---|
| `seconds` | `int` | Duration of the countdown in seconds |
| `label` | `str` | Name of the session (e.g. `"work session"`, `"Short Break"`) |

**Behaviour by label:**

| Label value | Message displayed |
|---|---|
| `"work session"` | `Focus on your task!` |
| Any string containing `"Break"` | `Take a breath...` |

**On completion:**

- Clears the screen and prints a completion message.
- **Windows:** plays an audio beep via `winsound.Beep(1000, 500)` (1000 Hz, 500 ms).
- **Unix/macOS:** prints a 🔔 bell emoji as a visual cue.

---

### `pomodoro_timer()`

The main entry point and control loop for the application.

```python
def pomodoro_timer():
    ...
```

**Responsibilities:**

1. Displays a welcome screen.
2. Prompts the user to accept defaults or provide custom settings.
3. Confirms the active configuration to the user.
4. Waits for `Enter` to begin.
5. Runs an infinite loop alternating between work sessions and breaks.
6. Tracks completed cycles to determine when a long break is due.
7. Handles `KeyboardInterrupt` (`Ctrl+C`) for a graceful exit.

---

## Configuration

### Default Settings

These values are used if the user selects `yes` (or presses Enter) at the customisation prompt.

| Setting | Default Value |
|---|---|
| Work session length | **25 minutes** |
| Short break length | **5 minutes** |
| Long break length | **15 minutes** |
| Cycles before long break | **4** |

### Custom Settings

If the user types `no` (or any string starting with `n`) at the prompt, they are asked to input each value manually:

```
Enter work session length (minutes): 
Enter short break length (minutes): 
Enter long break length (minutes): 
Enter number of cycles before a long break: 
```

All inputs are cast to `int`. If any value cannot be converted, a `ValueError` is caught and the default settings are restored automatically.

---

## Flow Diagram

```
Start
  │
  ▼
Show welcome screen
  │
  ▼
Use default settings? ──yes──► Use defaults
  │ no
  ▼
Prompt for custom values
  │
  ▼
Show configuration summary
  │
  ▼
Press Enter to begin
  │
  ▼
┌─────────────────────────────────┐
│                                 │
│   Start Work Session countdown  │◄──────────────────┐
│                                 │                   │
└──────────────┬──────────────────┘                   │
               │                                      │
               ▼                                      │
       completed_cycles += 1                          │
               │                                      │
       ┌───────┴────────┐                             │
       │                │                             │
  cycles % n == 0   otherwise                         │
       │                │                             │
       ▼                ▼                             │
  Long Break        Short Break                       │
       │                │                             │
       └───────┬────────┘                             │
               │                                      │
               ▼                                      │
       Press Enter to continue ──────────────────────►┘
               │
        (Ctrl+C pressed)
               │
               ▼
     Print goodbye & exit
```

---

## Platform Support

| OS | Screen clear | End-of-session alert |
|---|---|---|
| Windows | `os.system("cls")` | `winsound.Beep(1000, 500)` |
| macOS | `os.system("clear")` | Prints 🔔 |
| Linux | `os.system("clear")` | Prints 🔔 |

> **Note:** `winsound` is a Windows-only standard library module and is imported inside the function to avoid import errors on other platforms.

---

## Usage

### Running the script

```bash
python pomodoro_timer.py
```

### Starting a session

```
Pomodoro Timer

Use default settings (25min work, 5min short break, 15min long break?) (yes/no): yes

Starting Pomodoro Timer with:
• 25 minute work sessions
• 5 minute short breaks
• 15 minute long break after 4 cycles
• Press Ctrl+C at any time to exit

Press Enter to begin...
```

### During a countdown

```
 Work Session  

⏳ Time remaining: 24:37

 Focus on your task! 
```

### Stopping the timer

Press `Ctrl+C` at any time:

```
Goodbye!
```

---

## Error Handling

| Scenario | Handling |
|---|---|
| Non-integer input during custom setup | `ValueError` caught; defaults restored; 2-second warning shown |
| User presses `Ctrl+C` | `KeyboardInterrupt` caught; screen cleared; goodbye message printed |

---
