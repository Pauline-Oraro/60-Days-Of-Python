# 🍽️ Random Recipe Generator — Mini Project

A fun command-line Python application that generates random recipe ideas by combining ingredients and cooking methods. Every run produces a unique meal suggestion — great for when you can't decide what to cook!

---

## 📋 Project Overview

| Detail | Info |
|--------|------|
| **Project Type** | Mini Project — Command Line App |
| **Difficulty** | Beginner |
| **Concepts Used** | `import random`, lists, `while` loop, `break`, `random.choice()`, f-strings, `.lower()`, `.startswith()`, chained method calls |

---

## 💻 Full Code

```python
import random

print("RANDOM RECIPE GENERATOR")

proteins = ["chicken", "beef", "tofu", "fish", "eggs"]
veggies  = ["broccoli", "carrots", "spinach", "bell peppers", "mushrooms"]
carbs    = ["rice", "pasta", "potatoes", "quinoa", "bread"]
methods  = ["baked", "grilled", "stir-fried", "roasted", "sautéed"]
flavors  = ["garlic", "lemon", "spicy", "herb", "sweet & sour"]

while True:
    protein = random.choice(proteins)
    veggie  = random.choice(veggies)
    carb    = random.choice(carbs)
    method  = random.choice(methods)
    flavor  = random.choice(flavors)

    print(f"\nYour random recipe: {flavor} {method} {protein} with {veggie} and {carb}")

    if not input("\nGenerate another one? (y/n): ").lower().startswith("y"):
        print("Goodbye!")
        break
```

---

## 🔍 Step-by-Step Explanation

### Step 1 — Import the `random` Module

```python
import random
```

- The `random` module is a Python **built-in** — no installation required
- Imported at the very top so it is available throughout the entire program
- Used for `random.choice()` which picks one random item from each ingredient list

> **Important:** Always import modules at the **top of the file**. Python reads top to bottom — calling `random.choice()` before the import raises a `NameError`.

---

### Step 2 — Display the App Title

```python
print("RANDOM RECIPE GENERATOR")
```

- Prints the application name once at the start
- Sets context before the user interacts with the program

---

### Step 3 — Define the Ingredient and Method Lists

```python
proteins = ["chicken", "beef", "tofu", "fish", "eggs"]
veggies  = ["broccoli", "carrots", "spinach", "bell peppers", "mushrooms"]
carbs    = ["rice", "pasta", "potatoes", "quinoa", "bread"]
methods  = ["baked", "grilled", "stir-fried", "roasted", "sautéed"]
flavors  = ["garlic", "lemon", "spicy", "herb", "sweet & sour"]
```

- Five **lists** store the recipe building blocks — one for each component of a meal
- Each list is defined **outside** the loop so it is created once and reused on every iteration
- Defined at the top for easy editing — adding or removing ingredients only requires changing these lists

### List Overview

| List | Role in Recipe | Items | Count |
|------|---------------|-------|-------|
| `proteins` | Main ingredient | `chicken`, `beef`, `tofu`, `fish`, `eggs` | 5 |
| `veggies` | Side vegetable | `broccoli`, `carrots`, `spinach`, `bell peppers`, `mushrooms` | 5 |
| `carbs` | Base/starch | `rice`, `pasta`, `potatoes`, `quinoa`, `bread` | 5 |
| `methods` | Cooking technique | `baked`, `grilled`, `stir-fried`, `roasted`, `sautéed` | 5 |
| `flavors` | Seasoning/style | `garlic`, `lemon`, `spicy`, `herb`, `sweet & sour` | 5 |

> **Important:** With 5 options in each of 5 lists, the generator can produce **5 × 5 × 5 × 5 × 5 = 3,125 unique combinations**. Adding just one more item to each list increases that to **6⁵ = 7,776 combinations**. The combinatorial power grows fast!

---

### Step 4 — Start an Infinite Loop

```python
while True:
```

- Creates an **infinite loop** that keeps generating recipes until the user says no
- The number of iterations is unknown in advance — the user decides when to stop
- Exited with a `break` statement at the end of each iteration

---

### Step 5 — Pick a Random Item from Each List

```python
protein = random.choice(proteins)
veggie  = random.choice(veggies)
carb    = random.choice(carbs)
method  = random.choice(methods)
flavor  = random.choice(flavors)
```

- `random.choice()` picks **one random item** from a list — each item has an equal probability of being selected
- Five separate calls, one per ingredient category
- Each call is **independent** — the choice of protein has no effect on the choice of veggie, carb, or any other component
- All five selections happen fresh every time the loop runs

| Variable | Example Value | Source List |
|----------|--------------|-------------|
| `protein` | `"chicken"` | `proteins` |
| `veggie` | `"mushrooms"` | `veggies` |
| `carb` | `"pasta"` | `carbs` |
| `method` | `"grilled"` | `methods` |
| `flavor` | `"lemon"` | `flavors` |

