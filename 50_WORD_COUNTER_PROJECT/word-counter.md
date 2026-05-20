# 📝 Word Counter & Text Analyzer

A lightweight, interactive command-line tool written in Python that analyzes text and provides detailed statistics including word count, character count, sentence count, and estimated reading time.

---

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Output Example](#output-example)
- [Function Reference](#function-reference)

---

## Features

- **Word Count** — Counts total number of words in the text
- **Character Count** — Reports characters both with and without spaces
- **Sentence Count** — Detects sentences ending with `.`, `!`, or `?`
- **Average Words per Sentence** — Calculates sentence complexity
- **Average Characters per Word** — Measures word length
- **Reading Time Estimate** — Estimates reading time based on an average reading speed of 225 words per minute, displayed in seconds (for short texts) or minutes (for longer texts)
- **Interactive CLI Loop** — Keeps running until the user chooses to exit

---

## Requirements

- Python 3.x (no external libraries required — uses only the Python standard library)

---

## Usage

Run the script from your terminal:

```bash
python word_counter.py
```

You will be greeted with a menu:

```
==== Word Counter ====
Count words, characters, and sentences in your text

Choose an option:
1. Enter text to analyze
2. Exit

Your choice (1/2):
```

**To analyze text:**

1. Enter `1` and press Enter.
2. Paste or type your text. Press **Enter twice** when done.
3. The analysis results will be printed immediately.
4. You will be returned to the menu to analyze another piece of text or exit.

**To exit:**

Enter `2` and press Enter.

---

## Output Example

Given the input:

> *The quick brown fox jumps over the lazy dog. It was a bright sunny day! Was the fox really that quick?*

The tool outputs:

```
===== Text Analysis Results =====
•  Words: 20
•  Characters (with spaces): 101
•  Characters (without spaces): 82
•  Sentences: 3
•  Average words per sentence: 6.7
•  Average characters per word: 5.1
•  Estimated reading time: 5 seconds
```

---

## Function Reference

### `count_words(text: str) -> int`

Splits the input string on whitespace and returns the total number of words.

```python
count_words("Hello world")  # Returns: 2
```

---

### `count_characters(text: str, include_spaces: bool) -> int`

Returns the number of characters in the text.

- If `include_spaces=True`, counts all characters including spaces.
- If `include_spaces=False`, strips spaces before counting.

```python
count_characters("Hello world", True)   # Returns: 11
count_characters("Hello world", False)  # Returns: 10
```

---

### `count_sentences(text: str) -> int`

Counts the number of sentences by scanning for sentence-ending punctuation (`.`, `!`, `?`).

- If no punctuation is found but the text is non-empty, it assumes there is at least one sentence.

```python
count_sentences("Hello! How are you?")  # Returns: 2
count_sentences("No punctuation here")  # Returns: 1
count_sentences("")                      # Returns: 0
```

---

### `analyze_text(text: str) -> None`

Orchestrates all analysis functions and prints a formatted summary report to the console. Computes:

- Word count
- Character counts (with and without spaces)
- Sentence count
- Average words per sentence
- Average characters per word
- Estimated reading time (in seconds if under 1 minute, otherwise in minutes)

---

### `main() -> None`

Entry point for the program. Displays the main menu in an infinite loop, collects multi-line text input from the user, and dispatches to `analyze_text()`. Exits cleanly when the user selects option `2`.

---
