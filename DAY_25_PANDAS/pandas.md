# Python Pandas

## What is Pandas?

**Pandas** is a Python library used for working with data sets. It provides functions for **analyzing**, **cleaning**, **exploring**, and **manipulating** data.

- Allows you to analyze big data and draw conclusions based on statistical theories
- Can clean messy data sets and make them readable and relevant
- Widely used in data science, machine learning, and data analysis

### Installation

```bash
pip install pandas
```

```python
import pandas as pd
```

> **Important:** The convention `import pandas as pd` is the universally accepted alias. Always use `pd` to keep your code consistent and recognizable to other developers.

---

## Core Data Structures

| Structure | Description | Analogy |
|-----------|-------------|---------|
| **Series** | A one-dimensional labeled array | A single **column** in a table |
| **DataFrame** | A two-dimensional labeled data structure | The **whole table** |

> **Important:** A Series is like one column of a DataFrame. When you combine multiple Series together, you get a DataFrame.

---

## Part 1: Pandas Series

A **Series** is like a column in a table — a one-dimensional array with labels (called an **index**).

### 1.1 Series with Default Index

When no index is provided, Pandas assigns a default integer index starting from `0`.

```python
nums = [1, 2, 3, 4, 5]
series = pd.Series(nums)
print(series)
```

Output:
```
0    1
1    2
2    3
3    4
4    5
dtype: int64
```

> **Important:** The left column is the **index** and the right column is the **data**. By default the index starts at `0`, not `1`.

---

### 1.2 Series with Custom Index

You can assign meaningful labels as the index instead of default integers.

```python
my_nums = [1, 2, 3, 4, 5]
my_series = pd.Series(my_nums, index=[1, 2, 3, 4, 5])
print(my_series)

fruits = ['Orange', 'Banana', 'Mango']
fruits_series = pd.Series(fruits, index=[1, 2, 3])
print(fruits_series)
```

> **Important:** The `index` list must have the **same length** as the data list, otherwise Pandas will raise a `ValueError`.

---

### 1.3 Series from a Dictionary

When creating a Series from a dictionary, the **keys become the index** and the **values become the data**.

```python
my_name = {
    'name': 'Paulie Oraro',
    'country': 'Kenya',
    'city': 'Nairobi',
    'occupation': 'Software engineer',
    'age': 25
}

dict_series = pd.Series(my_name)
print(dict_series)
```

Output:
```
name                Paulie Oraro
country                    Kenya
city                     Nairobi
occupation      Software engineer
age                           25
dtype: object
```

> **Important:** Creating a Series from a dictionary is a very common pattern because it naturally maps labels (keys) to values — making the data self-describing and easy to read.

---

### 1.4 Constant Series

You can create a Series where all values are the same constant.

```python
constant_numbers = pd.Series(11, index=[1, 2, 3, 4, 5])
print(constant_numbers)
```

Output:
```
1    11
2    11
3    11
4    11
5    11
dtype: int64
```

> **Important:** A constant Series requires an explicit index — Pandas needs to know how many rows to create.

---

## Part 2: Pandas DataFrames

A **DataFrame** is a two-dimensional, tabular data structure with labeled rows and columns — like a spreadsheet or SQL table.

### 2.1 DataFrame from a List of Lists

Pass a list of lists and specify the column names using the `columns` parameter.

```python
my_data = [
    ['Pauline', 'Kenya', 'Nairobi'],
    ['Alexandra', 'Tanzania', 'Dodoma'],
    ['Johnny', 'Uganda', 'Kampala']
]
my_dataframe = pd.DataFrame(my_data, columns=['Names', 'Country', 'City'])
print(my_dataframe)
```

Output:
```
       Names   Country     City
0    Pauline     Kenya  Nairobi
1  Alexandra  Tanzania   Dodoma
2     Johnny    Uganda  Kampala
```

> **Important:** When using a list of lists, you **must** provide the `columns` parameter manually — Pandas has no way to infer column names from raw lists.

---

### 2.2 DataFrame from a Dictionary

Each **key** becomes a column name and each **value** (a list) becomes the column data. All lists must be the same length.

```python
students = {
    'Name': ['Paulie', 'Kate', 'Alexa', 'Joseph'],
    'Country': ['Kenya', 'Uganda', 'Tanzania', 'Rwanda'],
    'City': ['Nairobi', 'Kampala', 'Dodoma', 'Kigali']
}
students_table = pd.DataFrame(students)
print(students_table)
```

Output:
```
     Name   Country     City
0  Paulie     Kenya  Nairobi
1    Kate    Uganda  Kampala
2   Alexa  Tanzania   Dodoma
3  Joseph    Rwanda   Kigali
```

> **Important:** This is the most common way to create a DataFrame. It's clean, readable, and the column names come directly from the dictionary keys — no extra parameter needed.

---

### 2.3 DataFrame from a List of Dictionaries

Each **dictionary** in the list represents one **row**. The keys become column names.

```python
his_students = [
    {'Name': 'Asaph', 'Country': 'Finland', 'City': 'Helsinki'},
    {'Name': 'David', 'Country': 'UK',      'City': 'London'},
    {'Name': 'John',  'Country': 'Sweden',  'City': 'Stockholm'}
]
his_students_table = pd.DataFrame(his_students)
print(his_students_table)
```

Output:
```
    Name  Country       City
0  Asaph  Finland   Helsinki
1  David       UK     London
2   John   Sweden  Stockholm
```

---

### 2.4 Accessing Columns & Column Names

```python
# Get all column names
print(his_students_table.columns)
# Index(['Name', 'Country', 'City'], dtype='object')

# Access a single column (returns a Series)
country = his_students_table['Country']
print(country)
```

Output:
```
0    Finland
1         UK
2     Sweden
Name: Country, dtype: object
```

> **Important:** Accessing a single column from a DataFrame returns a **Series**, not a DataFrame. If you need it to remain a DataFrame, use double brackets: `his_students_table[['Country']]`.

---

## DataFrame Creation Methods — Comparison

| Method | Best Used When |
|--------|---------------|
| List of lists + `columns=` | You have raw data in rows and want to name columns manually |
| Dictionary of lists | You have data organized by column — most common approach |
| List of dictionaries | You have data organized by row, each with its own labels |

---

## Quick Reference

| Task | Code |
|------|------|
| Create a Series | `pd.Series([1, 2, 3])` |
| Series with custom index | `pd.Series(data, index=[...])` |
| Series from dictionary | `pd.Series(my_dict)` |
| Constant Series | `pd.Series(value, index=[...])` |
| DataFrame from list of lists | `pd.DataFrame(data, columns=[...])` |
| DataFrame from dictionary | `pd.DataFrame(my_dict)` |
| DataFrame from list of dicts | `pd.DataFrame([{...}, {...}])` |
| Get column names | `df.columns` |
| Access a column | `df['column_name']` |