> **Important:** `random.choice()` selects with **equal probability** — every item in the list has the same chance of being picked. If you want some ingredients to appear more often than others, you can add them to the list multiple times or use `random.choices()` with a `weights` parameter.

---

### Step 6 — Build and Print the Recipe

```python
print(f"\nYour random recipe: {flavor} {method} {protein} with {veggie} and {carb}")
```

- An **f-string** assembles all five random choices into one readable recipe sentence
- `\n` at the start adds a blank line before the recipe for visual spacing
- The order `flavor → method → protein → veggie → carb` produces a natural-sounding recipe name

**How the recipe string is assembled:**

```
flavor  = "lemon"
method  = "grilled"
protein = "chicken"
veggie  = "mushrooms"
carb    = "pasta"

→ "lemon grilled chicken with mushrooms and pasta"
```

> **Important:** The order in which the variables appear in the f-string determines how the recipe reads. `{flavor} {method} {protein}` reads like a real dish name — `"garlic roasted tofu"`. Swapping the order would produce less natural results like `"roasted garlic tofu"` or `"tofu garlic roasted"`.

---

### Step 7 — Ask to Generate Another Recipe

```python
if not input("\nGenerate another one? (y/n): ").lower().startswith("y"):
    print("Goodbye!")
    break
```

This is the most compact line in the program — three methods chained together in a single `if` statement. Let's break it down:

#### Step-by-step chain breakdown

```python
input("\nGenerate another one? (y/n): ")
```
Gets the user's response as a string.

```python
.lower()
```
Converts the response to lowercase — so `"Y"`, `"Yes"`, `"YES"` all work.

```python
.startswith("y")
```
Returns `True` if the response begins with `"y"` — accepts `"yes"`, `"yeah"`, `"yup"`, `"y"`.

```python
not ... 
```
Reverses the result — if it does **not** start with `"y"`, the `if` block runs.

```python
if not ...:
    print("Goodbye!")
    break
```
Prints `"Goodbye!"` and exits the loop.

> **Important:** This entire condition is evaluated in **one line** using method chaining. It is equivalent to the more verbose version:
> ```python
> response = input("\nGenerate another one? (y/n): ")
> response = response.lower()
> if not response.startswith("y"):
>     print("Goodbye!")
>     break
> ```
> Chaining is more concise but requires understanding that each method returns a value that the next method acts on. Both approaches produce identical results.

| User Response | `.lower()` | `.startswith("y")` | `not ...` | Action |
|---------------|-----------|-------------------|----------|--------|
| `"y"` | `"y"` | `True` | `False` | Generate again |
| `"yes"` | `"yes"` | `True` | `False` | Generate again |
| `"Yeah"` | `"yeah"` | `True` | `False` | Generate again |
| `"n"` | `"n"` | `False` | `True` | Goodbye + break |
| `"no"` | `"no"` | `False` | `True` | Goodbye + break |
| `""` (Enter) | `""` | `False` | `True` | Goodbye + break |

---

## 📊 Recipe Assembly Diagram

```
proteins  →  random.choice()  →  "fish"
veggies   →  random.choice()  →  "spinach"
carbs     →  random.choice()  →  "quinoa"
methods   →  random.choice()  →  "roasted"
flavors   →  random.choice()  →  "herb"
                    ↓
f-string: "herb roasted fish with spinach and quinoa"
```

---

## 📊 Example Output

### Example 1 — Single Recipe

```
RANDOM RECIPE GENERATOR

Your random recipe: garlic grilled chicken with broccoli and rice

Generate another one? (y/n): n
Goodbye!
```

### Example 2 — Multiple Recipes

```
RANDOM RECIPE GENERATOR

Your random recipe: spicy stir-fried tofu with bell peppers and noodles

Generate another one? (y/n): y

Your random recipe: lemon baked fish with spinach and quinoa

Generate another one? (y/n): y

Your random recipe: sweet & sour roasted beef with mushrooms and potatoes

Generate another one? (y/n): n
Goodbye!
```

### Example 3 — Same Ingredient Twice (Possible)

```
Your random recipe: herb grilled chicken with broccoli and rice

Generate another one? (y/n): y

Your random recipe: herb grilled chicken with carrots and pasta
```

> Since each `random.choice()` is independent, the same protein, method, or flavor can appear in consecutive recipes.

---

## 🧠 Concepts Practised

| Concept | Where Used |
|---------|-----------|
| `import random` | Importing the random module |
| Lists | Storing each ingredient and method category |
| `while True` | Keeping the generator running |
| `break` | Stopping when user declines another recipe |
| `random.choice()` | Picking a random item from each list |
| f-strings | Assembling the full recipe sentence |
| `.lower()` | Making the continue check case-insensitive |
| `.startswith()` | Flexible yes-detection for play-again |
| Method chaining | Combining `input()`, `.lower()`, `.startswith()` in one line |
| `\n` in strings | Adding blank lines for visual spacing |

---

## 👩‍💻 Author

**Pauline Oraro**
60 Days of Python Challenge — Recipe Generator Project
