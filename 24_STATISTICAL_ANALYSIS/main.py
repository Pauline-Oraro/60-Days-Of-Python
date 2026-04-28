# Statistics is the discipline that studies the  collection, organization, displaying, analysing, interpreting and presentation of data. It is a branch of mathematics that is recommended to be a prerequisite for data science and machine learning.Having some knowlegde in statistics will help you make decisions on data.

# data is any set of characters that is gathered and translated for some purpose, usually analysis. It can be any character, including text and numbers, pictures, sound, or video. 

# The Python statistics module provides functions for calculating mathematical statistics of numerical data. 

# NumPy is a python library used for working with arrays.

#  It stands for Numerical Python.

# The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy. Arrays are very frequently used in data science, where speed and resources are very important.

# install numpy : pip install numpy

import numpy as np

# creating int numpy arrays

my_list = [1,2,3,4,5]
print(type(my_list))

# creating a multidimensional array using numpy
two_dim_list = [[1,2,3], [4,5,6]]
print(two_dim_list)

my_array = np.array(my_list)
print(my_array)
print(type(my_array))

# creating float numpy arrays
my_float_list = np.array(my_list, dtype=float)
print(my_float_list)

# creating boolean numpy arrays
this_list = [0,1,0,1,0]
my_bool_list = np.array(this_list, dtype=bool)
print(my_bool_list)

# converting numpy array to a list
numpy_array = np.array([1,2,3,4,5])
converted_list = numpy_array.tolist()
print(converted_list)
print(type(converted_list))

# creating numpy array from a tuple
my_tuple = (1,2,3,4,5)
my_array_from_tuple = np.array(my_tuple)
print(my_array_from_tuple)

# to know the number of items in a numpy array list we use size
print(my_array_from_tuple.size)

#mathematical operations on numpy arrays
array1 = np.array([1,2,3])
addition = array1 + 10
print(addition)

subraction = array1 - 10
print(subraction)

multiplication = array1 * 10
print(multiplication)

division = array1 / 10
print(division)

modulus = array1 % 2
print(modulus)

floor_division = array1 // 2
print(floor_division)

exponentiation = array1 ** 2
print(exponentiation)

# getting items from a numpy array
# 2 Dimension Array
two_dimension_array = np.array([[1,2,3],[4,5,6]])
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
print('First row:', first_row)
print('Second row:', second_row)

first_column= two_dimension_array[:,0]
second_column = two_dimension_array[:,1]

print('First column:', first_column)
print('Second column:', second_column)

# generating random numbers
    
normal_array = np.random.normal(79, 15, 80)
print(normal_array)

# NumPy has quite useful statistical functions for finding minimum, maximum, mean, median, percentile, standard deviation and variance, etc from the given elements in the array.
print('Minimum:', np.min(normal_array))
print('Maximum:', np.max(normal_array))
print('Mean:', np.mean(normal_array))
print('Median:', np.median(normal_array))
print('25th Percentile:', np.percentile(normal_array, 25))
print('50th Percentile:', np.percentile(normal_array, 50)) 
print('Standard Deviation:', np.std(normal_array))
print('Variance:', np.var(normal_array))
