# 🔐 Password Generator

A simple, interactive command-line password generator written in Python. Customize your password length and character types, and get an instant strength rating — no third-party libraries required.

---

## Features

- Generate passwords between **8 and 30 characters**
- Choose from four character sets:
  - Lowercase letters (`a-z`)
  - Uppercase letters (`A-Z`)
  - Numbers (`0-9`)
  - Special characters (`!@#$%` and more)
- **Password strength checker** that scores based on length and character variety
- Graceful fallback to lowercase if no character type is selected
- Option to generate multiple passwords in one session

---

## Requirements

- Python 3.x
- No external dependencies — uses only the built-in `random` and `string` modules

---

## Usage

Run the script directly from your terminal:

```bash
python password_generator.py
```

You'll be guided through an interactive prompt:

```
 ====  PASSWORD GENERATOR  ====
 Create super strong and secure passwords with ease!

Enter password length (8-30): 16

 Let's customize your password!
Include lowercase letters (a-z)? (y/n): y
Include uppercase letters (A-Z)? (y/n): y
Include numbers letters (0-9)? (y/n): y
Include special character (!@$#%)? (y/n): y

==== YOUR NEW PASSWORD 🎉
 gT3#mZ!qR8@wLx2&

 Strength:  ULTRA STRONG
```

---

## Strength Rating

Passwords are scored on a scale combining **length** (60%) and **character variety** (40%):

| Rating | Score |
|---|---|
| ULTRA STRONG | ≥ 0.8 |
| STRONG | ≥ 0.6 |
| DECENT | ≥ 0.4 |
| NEEDS IMPROVEMENT | < 0.4 |

---

## Functions

| Function | Description |
|---|---|
| `generate_password(...)` | Builds a random password from the selected character sets |
| `check_password_strength(password)` | Returns a strength label based on length and variety |
| `get_yes_no_input(question)` | Helper that validates `y/n` user input |
| `main()` | Entry point — runs the interactive CLI flow |

---

## Security Tips

As reminded at the end of each session:

- Never reuse the same password across multiple accounts
- Store passwords in a reputable **password manager**
- Rotate important passwords every few months
- Keep passwords private — even strong ones can be compromised if shared

---
