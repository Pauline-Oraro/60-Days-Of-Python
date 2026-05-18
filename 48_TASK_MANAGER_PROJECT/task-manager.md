# Task Manager

A simple command-line task manager written in Python that lets you add, view, complete, and delete tasks interactively.

---

## Features

- Add tasks with a custom title
- View all tasks with their completion status
- Mark tasks as completed
- Delete tasks
- Simple numbered menu interface

---

## How to Run

```bash
python task_manager.py
```

---

## Menu Options

| Option | Action |
|--------|--------|
| `1` | Add a new task |
| `2` | View all tasks |
| `3` | Mark a task as completed |
| `4` | Delete a task |
| `0` | Exit the program |

---

## Functions

### `display_menu()`

Prints the main navigation menu to the console.

### `add_task()`

Prompts the user for a task title and appends a new task dictionary to the `tasks` list. Each task is stored as:
```python
{"title": str, "completed": bool}
```

### `view_tasks()`

Displays all current tasks with their index and completion status. A `✓` indicates a completed task; a blank space indicates a pending one.

```
=== My tasks ===
1. [ ] Buy groceries
2. [✓] Write report
================
```

### `complete_tasks()`

Displays the task list and prompts the user to enter a task number. Sets the chosen task's `completed` field to `True`.

### `delete_task()`

Displays the task list and prompts the user to enter a task number. Removes the chosen task from the `tasks` list using `pop()`.

### `main()`

The entry point. Runs an infinite loop that displays the menu and routes user input to the appropriate function. Exits cleanly when the user enters `0`.

---

## Data Structure

Tasks are stored in a global in-memory list. Each task is a dictionary:

```python
tasks = [
    {"title": "Buy groceries", "completed": False},
    {"title": "Write report", "completed": True},
]
```

> **Note:** Data is not persisted between sessions. All tasks are lost when the program exits.

---

## Error Handling

- Non-numeric input when selecting a task number is caught with a `ValueError` and prompts a friendly error message.
- Out-of-range task numbers are validated and rejected before any action is taken.

---

## Example Session

```
=== Task Manager ===
1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
0. Exit
=======================
Enter your choice (0-4): 1
Enter task title: Buy groceries
Task Buy groceries added successfully.

Enter your choice (0-4): 2

=== My tasks ===
1. [ ] Buy groceries
================

Enter your choice (0-4): 3
1. [ ] Buy groceries
Enter task number to mark as completed: 1
Task 'Buy groceries' marked as completed!

Enter your choice (0-4): 0
Goodbye! 👋
```
