# When we write our code it is common that we make mistakes. if our code fails to run the python interpreter will raise an error. 

# Understanding the different types of errors and how to handle them is an important part of becoming a proficient python programmer.

# There are many different types of errors that can occur in python. In this lesson we will learn about the different types of errors and how to handle them.


# SYNTAX ERRORS
# A syntax error occurs when the python interpreter encounters code that does not follow the rules of the python language. This can be caused by a missing parenthesis, a missing colon, or a misspelled keyword.

# This will raise a syntax error because the closing parenthesis is missing.
print("pauline" 
      

# NAME ERRORS
# A name error occurs when the python interpreter encounters a variable or function name that is not defined. This can be caused by a typo or by trying to use a variable that has not been assigned a value.

print(age)


# INDEX ERRORS
# An index error occurs when the python interpreter encounters an index that is out of range. This can be caused by trying to access an element in a list that does not exist.

fruits = ["apple", "banana", "cherry"]
print(fruits[3])  


# MODULE NOT FOUND ERRORS
# A module not found error occurs when the python interpreter cannot find a module that is being imported. This can be caused by a typo in the module name or by trying to import a module that is not installed.

import maths
print(maths.pi)


# ATTRIBUTE ERRORS
# An attribute error occurs when the python interpreter encounters an attribute that does not exist. This can be caused by a typo in the attribute name or by trying to access an attribute that does not exist.

class Person:
    def __init__(self, name):
        self.name = name

person = Person("Alice")
print(person.name)  # This will print "Alice"

# This will raise an attribute error because the attribute "age" does not exist.
print(person.age)


# KEY ERROR
# A key error occurs when the python interpreter encounters a key that does not exist in a dictionary. This can be caused by a typo in the key name or by trying to access a key that does not exist.

my_dict = {"name": "Alice", "age": 30}
print(my_dict["name"])  # This will print "Alice"

# This will raise a key error because the key "gender" does not exist in the dictionary.
print(my_dict["gender"])


# TYPE ERROR
# A type error occurs when the python interpreter encounters an operation that is not supported for a particular data type. This can be caused by trying to perform an operation on incompatible data types.

print(4 + "5")  # This will raise a type error because you cannot add an integer and a string together.


#IMPORT ERROR
# An import error occurs when the python interpreter cannot find a module that is being imported. This can be caused by a typo in the module name or by trying to import a module that is not installed.

import mathh
print(mathh.pi)

#VALUE ERROR
# A value error occurs when the python interpreter encounters a value that is not valid for a particular operation. This can be caused by trying to convert a string to an integer that does not contain a valid number.

print(int("hello"))  # This will raise a value error because "hello" is not a valid integer.


#ZERO DIVISION ERROR
# A zero division error occurs when the python interpreter encounters a division operation where the denominator is zero. This can be caused by trying to divide a number by zero.

print(5 / 0)  # This will raise a zero division error.