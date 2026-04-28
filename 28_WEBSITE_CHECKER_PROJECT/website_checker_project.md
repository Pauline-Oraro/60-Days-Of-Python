# Website URL Checker 🔐

A beginner-friendly Python mini project that checks whether a website URL is **secure (HTTPS)** or **not secure (HTTP)** by analysing the URL prefix entered by the user.

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Concepts Used](#concepts-used)
- [The Code](#the-code)
- [Step-by-Step Explanation](#step-by-step-explanation)
- [Sample Output](#sample-output)
- [What is HTTPS vs HTTP?](#what-is-https-vs-http)
- [Important Notes](#important-notes)

---

## Project Overview

This mini project takes a website URL as user input and uses conditional logic (`if`, `elif`, `else`) to determine whether the URL uses the **secure HTTPS protocol** or the **unsecured HTTP protocol**.

---

## Concepts Used

| Concept | Description |
|---------|-------------|
| `print()` | Displays output to the terminal |
| `input()` | Takes user input from the terminal |
| `str.startswith()` | Checks if a string begins with a specified prefix |
| `if / elif / else` | Conditional statements for decision making |

---

## The Code

```python
print("WEBSITE URL CHECKER")
url = input("Enter the URL of the website you want to check: ")

if url.startswith('https://'):
    print("This website uses HTTPS which is secure.")
elif url.startswith("http://"):
    print("This website uses HTTP which is not secure.")
else:
    print("Invalid URL. Please make sure to include http:// or https://")
```

---

## Step-by-Step Explanation

### Step 1 — Display the Program Title

```python
print("WEBSITE URL CHECKER")
```

The first line simply prints the name of the program to the terminal so the user knows what the program does before they interact with it.

---

### Step 2 — Get User Input

```python
url = input("Enter the URL of the website you want to check: ")
```

- `input()` pauses the program and waits for the user to type something and press **Enter**
- Whatever the user types is stored as a **string** in the variable `url`
- The string inside `input()` is the **prompt** — it tells the user what to type

> **Important:** `input()` always returns a **string**, even if the user types a number. No type conversion is needed here since we are working with text.

---

### Step 3 — Check for HTTPS (Secure)

```python
if url.startswith('https://'):
    print("This website uses HTTPS which is secure.")
```

- `startswith()` is a built-in Python **string method** that returns `True` if the string begins with the specified prefix and `False` if it does not
- This checks whether the URL begins with `'https://'` — the secure protocol
- If true, the program tells the user the website is secure

> **Important:** The `if` condition is checked **first**. Python evaluates conditions from top to bottom and stops at the first match. `https://` is checked before `http://` deliberately — because `https://` also starts with `http://`, so checking `http://` first would incorrectly match secure URLs.

---

### Step 4 — Check for HTTP (Not Secure)

```python
elif url.startswith("http://"):
    print("This website uses HTTP which is not secure.")
```

- `elif` ("else if") is only evaluated if the `if` condition above was `False`
- This catches URLs that use plain `http://` — the unencrypted, unsecured protocol
- If true, the program warns the user the website is not secure

---

### Step 5 — Handle Invalid Input

```python
else:
    print("Invalid URL. Please make sure to include http:// or https://")
```

- The `else` block runs when **none** of the above conditions matched
- This handles cases where the user typed something that is not a valid URL (e.g. `github.com` without any protocol prefix, or a random string)
- Always include an `else` block as a safety net for unexpected input

> **Important:** Never assume users will enter input in the exact format you expect. Always handle invalid input gracefully — this is called **input validation**.

---

---

## Sample Output

### Secure URL (HTTPS)

```
========================================
      WEBSITE URL CHECKER
========================================
Enter the URL of the website you want to check: https://github.com/Pauline-Oraro
✅ 'https://github.com/Pauline-Oraro' uses HTTPS — this website is SECURE.
```

### Unsecure URL (HTTP)

```
========================================
      WEBSITE URL CHECKER
========================================
Enter the URL of the website you want to check: http://example.com
⚠️  'http://example.com' uses HTTP — this website is NOT SECURE.
   Consider using the HTTPS version if available.
```

### Invalid Input

```
========================================
      WEBSITE URL CHECKER
========================================
Enter the URL of the website you want to check: github.com
❌ Invalid URL. Please include 'http://' or 'https://' at the start.
```

---

## What is HTTPS vs HTTP?

| Feature | HTTP | HTTPS |
|---------|------|-------|
| **Full Name** | Hypertext Transfer Protocol | Hypertext Transfer Protocol **Secure** |
| **Encryption** | ❌ No encryption | ✅ Encrypted using TLS/SSL |
| **Data Security** | Data sent in plain text — visible to attackers | Data is encrypted — unreadable to attackers |
| **URL Prefix** | `http://` | `https://` |
| **Port** | 80 | 443 |
| **Use Case** | Old or internal websites | All modern websites, especially those handling logins or payments |
| **Browser Indicator** | 🔓 "Not Secure" warning | 🔒 Padlock icon |

> **Important:** Never enter passwords, credit card numbers, or personal information on a website that uses `http://`. Without HTTPS, your data is transmitted as plain text and can be intercepted by anyone on the same network — this is called a **Man-in-the-Middle (MITM) attack**.

---

## Important Notes

- **Order of conditions matters** — always check `https://` before `http://` because `https://` also contains `http://`. Reversing the order would cause all HTTPS URLs to be incorrectly flagged as HTTP
- **`startswith()` is case-sensitive** — `HTTP://` would not match `http://`. Use `.lower()` on the input to handle this: `url.lower().startswith('https://')`
- **This is a prefix check only** — it does not make a real network request to verify the website exists or that its SSL certificate is valid. For real URL validation, use libraries like `requests` or `validators`
- **`input()` always returns a string** — no need to convert the type since we are only working with string methods
- **Always handle the `else` case** — robust programs never assume user input will be perfect

---

## 👩‍💻 Author

**Pauline Oraro**
60 Days of Python Challenge — Website Checker Project
