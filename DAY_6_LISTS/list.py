# Lists are used to store multiple items in a single variable.

# they are created using square brackets and list items are ordered, changeable and allow duplicate values.
ThisList = ["pauline", "kate", "maggie"]
print(ThisList)

# list items are indexed, the first item has index [0], the second item has index [1].......

# lists are ordered meaning that the items have a defined order and that order will not change. If you add new items to a list, the new items will be placed at the end of the list.

# list are changeable meaning that we can change, add and remove items in a list after it has been created.

# since lists are indexed they can have items with the same value.
thisList = ["apple", "banana", "cherry", "apple", "cherry"]
print(thisList)

# to determine how many items a list has use the len() function
print(len(thisList))

# list items can be of any data type
list1 = ["mangoes", "pineapples", "oranges"]
list2 = [111, 222, 333, 444]
list3 = [True, False, True, False]
print(list1)
print(list2)
print(list3)

# a list can contain different data types
list4 = ["pauline", 20, True, "Nairobian", 44.5]
print(list4)

# lists are defined as objects with the data type list
myList = ["Nairobi", "Mombasa", "Kisumu"]
print(type(myList))

# can use the list() constructor when creating a new list
newList = list((99, 88, 77, 66))
print(newList)


# List items are indexed and you can access them by referring to the index number

students_Names = ["hillary", "mary", "jane", "max", "john"]
print(students_Names[0])  # Access the first item
print(students_Names[2])  # Access the third item

# negative indexing means start from the end, -1 refers to the last item, -2 refers to the second last items......

print(students_Names[-1])  # Access the last item
print(students_Names[-3])  # Access the third last item

# You can specify a range of indexes by specifying where to start and where to end the range. When specifying a range, the return value will be a new list with the specified items.

print(students_Names[1:4])  # Access items from index 1 to index 3 (4 is not included)
print(students_Names[:3])  # Access items from the beginning to index 2
print(students_Names[2:])  # Access items from index 2 to the end

# specify negative indexes if you want to start the search from the end of the list

print(students_Names[-4:-1])  # Access items from index -4 to -1

# to determine if a specified item is present in a list use the in keyword
if "max" in students_Names:
    print("Yes, max is in the list")


# to change the value of a specific item refer to the index number

fruits = ["apples", "bananas", "oranges", "strawberries", "berries"]
print(fruits)
fruits[2] = 'grapes'
print(fruits)

# to change the value of items within a specific range, define a list with the new values and refer to the range of index numbers where you want to insert the new values
fruits[1:3] = ["kiwi", "mangoes"]
print(fruits)


# ADDING LIST ITEMS

# to insert a new list items without replacing any of the existing values we can use the insert() method. The insert() method inserts an item at the specified index.
fruits.insert(2, "watermelon")
print(fruits)

# to add an item to the end of the list use the append() method
fruits.append("pineapples")
print(fruits)

# to append elements from another list to the current list use the extend() method
tropicalFruits = ["papaya", "guava", "passion fruit"]
fruits.extend(tropicalFruits)
print(fruits)


# REMOVING LIST ITEMS

# the remove() method removes the specified item from the list
fruits.remove("kiwi")
print(fruits)

# the pop() method removes the specified index and if you do not specify the index the pop() method removes the last item.
fruits.pop(2)
print(fruits)
fruits.pop()
print(fruits)

# the del keyword also removes the specified index
del fruits[0]
print(fruits)

# the del keyword can also delete the list completely

# the clear() method empties the list but keeps the list itself.
fruits.clear()
print(fruits)


# LOOP LISTS

# you can loop through the list items by using a for loop.

vegetables = ["cabbage", "spinach", "kale", "carrots", "broccoli"]
for x in vegetables:
    print(x)

# you can also loop through the list items by referring to their index number. Use the range() and len() functions to create a suitable iterable.
for i in range(len(vegetables)):
    print(vegetables[i])

# you can loop through the list items by using a while loop. Use the len() function to determine the length of the list then start at 0 and loop your way through the list items by referring to their index.
i = 0
while i < len(vegetables):
    print(vegetables[i])
    i += 1

# you can loop through the list compherension which offers the shortest syntax for looping through lists.
[print(x) for x in vegetables]


# SORT LISTS
# the sort() method sorts the list alphanumerically, ascending by default.
vegetables.sort()
print(vegetables)

# sort numerically
numbers = [100, 50, 6, 82, 44]
numbers.sort()
print(numbers)

# to sort descending, use the keyword argument reverse = True
vegetables.sort(reverse=True)
numbers.sort(reverse=True)
print(vegetables)
print(numbers)

# if you want a case-insensitive sort function use str.lower as a key function
cars = ["Ford", "BMW", "Volvo", "audi", "mercedes"]
cars.sort(key=str.lower)
print(cars)

# if you want to reverse the order of a list regardless of the alphabetic order use the reverse() method.
cars.reverse()
print(cars)


# COPY LISTS

# use the copy() method to make a copy of a list
names = ["pauline", "kate", "maggie"]
names_copy = names.copy()
print(names_copy)

# another way of making a copy is to use the built-in method list()
names_copy2 = list(names)
print(names_copy2)

# you can also make a copy of a list by using the : slice operator
names_copy3 = names[:]
print(names_copy3)

# JOIN LSTS

# use the + operator
schoolList = ["kinoo primary", "kinoo secondary", "kinoo academy"]
universityList = ["university of nairobi", "strathmore university", "kenyatta university"]
educationList = schoolList + universityList
print(educationList)

# another way to join two lists is by appending all the items from  universityList to schoolList using the append() method.
for x in universityList:
    schoolList.append(x)
print(schoolList)

# can use the extend() method where the purpose is to add elements from one list to another list
schoolList.extend(universityList)
print(schoolList)