# operators are used to perform operations on variables and values

#arithmetic operators are used with numeric values to perform common mathematical operations

valueOne = 400
valueTwo = 200
#addition
print(valueOne + valueTwo)

#subtraction
print(valueOne - valueTwo)

# multiplication
print(valueOne * valueTwo)

# division which always returns a float value
print(valueOne / valueTwo)

# modulus
print(valueOne % valueTwo)

# exponentiation
print(valueOne ** valueTwo)

# floor division which return an integer value
print(valueOne // valueTwo)


# assignment operators are used to assign values to variables

# = 
a = 5
print(a)

# += is the same as b = b + 3
b = 7
b += 3
print(b)

#-= is the same as c = c-2
c = 10
c -=2
print(c)

# *= is the same as d = d * 4
d = 3
d *= 4
print(d)

# /= is the same as e = e /2
e = 20
e /= 2
print(e)

# %= is the same as f = f % 3
f = 10
f %= 3
print(f)

# // = is the same as g = g // 2
g = 10
g //= 2
print(g)

# **= is the same as h = h ** 2
h = 5
h **= 2
print(h)

# comparison operators are used to compare two values. They return a boolean value of either True or False
i = 5
j = 10
print(i == j)  # equal
print(i != j)  # not equal
print(i > j)   # greater than
print(i < j)   # less than
print(i >= j)  # greater than or equal to
print(i <= j)  # less than or equal to

# python allow you to chain comparison operators
k = 80
print(1 < k < 100)
print(1 < k and k < 100)

# logical operators are used to combine conditional statements

#and returns true if both statements are true
l = 5
print (l < 10 and l < 20)

# or returns true if one of the statements is true
m = 15
print( m < 10 or m < 20)

# not reverses the result and returns false if the result is true
n = 25
print(not(n < 20))
print(not(n > 20))

# identity operators are used to compare the objects, not if they are equal but if they are actually the same object with the same memory location.

# is returns true if both variables are the same object
o = ["apples", "pineapples"]
p = ["apples", "pineapples"]
q = o
print(o is q)
print(o is p)

# is not returns true if both variables are not of the same object
print(o is not p)


# membership operators are used to test if a sequence is presented in an object

# in returns true if a sequence with the specified value is present in the object
r = ["apples", "pineapples"]
print("apples" in r)
print("bananas" in r)

# not in returns true if a sequence with the specified value is not present in the object
print("bananas" not in r)


# bitwise operators are used to compare (binary) numbers

# & sets each bit to 1 if both are 1
print( 6 & 3)

# | sets each bit to 1 if one of the two bits is 1
print(6 | 3)

# ^ sets each bit to 1 if only one of two bits is 1
print(6 ^ 3)