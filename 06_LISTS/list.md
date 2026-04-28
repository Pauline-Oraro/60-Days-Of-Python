# Python Lists

A **list** is used to store multiple items in a single variable. Lists are created using square brackets `[]` and are **ordered**, **changeable**, and allow **duplicate values**.

```python
ThisList = ["pauline", "kate", "maggie"]
print(ThisList)  # ['pauline', 'kate', 'maggie']
```

---

## 1. List Properties

| Property | Description |
|----------|-------------|
| **Ordered** | Items have a defined order that does not change. New items are added to the end. |
| **Changeable** | Items can be added, removed, or modified after creation. |
| **Indexed** | Each item has an index starting at `0`. |
| **Allows Duplicates** | Items with the same value are permitted. |

```python
thisList = ["apple", "banana", "cherry", "apple", "cherry"]
print(thisList)       # ['apple', 'banana', 'cherry', 'apple', 'cherry']
print(len(thisList))  # 5
```

---

## 2. List Data Types

List items can be of **any** data type, and a single list can hold mixed types.

```python
list1 = ["mangoes", "pineapples", "oranges"]   # strings
list2 = [111, 222, 333, 444]                    # integers
list3 = [True, False, True, False]              # booleans
list4 = ["pauline", 20, True, "Nairobian", 44.5]  # mixed
```

To check the type of a list:

```python
myList = ["Nairobi", "Mombasa", "Kisumu"]
print(type(myList))  # <class 'list'>
```

You can also create a list using the `list()` constructor:

```python
newList = list((99, 88, 77, 66))
print(newList)  # [99, 88, 77, 66]
```

---

## 3. Accessing Items

### Positive Indexing

```python
students_Names = ["hillary", "mary", "jane", "max", "john"]
print(students_Names[0])  # hillary (first item)
print(students_Names[2])  # jane (third item)
```

### Negative Indexing

`-1` refers to the last item, `-2` the second last, and so on.

```python
print(students_Names[-1])  # john (last item)
print(students_Names[-3])  # jane (third from last)
```

### Range of Indexes (Slicing)

```python
print(students_Names[1:4])  # ['mary', 'jane', 'max'] (index 4 not included)
print(students_Names[:3])   # ['hillary', 'mary', 'jane'] (start to index 2)
print(students_Names[2:])   # ['jane', 'max', 'john'] (index 2 to end)
print(students_Names[-4:-1])# ['mary', 'jane', 'max'] (negative range)
```

### Check if Item Exists

```python
if "max" in students_Names:
    print("Yes, max is in the list")
```

---

## 4. Changing Items

### Change a Single Item

```python
fruits = ["apples", "bananas", "oranges", "strawberries", "berries"]
fruits[2] = "grapes"
print(fruits)  # ['apples', 'bananas', 'grapes', 'strawberries', 'berries']
```

### Change a Range of Items

```python
fruits[1:3] = ["kiwi", "mangoes"]
print(fruits)  # ['apples', 'kiwi', 'mangoes', 'strawberries', 'berries']
```

---

## 5. Adding Items

| Method | Description | Example |
|--------|-------------|---------|
| `.insert(i, item)` | Inserts item at specified index | `fruits.insert(2, "watermelon")` |
| `.append(item)` | Adds item to the end of the list | `fruits.append("pineapples")` |
| `.extend(list)` | Appends all items from another list | `fruits.extend(tropicalFruits)` |

```python
fruits.insert(2, "watermelon")
fruits.append("pineapples")

tropicalFruits = ["papaya", "guava", "passion fruit"]
fruits.extend(tropicalFruits)
```

---

## 6. Removing Items

| Method/Keyword | Description |
|----------------|-------------|
| `.remove(item)` | Removes the first occurrence of the specified item |
| `.pop(i)` | Removes item at specified index (removes last item if no index given) |
| `del list[i]` | Deletes the item at the specified index (can also delete the entire list) |
| `.clear()` | Empties the list but keeps the list object |

```python
fruits.remove("kiwi")    # removes by value
fruits.pop(2)             # removes by index
fruits.pop()              # removes last item
del fruits[0]             # deletes at index
fruits.clear()            # empties the list → []
```

---

## 7. Looping Through a List

### `for` Loop

```python
vegetables = ["cabbage", "spinach", "kale", "carrots", "broccoli"]
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

### List Comprehension (Shortest Syntax)

```python
[print(x) for x in vegetables]
```

---

## 8. Sorting Lists

### Ascending (Default)

```python
vegetables.sort()
numbers = [100, 50, 6, 82, 44]
numbers.sort()
```

### Descending

```python
vegetables.sort(reverse=True)
numbers.sort(reverse=True)
```

### Case-Insensitive Sort

```python
cars = ["Ford", "BMW", "Volvo", "audi", "mercedes"]
cars.sort(key=str.lower)
```

### Reverse Order (without sorting)

```python
cars.reverse()
```

---

## 9. Copying a List

> **Note:** You cannot copy a list with `copy2 = copy1` because it will only create a reference, not a new list. Use one of the methods below.

| Method | Example |
|--------|---------|
| `.copy()` | `names_copy = names.copy()` |
| `list()` constructor | `names_copy2 = list(names)` |
| Slice operator | `names_copy3 = names[:]` |

```python
names = ["pauline", "kate", "maggie"]
names_copy  = names.copy()
names_copy2 = list(names)
names_copy3 = names[:]
```

---

## 10. Joining Lists

### `+` Operator

```python
schoolList      = ["kinoo primary", "kinoo secondary", "kinoo academy"]
universityList  = ["university of nairobi", "strathmore university", "kenyatta university"]
educationList   = schoolList + universityList
print(educationList)
```

### `.append()` in a Loop

```python
for x in universityList:
    schoolList.append(x)
```

### `.extend()` Method

```python
schoolList.extend(universityList)
```

| Method | Best Used When |
|--------|----------------|
| `+` | Creating a new combined list |
| `.append()` in loop | Adding one item at a time from another iterable |
| `.extend()` | Adding all items from one list to another in-place |
