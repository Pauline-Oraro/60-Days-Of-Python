# Variables are containers for storing data values.
# A variable is created the moment you first assign a value to it.
# Variable names are case sensitive.
# Variable names must start with a letter or underscore.
# A variable name cannot start with a number.
# Variable names can only contain alpha-numeric characters and underscores(A-Z, 0-9 and _).
# A variable name cannot be any of the python keywords.
# Variables with more than one word can be written in camel case, pascal case and snake case.

x = 6
y = "Pauline"
z = 999
myVar = "this is a variable but it is in camel case"
my_var = "this is also a variable but with an underscore"
_my_var = "This is another variable but it starts with an underscore"
MYVAR = "This is also a variable but in uppercase"
myvar4 = "This is a variable with a number in it"

# camel case
myFirstName = "Pauline"
# pascal case
MyFirstName = "Pauline"
# snake case
my_first_name = "Pauline"

print(x)
print(y)
print(z)
print(myVar)
print(my_var)
print(_my_var)
print(MYVAR)
print(myvar4)


# Can get the data type of a variable with the type() function.
print(type(x))
print(type(y))
print(type(z))

# Python allows you to assign values to multiple variables in one line. Make sure the number of variables matches the number of values.
a, b, c = "Orange", "Banana", "Mangoes"
print(a)
print(b)
print(c)

# Can assign the same value to muliple variables in one line.
d = e = f = "Berries"
print(d)
print(e)
print(f)

# in the print() function you can output multiple variables separated by a comma or + sign.
firstName = "Pauline "
MiddleName = "Akinyi "
surName = "Oraro"
print(firstName + MiddleName + surName)
print(firstName, MiddleName, surName)

#Global variables are variables that are created outside a function and can be used by eeveryone, both inside and outside of functions.

myVariable = "awesome"

def myFunc():
    print("I am " + myVariable) ;

myFunc()

# Local variables are variables that are created inside a function and can only be used inside that function.

def myLocalFunc():
    localVariable = "genius"
    print("I am a " + localVariable)

myLocalFunc()

# to create a global variable inside a function, you can use the global keyword. if you use the global keyword, the variable belongs to the global scope and can be used outside the function.

def myGlobalFunction():
    global globalVariable
    globalVariable ="python"

myGlobalFunction()
print(globalVariable)

# can use the global keyword to change the value of a global variable inside a function.

letterX = "programming"

def changeLetterX():
    global letterX
    letterX = "coding"

changeLetterX()

print(letterX)