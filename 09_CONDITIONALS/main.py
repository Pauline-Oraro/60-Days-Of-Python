# python supports the usual logical conditions from mathematics. There are equals, not equals, less than, less than or equal to, greater than, greater than or equal to.

# this conditions can be used in several ways and most commonly in if statements and loops.

# if statement

# the if statement evaluates a condition which is an expression that results in True or False. If the condition is true, the code block inside the if statement is executed. If the condition is false the code block is skipped.

# python relies on indentation to define scope in the code. When the if statement does not have indentation it will raise an error

a = 100
b = 200
if b > a :
    print("b is greater than a ")

number = 15
if number > 0:
    print("The number is positive")

# you can have multiple statements inside an if block and all statements must be indented at the same level

age = 20
if age >= 18:
    print("You are an adult")
    print("You can vote")
    print("You have full legal rights")

# boolean variables can be used directly in if statements without comparison operators.
logged_in = True
if logged_in:
    print("Welcome back to your account")

# zero, empty strings, none and empty collections are treated as false and everything is treated as true.


# ELIF STATEMENT

# The elif keyword is python way of saying "if the previous conditions were not true, then try this condition"

# The elif keyword allows you to check multiple expressions for true and execute a block of code as soon as one of the conditions evaluates to true.

# when you use elif, python evaluates the conditions from top to bottom. As soon as it finds a condition that is true, it executes that block and skips all remaining conditions.

# Only the first true condition will be executed even if multiple conditions are true, python stops after executing the first matching block.

# Use elif when you have multiple mutually exclusive conditions to check.

c = 44
d = 44
if d > c:
    print("d is greater than c")
elif c == d:
    print("c and d are equal")

# you can have as many elif statements as you need. Python will check each condition in order and execute the first one that is  true.

score  = 85
if score >= 90:
    print ("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")

day = 4
if day == 1:
    print("monday")
elif day == 2:
    print("tuesday")
elif day == 3:
    print("wednesday")
elif day == 4:
    print("thursday")
elif day == 5:
    print("friday")
elif day == 6:
    print("saturday")
elif day == 7:
    print("sunday")


# PYTHON ELSE STATEMENT

# the else keyword catches anything which is not caught by the preceding conditions. The else statement is executed when if condition and any elif conditions evaluate to false. 

# The else statement acts as a fallback that executes when none of the preceding conditions are true.

# the else statement must come last.

e = 200
f = 100
if f > a:
    print("f is greater than a")
elif e == f:
    print("e and f are equal")
else:
    print("e is greater than f")

g = 300
h = 200
if h > g:
    print("h is greater than g")
else:
    print("h is not greater than g")

myNumber = 5
if myNumber % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

temperature = 22
if temperature > 30:
    print("it is hot outside")
elif temperature > 20:
    print("it is warm outside")
elif temperature > 10:
    print("it is cool outside")
else:
    print("it is cold outside")


# SHORTHAND IF

# if you have only one statement to execute yyou can put it on the same line as the if statement.

i = 5
j = 2
if i > j : print("i is greater than j")

# if you have one statement for if and one for else you can put them on the same line using a conditional expression.

k = 2
l = 350
print("k") if k > l else print("l")

# you can also use a one-line if/else to choose a value and assign it to a variable.

m = 10
n = 20
bigger = m if m > n else n
print("Bigger is", bigger)


# LOGICAL OPERATORS

# Logical operators are used to combine conditional statements. 
# and returns true if both statements are true

o = 200
p = 33
q = 500
if o > p and q > o:
    print("Both conditions are true")

# or returns true if one of the statements is true

o = 200
p = 33
q = 500
if o > p or o > c:
    print("Atleast one of the conditions is true")

# not reverses the result, returns false if the result is true
p = 33
q = 500
if not p > q:
    print("p is not greater than q")

# you can combine multiple logical operators in a single expression. Python evaluates not first then and then or.
myAge = 25
is_student = False
has_discount_code = True
if (myAge < 18 or myAge > 65) and not is_student or has_discount_code:
    print("Discount applies")


# NESTED IF STATEMENTS

# you can have if statements inside if statements
x = 41
if x > 10:
    print("above ten")
    if x > 20:
        print("and also above 20")
    else:
        print("but not above 20")

studentAge = 16
has_license = True
if studentAge >= 18:
    if has_license:
        print("you can drive")
    else:
        print("You need a license")
else:
    print("you are too young to drive")


# PASS STATEMENT

# if statements cannot be empty but if you for some reason have an if statement with no content put in the pass statement to avoid getting an error.

# the pass statement is a null operation nothing happens when it executes

# the pass statement is useful when you are creating code structure but you haven't implemented the logic yet. Used as a placeholder for future code during development. Used in empty functions or classes that you plan to implement later.

z = 44
y = 200
if y > z:
    pass


# PYTHON MATCH

# the match statement is used to perform different actions based on different conditions.

# instead of writing many if else statements you can use the match statement.

# the match expression is evaluated once. the value of the expression is compared with the values of each case. if there is a match the associated block of code is executed.

# use the underscore character as the last case value if you want a code block to execute when there are not other matches.

day = 5
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")