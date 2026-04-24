# Python NumPy & Statistics

## What is Statistics?

**Statistics** is the discipline that studies the collection, organization, displaying, analysing, interpreting, and presentation of data. It is a branch of mathematics that is recommended as a prerequisite for **data science** and **machine learning**. Having knowledge in statistics helps you make better decisions based on data.

## What is Data?

**Data** is any set of characters gathered and translated for some purpose — usually analysis. It can be text, numbers, pictures, sound, or video.

---

## What is NumPy?

**NumPy** (Numerical Python) is a Python library used for working with arrays. The array object in NumPy is called `ndarray`.

### Why NumPy?

- Provides a powerful N-dimensional array object
- Much faster than Python lists for numerical operations
- Supports mathematical, statistical, and logical operations
- Widely used in data science and machine learning
- Works seamlessly with other libraries like Pandas and Matplotlib

### Installation

```bash
pip install numpy
```

```python
import numpy as np
```

> **Important:** The convention `import numpy as np` is the universally accepted alias. Always use `np` to keep your code consistent and readable to others.

---

## 1. Creating NumPy Arrays

### From a List (Integer Array)

```python
my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
print(my_array)        # [1 2 3 4 5]
print(type(my_array))  # <class 'numpy.ndarray'>
```

> **Important:** Unlike Python lists, NumPy arrays are printed **without commas** between elements.

### Float Array

```python
my_float_list = np.array(my_list, dtype=float)
print(my_float_list)  # [1. 2. 3. 4. 5.]
```

### Boolean Array

```python
this_list = [0, 1, 0, 1, 0]
my_bool_list = np.array(this_list, dtype=bool)
print(my_bool_list)  # [False  True False  True False]
```

> **Important:** When converting to boolean, `0` becomes `False` and any non-zero value becomes `True`.

### From a Tuple

```python
my_tuple = (1, 2, 3, 4, 5)
my_array_from_tuple = np.array(my_tuple)
print(my_array_from_tuple)  # [1 2 3 4 5]
```

### Multidimensional Array (2D)

```python
two_dim_list = [[1, 2, 3], [4, 5, 6]]
two_dimension_array = np.array(two_dim_list)
print(two_dimension_array)
# [[1 2 3]
#  [4 5 6]]
```

---

## 2. Converting Arrays

### NumPy Array → Python List

```python
numpy_array = np.array([1, 2, 3, 4, 5])
converted_list = numpy_array.tolist()
print(converted_list)       # [1, 2, 3, 4, 5]
print(type(converted_list)) # <class 'list'>
```

### Getting the Size of an Array

```python
print(my_array_from_tuple.size)  # 5
```

> **Important:** `.size` returns the **total number of elements** in the array. For multidimensional arrays, it counts all elements across all dimensions.

---

## 3. Array Data Types (`dtype`)

| dtype | Description | Example Input | Output |
|-------|-------------|---------------|--------|
| `int` | Integer (default for whole numbers) | `[1, 2, 3]` | `[1 2 3]` |
| `float` | Floating point | `[1, 2, 3]` | `[1. 2. 3.]` |
| `bool` | Boolean | `[0, 1, 0]` | `[False True False]` |
| `str` | String | `['a', 'b']` | `['a' 'b']` |

---

## 4. Mathematical Operations on Arrays

NumPy applies operations to **every element** in the array at once — this is called **vectorization** and is much faster than using a Python loop.

```python
array1 = np.array([1, 2, 3])

print(array1 + 10)   # [11 12 13]  — addition
print(array1 - 10)   # [-9 -8 -7]  — subtraction
print(array1 * 10)   # [10 20 30]  — multiplication
print(array1 / 10)   # [0.1 0.2 0.3] — division
print(array1 % 2)    # [1 0 1]     — modulus
print(array1 // 2)   # [0 1 1]     — floor division
print(array1 ** 2)   # [1 4 9]     — exponentiation
```

> **Important:** Operations apply to every element simultaneously without needing a loop — this is one of NumPy's biggest advantages over plain Python lists.

---

## 5. Accessing Items from a 2D Array

```python
two_dimension_array = np.array([[1, 2, 3], [4, 5, 6]])
```

### Accessing Rows

```python
first_row  = two_dimension_array[0]
second_row = two_dimension_array[1]
print('First row:', first_row)   # First row: [1 2 3]
print('Second row:', second_row) # Second row: [4 5 6]
```

### Accessing Columns

Use `[:, column_index]` — the `:` means "all rows".

```python
first_column  = two_dimension_array[:, 0]
second_column = two_dimension_array[:, 1]
print('First column:', first_column)   # First column: [1 4]
print('Second column:', second_column) # Second column: [2 5]
```

> **Important:** The `:` in `[:, 0]` selects **all rows** while `0` selects the first column. This is called **slicing** and is unique to NumPy — Python lists cannot do this directly.

---

## 6. Generating Random Numbers

`np.random.normal()` generates an array of random numbers following a **normal (bell curve) distribution**.

```python
# np.random.normal(mean, standard_deviation, number_of_values)
normal_array = np.random.normal(79, 15, 80)
print(normal_array)
```

> **Important:** A **normal distribution** means values cluster around the mean (79) with most falling within one standard deviation (15) on either side. This is heavily used in statistics and machine learning.

---

## 7. Statistical Functions

NumPy provides built-in functions for the most common statistical calculations.

```python
print('Minimum:', np.min(normal_array))
print('Maximum:', np.max(normal_array))
print('Mean:', np.mean(normal_array))
print('Median:', np.median(normal_array))
print('25th Percentile:', np.percentile(normal_array, 25))
print('50th Percentile:', np.percentile(normal_array, 50))
print('Standard Deviation:', np.std(normal_array))
print('Variance:', np.var(normal_array))
```

### Statistical Functions Reference

| Function | Description |
|----------|-------------|
| `np.min(arr)` | Smallest value in the array |
| `np.max(arr)` | Largest value in the array |
| `np.mean(arr)` | Average of all values |
| `np.median(arr)` | Middle value when sorted |
| `np.percentile(arr, n)` | Value below which n% of data falls |
| `np.std(arr)` | How spread out values are from the mean |
| `np.var(arr)` | Square of the standard deviation |

### Understanding the Key Statistics

| Term | What it tells you |
|------|-------------------|
| **Mean** | The average — the central value of the data |
| **Median** | Less affected by outliers than the mean |
| **Standard Deviation** | Low = data is clustered; High = data is spread out |
| **Variance** | Same concept as std deviation but squared |
| **Percentile** | Useful for understanding data distribution (e.g. 25th percentile = bottom quarter of data) |

> **Important:** The **50th percentile** is always equal to the **median**. These are two ways of expressing the same thing.

---

## Quick Reference

| Task | Code |
|------|------|
| Create array from list | `np.array([1, 2, 3])` |
| Create float array | `np.array([1, 2, 3], dtype=float)` |
| Create boolean array | `np.array([0, 1, 0], dtype=bool)` |
| Convert to Python list | `array.tolist()` |
| Get number of elements | `array.size` |
| Generate random normal data | `np.random.normal(mean, std, n)` |
| Get a row from 2D array | `array[row_index]` |
| Get a column from 2D array | `array[:, col_index]` |
| Basic math operations | `array + n`, `array * n`, etc. |
| Min / Max | `np.min(arr)` / `np.max(arr)` |
| Mean / Median | `np.mean(arr)` / `np.median(arr)` |
| Standard Deviation / Variance | `np.std(arr)` / `np.var(arr)` |
