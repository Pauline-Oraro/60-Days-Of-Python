# Word Association Game

A terminal-based word association game written in Python. Players are prompted with a word and must respond with a related word — the faster they answer, the more points they earn.

## Code Walkthrough

### Step 1 — Import Libraries

```python
import random
import time
```

Two modules from Python's standard library are imported:

- `random` — used to pick a random prompt word each round so the game doesn't repeat in a predictable order.
- `time` — used to measure how long the player takes to respond, which directly affects their score.

---

### Step 2 — Define the Word Bank

```python
word_pairs = {
    "sky": ["blue", "cloud", "bird", "fly", "sun"],
    "water": ["drink", "ocean", "swim", "fish", "boat"],
    ...
}
```

`word_pairs` is a dictionary where each **key** is a prompt word and its **value** is a list of accepted associated words. When the player's input matches any word in the list, the answer is counted as correct. This structure makes it easy to add or remove word sets without changing any game logic.

---

### Step 3 — Print the Welcome Message

```python
print("\nWORD ASSOCIATION GAME")
print("Respond with a related word to the given word")
```

A simple header is printed once at the start of the game to greet the player and explain the objective. The `\n` at the beginning adds a blank line for readability in the terminal.

---

### Step 4 — Initialise Score Trackers

```python
score = 0
rounds = 0
```

Two counters are set to zero before the game loop begins:

- `score` — accumulates the player's earned points across all rounds.
- `rounds` — tracks how many rounds have been played, used to calculate the total possible points at the end of each round.

---

### Step 5 — Start the Game Loop

```python
while True:
```

An infinite loop keeps the game running round after round. The loop only exits when the player chooses to stop (handled in the final step). Every iteration of this loop is one complete round of the game.

---

### Step 6 — Pick a Random Prompt Word

```python
prompt = random.choice(list(word_pairs.keys()))
related_words = word_pairs[prompt]
```

`random.choice()` selects one key at random from the dictionary. `word_pairs.keys()` returns the keys as a view, so it is first converted to a `list` since `random.choice()` requires a sequence. The associated word list for that prompt is stored in `related_words` for use in the answer check later.

---

### Step 7 — Display the Prompt to the Player

```python
print(f"\nPrompt word: {prompt.upper()}")
print("Type a word related to this prompt")
```

The chosen prompt word is printed in uppercase using `.upper()` to make it visually distinct and easy to read. A second line instructs the player to type their answer.

---

### Step 8 — Capture the Player's Response and Time It

```python
start_time = time.time()
response = input("> ").lower().strip()
response_time = time.time() - start_time
```

`time.time()` records the current timestamp in seconds just before `input()` pauses for the player to type. Once they press Enter, `time.time()` is called again and the difference gives the elapsed response time in seconds. The player's input is immediately normalised with `.lower()` (converts to lowercase) and `.strip()` (removes leading/trailing whitespace) so that `"  Blue "`, `"BLUE"`, and `"blue"` all match equally.

---

### Step 9 — Check the Answer and Award Points

```python
print("response time", response_time)

if response in related_words:
    points = max(1, 5 - int(response_time))
    score += points
    print(f"Good association +{points} points (answered in {response_time:.1f}s)")
else:
    print(f"Not a common association. Related words included: {', '.join(related_words)}")
```

The normalised response is checked against `related_words` using the `in` operator. If it matches:

- `int(response_time)` floors the elapsed seconds to a whole number (e.g. `2.8s → 2`).
- `5 - int(response_time)` calculates the base points (e.g. `5 - 2 = 3`).
- `max(1, ...)` guarantees at least 1 point regardless of how long the player took.

If the answer doesn't match, the player is shown all valid associations so they can learn for next time.

### Scoring Table

| Response Time | Points Earned |
|---|---|
| Under 1 second | 5 points |
| 1–2 seconds | 4 points |
| 2–3 seconds | 3 points |
| 3–4 seconds | 2 points |
| 4+ seconds | 1 point |

---

### Step 10 — Update and Display the Round Score

```python
rounds += 1
print(f"Score: {score}/{rounds * 5} possible points")
```

`rounds` is incremented by 1 after each answer. The score is then displayed as `earned / possible`, where possible points equals `rounds × 5` (since each round has a maximum of 5 points). This gives the player a clear picture of their performance over time.

---

### Step 11 — Ask to Play Again or Exit

```python
if input("\nPlay again? (yes/no): ").lower().startswith('n'):
    print(f"Final Score: {score}. Thanks for playing!")
    break
```

The player is asked if they want to continue. `.lower().startswith('n')` means any response beginning with `n` — such as `"no"`, `"nope"`, or just `"n"` — triggers the exit. A final score message is printed and `break` exits the `while True` loop, ending the program.

## Word Bank

The game includes 8 prompt words, each with 5 valid associations:

| Prompt | Valid Associations |
|---|---|
| sky | blue, cloud, bird, fly, sun |
| water | drink, ocean, swim, fish, boat |
| food | eat, cook, tasty, meal, restaurant |
| music | song, dance, listen, band, rhythm |
| book | read, story, page, author, library |
| tree | leaf, green, forest, wood, shade |
| car | drive, road, wheel, travel, speed |
| dog | pet, bark, walk, loyal, puppy |

## Gameplay Example

```
WORD ASSOCIATION GAME
Respond with a related word to the given word

Prompt word: MUSIC
Type a word related to this prompt
> dance
response time 1.2394...
Good association +4 points (answered in 1.2s)
Score: 4/5 possible points

Play again? (yes/no): yes

Prompt word: TREE
Type a word related to this prompt
> forest
response time 0.8712...
Good association +5 points (answered in 0.9s)
Score: 9/10 possible points

Play again? (yes/no): no
Final Score: 9. Thanks for playing!
```

Each key is a prompt word and its value is a list of accepted responses.
