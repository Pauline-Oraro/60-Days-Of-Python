# 🎵 Music Recommender — Mini Project

A command-line Python application that recommends a random music artist based on the user's preferred genre. It uses a dictionary to map genres to artists and the `random` module to pick a surprise recommendation.

---

## 📋 Project Overview

| Detail | Info |
|--------|------|
| **Project Type** | Mini Project — Command Line App |
| **Difficulty** | Beginner |
| **Concepts Used** | `import random`, dictionaries, `input()`, `print()`, `if/else`, `random.choice()`, f-strings |

---

## 💻 Full Code

```python
import random

print("MUSIC RECOMMENDER")

genres = {
    "Pop":       ["Taylor Swift", "Ariana Grande", "Ed Sheeran"],
    "Hip Hop":   ["Kendrick Lamar", "Drake", "J. Cole"],
    "R&B":       ["SZA", "The Weeknd", "Usher"],
    "Gospel":    ["Kirk Franklin", "CeCe Winans", "Maverick City Music"],
    "Jazz":      ["Miles Davis", "Louis Armstrong", "Nina Simone"],
    "Reggae":    ["Bob Marley", "Sean Paul", "Shaggy"],
    "Afrobeats": ["Burna Boy", "Wizkid", "Tems"],
    "Amapiano":  ["Kabza De Small", "DJ Maphorisa", "Tyler ICU"]
}

choice = input("What genre do you like? (Pop/Hip Hop/R&B/Gospel/Jazz/Reggae/Afrobeats/Amapiano): ")

if choice not in genres:
    print("Sorry, I don't know that genre.")
else:
    print(f"Check out {random.choice(genres[choice])}")
```

---

## 🔍 Step-by-Step Explanation

### Step 1 — Import the `random` Module

```python
import random
```

- The `random` module is a Python **built-in** — no installation needed
- It is imported at the very top of the file, before any code runs
- Here it is used for `random.choice()` which picks a random item from a list

> **Important:** Always place `import` statements at the **top of the file**. Python reads top to bottom — importing after the code that uses it will cause a `NameError`.

---

### Step 2 — Display the App Title

```python
print("MUSIC RECOMMENDER")
```

- Prints the name of the application to the terminal
- Lets the user know what the program does before they interact with it

---

### Step 3 — Create the Genre Dictionary

```python
genres = {
    "Pop":       ["Taylor Swift", "Ariana Grande", "Ed Sheeran"],
    "Hip Hop":   ["Kendrick Lamar", "Drake", "J. Cole"],
    "R&B":       ["SZA", "The Weeknd", "Usher"],
    "Gospel":    ["Kirk Franklin", "CeCe Winans", "Maverick City Music"],
    "Jazz":      ["Miles Davis", "Louis Armstrong", "Nina Simone"],
    "Reggae":    ["Bob Marley", "Sean Paul", "Shaggy"],
    "Afrobeats": ["Burna Boy", "Wizkid", "Tems"],
    "Amapiano":  ["Kabza De Small", "DJ Maphorisa", "Tyler ICU"]
}
```

- A **dictionary** is used to map each genre (key) to a list of artists (value)
- Each **key** is a genre name (string)
- Each **value** is a **list** of three artist names

### Dictionary Structure

| Key (Genre) | Value (Artists) |
|-------------|-----------------|
| `"Pop"` | `["Taylor Swift", "Ariana Grande", "Ed Sheeran"]` |
| `"Hip Hop"` | `["Kendrick Lamar", "Drake", "J. Cole"]` |
| `"R&B"` | `["SZA", "The Weeknd", "Usher"]` |
| `"Gospel"` | `["Kirk Franklin", "CeCe Winans", "Maverick City Music"]` |
| `"Jazz"` | `["Miles Davis", "Louis Armstrong", "Nina Simone"]` |
| `"Reggae"` | `["Bob Marley", "Sean Paul", "Shaggy"]` |
| `"Afrobeats"` | `["Burna Boy", "Wizkid", "Tems"]` |
| `"Amapiano"` | `["Kabza De Small", "DJ Maphorisa", "Tyler ICU"]` |

