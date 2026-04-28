# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable and allow duplicate values. 
# Tuples are written with round brackets.
# Tuple items are indexed, the first item has index[0], the second item has index [1]......
# Tuples are ordered meaning that the items have a defined order and that order will not change.
# Tuples are unchangeable meaning that we cannot change, add or remove items after the tuple has been created.
# Tuples can have items with the same value.

myTuple = ("kate","john","michael")
print(myTuple)

thisTuple = ("kate", "george", "maria", "kate", "michael", "maria")
print(thisTuple)

# to determine how many items a tuple has use the len() function
print(len(thisTuple))

# to create a tuple with only one item you have to add a comma after the item otherwise python wwill not recognize it a tuple.
myList = ("wonder",)
print(type(myList))

# tuples items can be of any data type
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)

# can use the tuple() constructor to make a tuple.
myGroceryList = tuple(("milk", "bread", "eggs"))
print(myGroceryList)


# ACCESSING TUPLE ITEMS

# you can access tuple items by referring to the index number inside square brackets
myFruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(myFruits[1])

# negative indexing means start from end of the tuple. -1 refers to the last item, -2 refers to the second last item....
print(myFruits[-1])

# you can specify a range of indexes by specifying where to start and where to end the range. when specifying a range the return value will be a new tuple with the specified items.
print(myFruits[2:5])

# can specify negative indexes if you want to start the search from the end of the tuple
print(myFruits[-4:-1])

# to determine if a specified item is present ina tuple use the in keyword
if "apple" in myFruits:
    print("Yes, 'apple' is in the fruits tuple")


# UPDATING TUPLES

# Tuples are unchangeable, meaning that you cannot change, add or remove items once the tuple is created. but you can convert the tuple into a list, change the list and covert the list back into a tuple.
cars = ("ford", "toyota", "honda")
print(cars)
carsList = list(cars)
carsList[0] = "nissan"
cars = tuple(carsList)
print(cars)

# to add items to a tuple you can convert it into a list, add the item to the list and convert it back into a tuple.
names = ("kate", "pauline", "john")
print(names)
namesList = list(names)
namesList.append("mary")
names = tuple(namesList)
print(names)

# you can add tuples to tuples by creating a new tuple with the items and add it to the existing tuple
tupleA = ("a", "b", "c")
tupleB = (1, 2, 3)
tupleC = tupleA + tupleB
print(tupleC)

# you can remove items in a tuple by converting it into a list, removing the item from the list and converting it back into a tuple.
letters = ("a", "b", "c", "d", "e")
print(letters)
lettersList = list(letters)
lettersList.remove("c")
letters = tuple(lettersList)
print(letters)


# UNPACKING TUPLES
# when we create a tuple we assign values to it and this is called packing a tuple. when we want to extract the values back into variables this is called unpacking a tuple.
places = ("nairobi", "mombasa", "kisumu")
(city1, city2, city3) = places
print(city1)
print(city2)
print(city3)

# if the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list
capitalCity = ("Nairobi", "Dodoma", "Addis Ababa", "Kampala", "Mogadishu")
(capital1, capital2, *capital3) = capitalCity
print(capital1)
print(capital2)
print(capital3)

#LOOP TUPLES

# you can loop through the tuple items by using a for loop
vegetables = ("Broccoli", "celery", "kale", "peas", "butternut")

for x in vegetables:
    print(x)

# you can also loop through the tuple items by referring to their index number. Use the range() and len () function.
for i in range(len(vegetables)):
    print(vegetables[i])

# you can loop through the tuple items by using a while loop. Use the len() function to determine the length of the tuple then start at 0 and loop your way through the tuple items by referring to their indexes.
i = 0
while i < len(vegetables):
    print(vegetables[i])
    i = i + 1


# JOIN TUPLES

# you can join two or more tuples using the + operator
students = ("liam", "zawadi", "jack", "mary")
lecturers = ("john", "peter", "lucy")

university = students + lecturers
print(university)

# if you want to multiply the content of a tuple a given number of times you can use the * operator.
studentsNames = students * 2
print(studentsNames)