# A module is a file containing a set of functions you want to include in your application.

# to create a module just save the code you want in another file with the file extension .py

# we can now use the module we just created by using the import statement.

import module

module.greeting("Pauline")

# the module can contain functions but also variables of all types.

a = module.person1["age"]
print(a)

# you can create an alias when you import a module by using the as keyword.

import module as md

name = md.person1["name"]
print(name)

# there are several built-in modules in python which you can import whenever you like.

import platform

x = platform.system()
print(x)

# there is a built in function to list all the function names or variable names in a module. this is a dir() function.

import platform

y = dir(platform)
print(y)

# you can choose to import only parts from a module by using the from keyword.

from module import person1

print(person1["country"])