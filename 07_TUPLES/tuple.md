# Python Tuples

A **tuple** is used to store multiple items in a single variable. Tuples are written with round brackets `()` and are **ordered**, **unchangeable**, and allow **duplicate values**.

```python
myTuple = ("kate", "john", "michael")
print(myTuple)  # ('kate', 'john', 'michael')

thisTuple = ("kate", "george", "maria", "kate", "michael", "maria")
print(thisTuple)
print(len(thisTuple))  # 6
```

---

## 1. Tuple Properties

| Property | Description |
|----------|-------------|
| **Ordered** | Items have a defined order that does not change. |
| **Unchangeable** | Items cannot be changed, added, or removed after creation. |
| **Indexed** | Each item has an index starting at `0`. |
| **Allows Duplicates** | Items with the same value are permitted. |

---

## 2. Creating Tuples

### Single-Item Tuple

To create a tuple with only one item, you **must** add a trailing comma — otherwise Python will not recognize it as a tuple.

```python
myList = ("wonder",)
print(type(myList))  # <class 'tuple'>
```

### Mixed Data Types

Tuple items can be of any data type.

```python
tuple1 = ("apple", "banana", "cherry")  # strings
tuple2 = (1, 5, 7, 9, 3)               # integers
tuple3 = (True, False, False)           # booleans
```

### Using the `tuple()` Constructor

```python
myGroceryList = tuple(("milk", "bread", "eggs"))
print(myGroceryList)  # ('milk', 'bread', 'eggs')
```

---

## 3. Accessing Items

### Positive Indexing

```python
myFruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(myFruits[1])   # banana
```

### Negative Indexing

`-1` refers to the last item, `-2` the second last, and so on.

```python
print(myFruits[-1])  # mango
```

### Range of Indexes (Slicing)

```python
print(myFruits[2:5])    # ('cherry', 'orange', 'kiwi')
print(myFruits[-4:-1])  # ('orange', 'kiwi', 'melon')
```

### Check if Item Exists

```python
if "apple" in myFruits:
    print("Yes, 'apple' is in the fruits tuple")
```

---

## 4. Updating Tuples

Tuples are **unchangeable**, but you can work around this by converting to a list, making changes, and converting back.

### Change an Item

```python
cars = ("ford", "toyota", "honda")
carsList = list(cars)
carsList[0] = "nissan"
cars = tuple(carsList)
print(cars)  # ('nissan', 'toyota', 'honda')
```

### Add an Item

```python
names = ("kate", "pauline", "john")
namesList = list(names)
namesList.append("mary")
names = tuple(namesList)
print(names)  # ('kate', 'pauline', 'john', 'mary')
```

### Join Two Tuples

You can concatenate tuples directly using `+`.

```python
tupleA = ("a", "b", "c")
tupleB = (1, 2, 3)
tupleC = tupleA + tupleB
print(tupleC)  # ('a', 'b', 'c', 1, 2, 3)
```

### Remove an Item

```python
letters = ("a", "b", "c", "d", "e")
lettersList = list(letters)
lettersList.remove("c")
letters = tuple(lettersList)
print(letters)  # ('a', 'b', 'd', 'e')
```

> **Pattern:** Convert → Modify → Convert back. This is the standard workflow for any tuple mutation.

---

## 5. Unpacking Tuples

**Packing** is assigning values into a tuple. **Unpacking** is extracting those values back into individual variables.

### Basic Unpacking

```python
places = ("nairobi", "mombasa", "kisumu")
(city1, city2, city3) = places
print(city1)  # nairobi
print(city2)  # mombasa
print(city3)  # kisumu
```

### Unpacking with `*` (Collect Remaining Values)

If there are more values than variables, use `*` to collect the remaining values into a list.

```python
capitalCity = ("Nairobi", "Dodoma", "Addis Ababa", "Kampala", "Mogadishu")
(capital1, capital2, *capital3) = capitalCity
print(capital1)   # Nairobi
print(capital2)   # Dodoma
print(capital3)   # ['Addis Ababa', 'Kampala', 'Mogadishu']
```

---

## 6. Looping Through a Tuple

### `for` Loop

```python
vegetables = ("Broccoli", "celery", "kale", "peas", "butternut")
for x in vegetables:
    print(x)
```

### `for` Loop with Index

```python
for i in range(len(vegetables)):
    print(vegetables[i])
```

### `while` Loop

```python
i = 0
while i < len(vegetables):
    print(vegetables[i])
    i += 1
```

---

## 7. Joining Tuples

### `+` Operator — Concatenate

```python
students  = ("liam", "zawadi", "jack", "mary")
lecturers = ("john", "peter", "lucy")
university = students + lecturers
print(university)  # ('liam', 'zawadi', 'jack', 'mary', 'john', 'peter', 'lucy')
```

### `*` Operator — Multiply

Repeat the contents of a tuple a given number of times.

```python
studentsNames = students * 2
print(studentsNames)  # ('liam', 'zawadi', 'jack', 'mary', 'liam', 'zawadi', 'jack', 'mary')
```

---

## Tuples vs Lists

| Feature | Tuple `()` | List `[]` |
|---------|-----------|----------|
| Ordered | ✅ | ✅ |
| Allows Duplicates | ✅ | ✅ |
| Changeable | ❌ | ✅ |
| Performance | Faster | Slower |
| Use Case | Fixed data | Dynamic data |
