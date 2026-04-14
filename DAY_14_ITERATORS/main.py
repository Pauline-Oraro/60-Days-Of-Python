# An iterator is an object that contains a countable number of values. 

# An iterator is an object that can be iterated upon meaning that you can traverse through all the values.

# In python an iterator is an object which implements the iterator protocol which consists of the methods __iter__() and __next__().

# lists, tuples, dictionaries, strings and sets are all iterable objects. They are iterable containers which you can get an iterator from.

mytuple = ("kate", "mercedes", "hailey")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

mystring = "pauline"
myit = iter(mystring)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# We can use for loop to iterate through an iterable object. It creates an iterator object and executes the next() method for each loop.
my_grocery_list = ["milk", "eggs", "bread", "butter", "cheese"]

for x in my_grocery_list:
    print(x)

my_name = "Oraro"
for y in my_name:
    print(y)