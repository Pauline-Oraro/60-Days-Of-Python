# Python has two primitive loop commands which are while loops and for loops.

#WHILE LOOP
# We can execute a set of statements as long as a condition is true.
# The while loop requires relevant variables to be ready, the the example below we need to define an indexing variable i which is set to 1.

i = 1
while i < 6:
    print(i)
    i += 1

# With the break statement we can stop the loop even if the while condition is true

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# With the continue statement we can stop the current iteration and continue with the next

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# With the else statement we can run a block of code once when the condition is no longer true

i = 1 
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")


# FOR LOOPS

# A for loop is used for iterating over a sequence that is either a list, tuple, dictionary, set or a string.

fruits = ["apple", "banana", "kiwi"]
for x in fruits:
    print(x)

# strings are iterable objects and they contain a sequence of characters
for x in "watermelon":
    print(x)

# with the break statement we can stop the loop before it has looped through all the items
vegetables = ["broccoli", "kales", "spinach"]
for y in vegetables:
    print(y)
    if y == "kales":
        break

# breaks before the print
for z in vegetables:
    if z == "kales":
        break
    print(z)

# with the continue statement we can stop the current iteration of the loop and continue with the next
for x in vegetables:
    if x == "kales":
        continue
    print(x)

# to loop through a set of code a specified number of times we can use the range() function. The range() function returns a sequence of numbers starting from 0 by default and increments by 1 and ends at a specified number

for a in range(7):
    print(a)

# it is possible to specify the starting value by adding a parameter
for b in range(3,6):
    print(b)

# it is possible to specify the increment value by adding a third parameter.
for c in range(2, 30, 4):
    print(c)

# the else keyword in a for loop specifies a block of code to be executed when the loop is finished
for d in range(7):
    print(d)
else:
    print("Finally finished!")

# a nested loop is a loop inside a loop. The inner loop will be executed one time for each iteration of the outer loop.
color = ["red", "yellow", "blue"]
fruits = ["apple", "banana", "blueberries"]

for e in color:
    for f in fruits:
        print(e, f)

# for loops cannot be empty but if you for some reason have a for loop with no content put in the pass statement to avoid getting an error.
for x in [0, 1, 2, 3]:
    pass