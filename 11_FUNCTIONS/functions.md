# Python Functions

A **function** is a block of code that only runs when it is called. Functions help avoid code repetition — write once, reuse many times. A function can also return data as a result.

---

## 1. Defining & Calling a Function

Use the `def` keyword followed by the function name and parentheses.

### Naming Rules

| Rule | Example |
|------|---------|
| Must start with a letter or underscore | `my_func`, `_helper` |
| Can only contain letters, numbers, and underscores | `calc_total2` |
| Case-sensitive | `myFunction` ≠ `myfunction` |
| Use descriptive names | `fahrenheit_to_celsius` not `f2c` |

```python
def my_function():
    print("This is a function")

my_function()  # calling the function
```

### Calling a Function Multiple Times

```python
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(88))  # 31.11
print(fahrenheit_to_celsius(50))  # 10.0
print(fahrenheit_to_celsius(90))  # 32.22
print(fahrenheit_to_celsius(60))  # 15.55
```

---

## 2. The `return` Statement

Functions send data back using `return`. When a `return` is reached, the function stops executing and sends the result back. If no `return` is present, the function returns `None` by default.

```python
def greeting():
    return "Hello from this function"

message = greeting()
print(message)      # Hello from this function
print(greeting())   # can also use the return value directly
```

---

## 3. The `pass` Statement

Function definitions cannot be empty. Use `pass` as a placeholder when the logic hasn't been implemented yet.

```python
def this_function():
    pass   # TODO: implement later
```

---

## 4. Function Arguments

Information is passed into functions as **arguments**. You can add as many as needed, separated by commas.

> **Parameter** = variable listed in the function definition.  
> **Argument** = actual value passed when the function is called.

```python
def my_name(name):          # 'name' is a parameter
    print(name + " : This is my name")

my_name("Pauline Akinyi Oraro")  # "Pauline Akinyi Oraro" is an argument
```

---

### Default Parameter Values

If a function is called without an argument, it uses the default value.

```python
def student_name(name="john"):
    print("Hello", name)

student_name()          # Hello john
student_name("oraro")   # Hello oraro
student_name("kate")    # Hello kate
```

---

### Keyword Arguments (`key=value`)

Pass arguments in any order using the `key=value` syntax.

```python
def my_pet(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_pet(animal="cat", name="Kiri")   # order doesn't matter
```

---

### Positional Arguments

Arguments passed without keywords — **order matters**.

```python
def my_cat(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_cat("cat", "maxy")   # must be in correct order
```

---

### Mixing Positional and Keyword Arguments

Positional arguments must always come **before** keyword arguments.

```python
def my_information(name, age, course):
    print("My name is", name, "and I am", age, "years old. I do", course)

my_information("Pauline Oraro", age=20, course="Bachelor of science in IT")
```

---

### Positional-Only Arguments (`/`)

Adding `/` after the parameters forces them to be positional only. Using keyword syntax will raise an error.

```python
def student(name, /):
    print("Hello", name)

student("mary")           # works
# student(name="mary")   # raises an error
```

---

### Keyword-Only Arguments (`*`)

Adding `*` before the parameters forces them to be keyword only. Using positional syntax will raise an error.

```python
def my_students(*, name):
    print("Hello", name)

my_students(name="jack")  # works
# my_students("jack")     # raises an error
```

---

### Combining Both (`/` and `*`)

Arguments before `/` are **positional only**. Arguments after `*` are **keyword only**.

```python
def my_numbers(a, b, /, *, c, d):
    return a + b + c + d

result = my_numbers(11, 22, c=33, d=44)
print(result)  # 110
```

---

### Passing Any Data Type as an Argument

```python
def my_fruits(fruits):
    for fruit in fruits:
        print(fruit)

my_fruit = ["cherries", "bananas", "apples"]
my_fruits(my_fruit)
# cherries
# bananas
# apples
```

---

## 5. `*args` and `**kwargs`

Use these when you don't know how many arguments will be passed.

### `*args` — Unknown Number of Positional Arguments

The `*` prefix lets a function accept any number of positional arguments, collected into a tuple.

```python
def my_children(*kids):
    print("The youngest child is " + kids[2])

my_children("jack", "azriel", "dylan")
# The youngest child is dylan
```

### `**kwargs` — Unknown Number of Keyword Arguments

The `**` prefix lets a function accept any number of keyword arguments, collected into a dictionary.

```python
def his_children(**kid):
    print("His last child is called " + kid["lname"])

his_children(fname="Pauline", sname="oraro", lname="akinyi")
# His last child is called akinyi
```

### Summary

| Syntax | Name | Accepts | Collected as |
|--------|------|---------|--------------|
| `*args` | Arbitrary positional args | Any number of values | Tuple |
| `**kwargs` | Arbitrary keyword args | Any number of key=value pairs | Dictionary |

---

## 6. Python Scope

A variable is only available within the region it is created — this is called **scope**.

### Local Scope

A variable created inside a function is only available within that function (and any inner functions nested inside it).

```python
def myfunc():
    x = 777
    print(x)   # 777

myfunc()
# print(x)   # would raise an error — x doesn't exist here

def mynumber():
    y = 44
    def myinnerfunc():
        print(y)   # inner function can access y
    myinnerfunc()

mynumber()  # 44
```

### Global Scope

A variable created in the **main body** of the Python code belongs to the global scope and is available everywhere, including inside functions.

```python
a = 99

def myfunctions():
    print(a)   # can access global variable

myfunctions()  # 99
print(a)       # 99
```

### Scope Summary

| Scope | Where Created | Accessible From |
|-------|---------------|-----------------|
| **Local** | Inside a function | Only within that function (and nested inner functions) |
| **Global** | Main body of the script | Anywhere in the program |
