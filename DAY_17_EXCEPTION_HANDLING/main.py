# When an error occurs or exception as we call it, python will normally stop and generate an error message.

# This exceptions can be handled using the try statement.

# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The else block lets you execute code when there is no error.

# The finally block lets you execute code regardless of the result of the try and except blocks.

# since the try block raises an error the except block will be executed

try:
    print(x)
except:
    print("An exception occured")

# you can define as many exception blocks as you want.

try:
    print(x)
except NameError:
    print("variable x is not defined")
except:
    print("Something else went wrong")

# you can use the else keyword to define a block of code to be executed if no errors were raised

try:
    print("hello")
except:
    print("something went wrong")
else:
    print("nothing went wrong")

# the finally block if specified will be executed regardless if the try block raises an error or not.

try:
    print(x)
except:
    print("something went wrong")
finally:
    print("the 'try except' is finished")


# you  can choose to throw an exception if a condition occurs. To throw or raise an exception use the raise keyword. You can define what kind of error to raise and the text to print to the user.

x = 1
if x < 0:
    raise Exception("Sorry no numbers below zero")

y = "hello"
if not type(y) is int:
    raise TypeError("only integers are allowed")