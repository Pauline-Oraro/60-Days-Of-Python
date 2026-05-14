# Simple Calculator

A command-line calculator written in Python that supports basic arithmetic operations.

---

## Features

- Addition
- Subtraction
- Multiplication
- Division (with division-by-zero protection)
- Recursive loop to perform multiple calculations in one session

---

## Functions

### `add(x, y)`

Returns the sum of `x` and `y`.

### `subtract(x, y)`

Returns the difference of `x` and `y`.

### `multiply(x, y)`

Returns the product of `x` and `y`.

### `divide(x, y)`

Returns the quotient of `x` divided by `y`.  
Returns an error message if `y` is `0`.

### `main()`

Entry point of the program. Handles user interaction including:

- Displaying the menu
- Validating operation choice
- Accepting and validating numeric inputs
- Displaying the result
- Prompting to perform another calculation

---

## Usage

Run the script directly with Python:

```bash
python calculator.py
```

### Example Session

```
SIMPLE CALCULATOR
Select operation:
1. ADDITION
2. SUBTRACTION
3. MULTIPLICATION
4. DIVISION

Enter choice (1-4): 1
Enter first number: 10
Enter second number: 5

10.0 + 5.0 = 15.0

Do you want to perform another calculation? (yes/no): no
Goodbye
```

---

## Error Handling

| Scenario | Behaviour |
|---|---|
| Invalid menu choice (not 1–4) | Prompts the user to re-enter a valid option |
| Non-numeric input for numbers | Prints an error and exits the current session |
| Division by zero | Returns `"Error! Division by zero is not allowed."` |

---

## Notes

- All number inputs are cast to `float`, so both integers and decimals are supported.
- The program recurses into `main()` when the user chooses to continue, which may cause a `RecursionError` after a very large number of consecutive calculations. Refactoring with a `while` loop is recommended for production use.
