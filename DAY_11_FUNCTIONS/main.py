# A function is a block of code which only runs when it is called.

# A function can return data as a result.

# Functions help avoid code repetition. With functions you can write the code once and reuse it.

# In python a function is defined using the def keyword followed by a function name and parenthesess.

# A function name must start with a letter or underscore.

# A function name can only contain letters, numbers and underscore.

# Function names are case-sensitive(myFunction and myfunction are different).

# It is a good practice to use descriptive names that explain what the function does.

def my_function():
    print("This is a function")

# to call a function write its name followed by parentheses

my_function()

# you can call the same function mulitple times

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
print(fahrenheit_to_celsius(88))
print(fahrenheit_to_celsius(50))
print(fahrenheit_to_celsius(90))
print(fahrenheit_to_celsius(60))

# Functions can send data back to the code that called them using the return statement. When a function reaches a return statement it stops executing and sends the result back. If a function does not have a return statement it returns none by default.

def greeting():
    return "Hello from this function"

message = greeting()
print(message)

# can use the return value directly
print(greeting())

# functions definations cannot be empty if you need to create a function placeholder without any code use the pass statement.

def this_function():
    pass


# FUNCTION ARGUMENTS

# information can be passed into functions as arguments

# arguments are specified after the function name inside the parameters. You can add as many arguments as you want just separate them with a comma.

# A parameter is the variable listed inside the parentheses in the function defination while an argument is the actual value that is sent to the function when it is called.

# By default a function must be called with the correct number of arguments. If you try to call the function with the wrong number of arguments you will get an error

def my_name(name): # name ia a parameter
    print(name + " : This is my name")

my_name("Pauline Akinyi Oraro") # "Pauline Akinyi Oraro" is an argument

# you can assign default values to parameters if the function is called without an argument it uses the default value

def student_name(name = 'john'):
    print("Hello", name)

student_name()
student_name("oraro")
student_name("kate")

# you can send arguments with the key=value syntax. The order does not matter. This are called keyword arguments.

def my_pet(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is ", name)
my_pet(animal="cat", name="Kiri")

# When you call a function with arguments without using keywords they are called positional arguments. They must be in the correct order. switching the order changes the result.

def my_cat(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is ", name)
my_cat("cat", "maxy")

# you can mix positional and keyword arguments in a function call. positional arguments must come before keyword arguments

def my_information(name, age, course):
    print("My name is", name, " and i am", age, " years old.", "I do", course, " in the university")

my_information("Pauline Oraro", age = 20, course="Bachelor of science in information technology" )

# you can specify that a function can have only positional arguments. add, / after the arguments. Without the, / you are actually allowed to use keyword arguments even if the function expects positional arguments. With , / you will get an error if you try to use keyword arguments.

def student(name, /):
    print("Hello", name)
student("mary")

# to specify that a function can have only keyword arguments add *, before the arguments. Without *, you are allowed to use positional arguments even if the function expects keyword arguments.

def my_students(*, name):
    print("Hello", name)

my_students(name= "jack")

# you can combine both argument types in the same function. Arguments before / are positional only and argument after * are keyword only.

def my_numbers(a, b, /, *, c, d):
    return a + b + c + d
result = my_numbers(11, 22, c = 33, d = 44)
print(result)

# you can send any data type as an argument to a function.

def my_fruits(fruits):
    for fruit in fruits:
        print(fruit)

my_fruit = ["cherries", "bananas", "apples"]
my_fruits(my_fruit)


# *ARGS AND **KWARGS

# by default a function must be called with the correct number of arguments. Sometimes you may not know how many arguments that wiil be passed into your function. *args and **kwargs allow functions to accept a unknown number of arguments.

# if you do not know the number of arguments that will be passed into your function add * before the parameter.

# The *args parameter allows a function to accept any number of positional arguments.

def my_children(*kids):
    print("The youngest child is " + kids[2])

my_children("jack", "azriel", "dylan")

# If you do not know how many keyword arguments will be passed into your function add ** before the parameter name.

# The **kwargs parameter allows a function to accept any number of keyword arguments

def his_children(**kid):
    print("His last child is called " + kid["lname"])

his_children(fname= "Pauline", sname = "oraro", lname= "akinyi")


# PYTHON SCOPE

# a variable is only available from the inside the region it is created. This is called a scope.

# a variable created inside a function is available inside that function. This variable is not available outside the function but it is available for any function inside a function.

def myfunc():
    x = 777
    print(x)

myfunc()

def mynumber():
    y = 44
    def myinnerfunc():
        print(y)
    myinnerfunc()

mynumber()

# a variable created in the main body of the python code is a global variable and it belongs to the global scope.

a = 99

def myfunctions():
    print(a)

myfunctions()
print(a)