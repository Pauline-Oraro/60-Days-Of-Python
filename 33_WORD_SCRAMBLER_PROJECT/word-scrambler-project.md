# 🧩 Word Scrambler (Python)

A simple Python command-line program that takes a word as input and returns a scrambled (shuffled) version of it. This project demonstrates basic concepts such as loops, user input handling, string manipulation, and randomness.

---

## 📌 Features

* Accepts user input dynamically
* Randomly shuffles characters in a word
* Runs continuously until the user exits
* Beginner-friendly implementation
* Uses Python’s built-in `random` module

---

## 💻 Example Usage

```text
WORD SCRAMBLER
Enter a word to scramble (or 'quit'): hello
Scrambled: olleh

Enter a word to scramble (or 'quit'): python
Scrambled: nhtopy

Enter a word to scramble (or 'quit'): quit
Goodbye!
```

---

## 🧠 How It Works

1. The program enters an infinite loop using `while True`
2. It prompts the user to enter a word
3. If the user types `"quit"`, the loop exits
4. Otherwise:

   * The word is converted into a list of characters
   * `random.shuffle()` rearranges the list in place
   * The characters are joined back into a string
5. The scrambled result is displayed

---

## 📄 Source Code

```python
import random

print("WORD SCRAMBLER")

while True:
    word = input("Enter a word to scramble (or 'quit'): ")
    
    if word.lower() == "quit":
        print("Goodbye!")
        break

    letters = list(word)
    random.shuffle(letters)
    print(f"Scrambled: {''.join(letters)}")
```

---

## 📚 Concepts Covered

* Loops (`while`)
* Conditional statements (`if`)
* String manipulation
* Lists and list operations
* Randomization (`random.shuffle`)
* User input/output

---

## 📜 License

This project is open-source and free to use for learning purposes.

---

## 🙌 Acknowledgements

Built as a beginner-friendly Python exercise to practice core programming concepts.

---