> **Important:** Dictionaries are the perfect data structure here because they give you direct, named access to each list. `genres["Pop"]` instantly returns the Pop artists list — much cleaner than using a nested list where you'd have to remember index positions.

---

### Step 4 — Get the User's Genre Choice

```python
choice = input("What genre do you like? (Pop/Hip Hop/R&B/Gospel/Jazz/Reggae/Afrobeats/Amapiano): ")
```

- `input()` pauses the program and waits for the user to type a genre and press **Enter**
- The typed genre is stored as a **string** in `choice`
- The prompt lists all valid options so the user knows exactly what to type

> **Important:** `input()` is **case-sensitive** by default. If the user types `"pop"` instead of `"Pop"`, it will not match the dictionary key and will fall into the `if choice not in genres` branch. A good improvement is to use `.title()` or `.strip()` on the input to handle common variations.

---

### Step 5 — Validate the Input

```python
if choice not in genres:
    print("Sorry, I don't know that genre.")
```

- The `in` operator checks whether `choice` exists as a **key** in the `genres` dictionary
- `not in` returns `True` if the key is **absent** from the dictionary
- If the genre is not found, a friendly error message is shown instead of crashing

> **Important:** Without this validation, accessing `genres[choice]` with an invalid key would raise a `KeyError` and crash the program. Always validate user input before using it to access a dictionary.

---

### Step 6 — Recommend a Random Artist

```python
else:
    print(f"Check out {random.choice(genres[choice])}")
```

- `genres[choice]` retrieves the **list of artists** for the chosen genre
- `random.choice()` picks **one random item** from that list
- The result is embedded in an f-string and printed as the recommendation

**Breaking it down:**
```python
genres["Afrobeats"]
# → ["Burna Boy", "Wizkid", "Tems"]

random.choice(["Burna Boy", "Wizkid", "Tems"])
# → "Wizkid"  (random pick each time)

f"Check out Wizkid"
# → "Check out Wizkid"
```

> **Important:** `random.choice()` picks from the list with **equal probability** — each artist has a 1-in-3 chance of being selected. Running the program multiple times with the same genre may return different artists.

---

## 📊 Example Outputs

### Example 1 — Valid Genre

```
MUSIC RECOMMENDER
What genre do you like? (Pop/Hip Hop/R&B/Gospel/Jazz/Reggae/Afrobeats/Amapiano): Afrobeats
Check out Burna Boy
```

### Example 2 — Different Run, Same Genre

```
MUSIC RECOMMENDER
What genre do you like? (Pop/Hip Hop/R&B/Gospel/Jazz/Reggae/Afrobeats/Amapiano): Afrobeats
Check out Tems
```

### Example 3 — Invalid Genre

```
MUSIC RECOMMENDER
What genre do you like? (Pop/Hip Hop/R&B/Gospel/Jazz/Reggae/Afrobeats/Amapiano): Country
Sorry, I don't know that genre.
```

### Example 4 — Case Mismatch

```
MUSIC RECOMMENDER
What genre do you like? (Pop/Hip Hop/R&B/Gospel/Jazz/Reggae/Afrobeats/Amapiano): pop
Sorry, I don't know that genre.
```

> This is a current limitation — input must match the exact capitalisation of the dictionary key.

---

---

## 🧠 Concepts Practised

| Concept | Where Used |
|---------|-----------|
| `import random` | Importing the random module |
| `print()` | Displaying the title and recommendation |
| Dictionaries | Mapping genres to lists of artists |
| Lists | Storing artists for each genre |
| `input()` | Getting the user's genre choice |
| `in` / `not in` | Checking if the genre exists in the dictionary |
| `if/else` | Handling valid and invalid input |
| `random.choice()` | Picking a random artist from the list |
| f-strings | Embedding the artist name in the output |

---

## 👩‍💻 Author

**Pauline Oraro**
60 Days of Python Challenge — Music Recommender Project
