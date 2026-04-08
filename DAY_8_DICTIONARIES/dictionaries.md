# Python Dictionaries

A **dictionary** is used to store data in **key:value pairs**. Dictionaries are written with curly brackets `{}` and are **ordered**, **changeable**, and do **not allow duplicate keys**.

```python
myCarBrand = {
    "brand": "Mercedes",
    "model": "AMG",
    "year": 2023
}
print(myCarBrand)           # {'brand': 'Mercedes', 'model': 'AMG', 'year': 2023}
print(myCarBrand["brand"])  # Mercedes
print(len(myCarBrand))      # 3
```

---

## 1. Dictionary Properties

| Property | Description |
|----------|-------------|
| **Ordered** | Items have a defined order that does not change. |
| **Changeable** | Items can be added, changed, or removed after creation. |
| **No Duplicates** | Two items cannot share the same key. Duplicates overwrite existing values. |

---

## 2. Creating Dictionaries

### Mixed Data Types

Dictionary values can be of any data type, including lists.

```python
student = {
    "name": "Pauline Oraro",
    "course": "Bachelor of science in information technology",
    "year": 2025,
    "languages": ["english", "swahili", "luo"]
}
print(type(student))  # <class 'dict'>
```

### Using the `dict()` Constructor

```python
studentOne = dict(name="kate", age=20, country="Tanzania")
print(studentOne)  # {'name': 'kate', 'age': 20, 'country': 'Tanzania'}
```

---

## 3. Accessing Items

```python
studentTwo = {
    "name": "Miguel",
    "age": 23,
    "course": "Bachelor of science in game development",
    "year": 2026
}
```

| Method | Description | Example |
|--------|-------------|---------|
| `dict[key]` | Access value by key name | `studentTwo["course"]` |
| `.get(key)` | Access value using get method | `studentTwo.get("year")` |
| `.keys()` | Returns all keys as a list | `studentTwo.keys()` |
| `.values()` | Returns all values as a list | `studentTwo.values()` |
| `.items()` | Returns all key-value pairs as tuples | `studentTwo.items()` |

```python
print(studentTwo["course"])   # Bachelor of science in game development
print(studentTwo.get("year")) # 2026
print(studentTwo.keys())      # dict_keys(['name', 'age', 'course', 'year'])
print(studentTwo.values())    # dict_values(['Miguel', 23, '...', 2026])
print(studentTwo.items())     # dict_items([('name', 'Miguel'), ...])
```

### Check if a Key Exists

```python
if "course" in studentTwo:
    print("Yes, 'course' is one of the keys in studentTwo dictionary")
```

---

## 4. Changing Items

### Change a Specific Value

```python
studentTwo["year"] = 2024
print(studentTwo)
```

### Using `.update()`

The `.update()` method updates the dictionary with the given key:value pairs.

```python
studentTwo.update({"course": "Bachelor of science in software development"})
print(studentTwo)
```

---

## 5. Adding Items

### New Index Key

```python
studentTwo["campus"] = "Main Campus"
print(studentTwo)
```

### Using `.update()` — Adds if Key Doesn't Exist

```python
studentTwo.update({"favourite-color": "blue"})
print(studentTwo)
```

---

## 6. Removing Items

| Method/Keyword | Description |
|----------------|-------------|
| `.pop(key)` | Removes the item with the specified key |
| `.popitem()` | Removes the last inserted item |
| `del dict[key]` | Deletes the item with the specified key |
| `.clear()` | Empties the dictionary but keeps the object |

```python
studentTwo.pop("course")     # removes 'course'
studentTwo.popitem()          # removes last inserted item
del studentTwo["campus"]      # removes 'campus'
studentTwo.clear()            # empties → {}
```

---

## 7. Looping Through a Dictionary

```python
myName = {
    "FirstName": "Pauline",
    "MiddleName": "Akinyi",
    "SurName": "Oraro",
    "NickName": "Hiltra"
}
```

### Loop Through Keys (Default)

```python
for x in myName:
    print(x)          # prints all key names

for m in myName.keys():
    print(m)          # same result using .keys()
```

### Loop Through Values

```python
for y in myName:
    print(myName[y])  # access values via key

for z in myName.values():
    print(z)          # same result using .values()
```

### Loop Through Key-Value Pairs

```python
for a, b in myName.items():
    print(a, b)       # prints both key and value
```

---

## 8. Copying a Dictionary

> **Note:** You cannot copy a dictionary with `copy2 = copy1` — this creates a reference, not a new object.

| Method | Example |
|--------|---------|
| `.copy()` | `copiedInformation = realInformation.copy()` |
| `dict()` constructor | `copiedTwo = dict(realInformation)` |

```python
realInformation = {
    "name": "Peter Alexander",
    "age": 55,
    "occupation": "Programmer",
    "Place of work": "Google",
    "Year of birth": 1970
}

copiedInformation = realInformation.copy()
copiedTwo         = dict(realInformation)
```

---

## 9. Nested Dictionaries

A dictionary can contain other dictionaries — this is called **nesting**.

```python
myFamily = {
    "FirstBorn": {
        "name": "Pauline",
        "year": 2001
    },
    "SecondBorn": {
        "name": "Gilbert",
        "year": 2004
    },
    "ThirdBorn": {
        "name": "Treasure",
        "year": 2020
    }
}
```

### Access a Nested Item

```python
print(myFamily["FirstBorn"]["name"])  # Pauline
```

### Loop Through a Nested Dictionary

```python
for c, obj in myFamily.items():
    print(c)
    for k in obj:
        print(k + ':', obj[k])

# Output:
# FirstBorn
# name: Pauline
# year: 2001
# SecondBorn
# ...
```

---

## Quick Reference

| Task | Method/Syntax |
|------|---------------|
| Access value | `dict[key]` or `.get(key)` |
| Get all keys | `.keys()` |
| Get all values | `.values()` |
| Get all pairs | `.items()` |
| Add / update item | `dict[key] = value` or `.update()` |
| Remove by key | `.pop(key)` or `del dict[key]` |
| Remove last item | `.popitem()` |
| Empty dictionary | `.clear()` |
| Copy dictionary | `.copy()` or `dict()` |
| Check key exists | `key in dict` |
