# 🤖 ChatBot — A Simple Python Conversational Bot

A lightweight, interactive command-line chatbot built with Python. No external libraries required — just pure Python fun!

---

## Overview

ChatBot is a simple terminal-based conversational bot that responds to user input with jokes, fun facts, and friendly conversation. It uses Python's built-in `random` and `time` modules to deliver a varied, engaging experience on every run.

---

## ✨ Features

- 👋 Randomised greetings and farewells for variety
- 😂 Built-in joke library for a quick laugh
- 🧠 Fun facts to learn something new each session
- 🎨 Colour preference mini-conversation
- 🔄 Graceful exit with a personalised goodbye
- 💬 Fallback responses for unrecognised input

---

## Usage

When the program starts, you will be prompted to enter your name. After that, type any of the supported commands (or just chat freely!) and the bot will respond.

```
Welcome to ChatBot!
I can chat about:
  'joke'  - Hear a funny joke
  'fact'  - Learn something new
  'color' - My favorite color
  'bye'   - End our chat

What is your name: Alex
ChatBot: Nice to meet you, Alex! How can I help you today?
You: can you tell me a joke
ChatBot: Why don't scientists trust atoms? Because they make up everything! 🤣
You: bye
ChatBot: Goodbye! 👋
ChatBot: It was fun chatting with you, Alex
```

---

## 💬 Commands

| Input | Description |
|---|---|
| `hi`, `hello`, `hey`, `howdy` | Receive a random greeting |
| `joke` | Get a random joke |
| `fact` | Learn a random fun fact |
| `color` | Chat about favourite colours |
| `bye`, `goodbye`, `exit`, `quit` | End the conversation |
| Anything else | Receive a random fallback response |

> **Note:** Commands are case-insensitive and extra whitespace is ignored.

---

## 🛠️ Customisation

You can easily extend the bot by editing the lists inside `chatbot()`:

- **Add more jokes** — append to the `jokes` list
- **Add more facts** — append to the `facts` list
- **Add new commands** — add an `elif` branch in the `while chatting` loop

---
