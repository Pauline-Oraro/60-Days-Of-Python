# Python Virtual Environments

## What is a Virtual Environment?

A **virtual environment** in Python is an isolated environment on your computer where you can run and test your Python projects. It allows you to manage project-specific dependencies without interfering with other projects or your main Python installation.

Think of a virtual environment as a **separate container** for each Python project. Each container:

- Has its own Python interpreter
- Has its own set of installed packages
- Is isolated from other virtual environments
- Can have different versions of the same package

### Why Use Virtual Environments?

- Prevents package version conflicts between projects
- Makes projects more portable and reproducible
- Keeps your system Python installation clean
- Allows testing with different Python versions

---

## 1. Creating a Virtual Environment

Python has the built-in `venv` module for creating virtual environments. Open your command prompt, navigate to your project folder, and run:

```bash
# Windows
python -m venv myfirstproject

# macOS/Linux
python3 -m venv myfirstproject
```

This creates a folder named `myfirstproject` with the following structure:

```
myfirstproject/
  Include/
  Lib/
  Scripts/
  .gitignore
  pyvenv.cfg
```

---

## 2. Activating the Virtual Environment

Before using the virtual environment, you must **activate** it:

```bash
# Windows
myfirstproject\Scripts\activate

# macOS/Linux
source myfirstproject/bin/activate
```

Once activated, your command prompt changes to show the active environment:

```bash
# Windows
(myfirstproject) C:\Users\Your Name>

# macOS/Linux
(myfirstproject) user@machine:~$
```

> The name in parentheses confirms you are working inside the virtual environment.

---

## 3. Installing Packages

Once your virtual environment is activated, install packages using `pip`. Packages are installed **only inside the virtual environment** and do not affect your global Python installation.

```bash
(myfirstproject) C:\Users\Your Name> pip install cowsay
```

Output:

```
Collecting cowsay
  Downloading cowsay-6.1-py3-none-any.whl (25 kB)
Installing collected packages: cowsay
Successfully installed cowsay-6.1
```

---

## 4. Using an Installed Package

Create a file called `test.py` and use the installed package:

```python
# test.py
import cowsay

cowsay.cow("Good Mooooorning!")
```

Run it from within the virtual environment:

```bash
(myfirstproject) C:\Users\Your Name> python test.py
```

Output:

```
  _________________
| Good Mooooorning! |
  =================
                 \
                  \
                    ^__^
                    (oo)\_______
                    (__)\       )\/\
                        ||----w |
                        ||     ||
```

---

## 5. Deactivating the Virtual Environment

When you are done working, deactivate the environment to return to your normal command line:

```bash
(myfirstproject) C:\Users\Your Name> deactivate
```

Your prompt returns to normal:

```bash
C:\Users\Your Name>
```

> **Important:** Running `test.py` outside the virtual environment will raise an error because `cowsay` was only installed inside it:
> ```
> ModuleNotFoundError: No module named 'cowsay'
> ```
> Simply activate the environment again to fix this.

---

## 6. Deleting a Virtual Environment

Since a virtual environment is self-contained, deleting it has no effect on other projects. Simply delete the folder:

```bash
# Windows
rmdir /s /q myfirstproject

# macOS/Linux
rm -rf myfirstproject
```

---

## Quick Reference

| Task | Windows Command | macOS/Linux Command |
|------|----------------|---------------------|
| Create environment | `python -m venv name` | `python3 -m venv name` |
| Activate | `name\Scripts\activate` | `source name/bin/activate` |
| Install a package | `pip install package` | `pip install package` |
| List installed packages | `pip list` | `pip list` |
| Deactivate | `deactivate` | `deactivate` |
| Delete environment | `rmdir /s /q name` | `rm -rf name` |
