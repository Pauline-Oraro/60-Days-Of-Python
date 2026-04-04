# strings in are surrounded by either single quotation marks or double quotation marks.
# 'hello' and "hello" are the same string.
# assigninig a string to a variable is done with the variable name followed by an equal sign and the string.

a = "string"
print(a)

# can assign a multiline string to a variable by using three quotes or three single quotes
b = """lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
print(b)

#strings in python are arrays of unicode characters. however, python does not have a character data type, a single character is simply a string with a length of 1. Square brackets can be used to access elements of the string.

c = "Hello world"
print(c[1])

#can loop through the characters in a string using for loop.

for y in "banana":
    print(y)

# to get the length of a string use the len() function
l = "python"
print(len(l))

# to check if a certain phrase or character is present in a string we can use the keyword in
text ="Python is a programming language"
print("a" in text)

# to check if a certain phrase or character is NOT present in a string we can use the keyword not in
textTwo  = "Javascript is a programming language"
print("python" not in textTwo)

# you can return a range of characters by using the slice syntax. specify the start index and the end index, separated by a colon, to return a part of the string.

#the first character has index 0, the second character has index 1, and so on. The end index is not included in the result.
slice = "this is a string data type"
print(slice[2:5]) 

# by leaving out the start index, the range will start at the first character
print(slice[:5])

# by leaving out the end index, the range will go to the end
print(slice[5:])

#python has a set of in-built methods that you can use on strings

myVariable  = "Coding is fun"
#uppercase
print(myVariable.upper())

#lowercase
print(myVariable.lower())

#remove whitespace
myVariableTwo = "   Hello world   "
print(myVariableTwo.strip())

#replace a string with another string
print(myVariable.replace("fun", "awesome"))

#split string
print(myVariable.split(" "))


# to concatenate or combine two strings you can use the + operator
stringOne = "Hello"
stringTwo = "Python"
stringThree = stringOne + " " + stringTwo
print(stringThree)


# we can combine strings and numbers by using f-strings or the format() method.
# to specify a string as an f-string simply put an f in front of the string and add curly brackets as placeholders for variables and other operations

age =20
txt = f"My name is Kate and I am {age} years old"
print(txt)


# Escape characters are used to insert characters that are illegal in a string. An escape character is a backslash \ followed by the character you want to insert.

txtTwo = "We are the so-called \"Wakanda\" from Africa"
print(txtTwo)