# Dictionaries are used to store data values in key: value pairs. 
# A dictionary is a collection which is ordered, changeable and do not allow duplicates.
# Dictionaries are written with curly brackets and have keys and values.

myCarBrand = {
    "brand": "Mercedes",
    "model": "AMG",
    "year": 2023
}
print(myCarBrand)

# Dictionary items are presented in key:value pairs and can be referred to by using the key name.
print(myCarBrand["brand"])

# A dictionary is ordered meaning that the items have a defined order and that order will not change.

# Dictionaries are changeable meaning that we can change, add or remove items after the dictionary has been created.

# Dictionaries cannot have two items with the same key. Duplicate values will overwrite existing values.

# To determine how many items a dictionary has use the len() function.
print(len(myCarBrand))

# The values in dictionary items can be of any data type
student = {
    "name": "Pauline Oraro",
    "course": "Bachelor of science in information technology",
    "year":2025,
    "languages": ["english","swahili","luo"]
}
print(student)

# Dictionaries are defined as objects with the data type called dict.
print(type(student))

# Can use the dict() constructor to make a dictionary.
studentOne = dict(name = "kate", age = 20, country = "Tanzania")
print(studentOne)


# ACCESS DICTIONARY ITEMS

# you can access the items of a dictionary by referring to its key name inside the square brackets
studentTwo = {
    "name" : "Miguel",
    "age" : 23,
    "course": "Bachelor of science in game development",
    "year": 2026
}
course = studentTwo["course"]
print(course)

# can use the get() method to access items of a dictionary
print(studentTwo.get("year"))

# the keys() method will return a list of all the keys in the dictionary
keys = studentTwo.keys()
print(keys)

# the values() method will return a list of all the values in the dictionary.
values = studentTwo.values()
print(values)

# the items() method will return each item in a dictionary as tuples in a list.
items = studentTwo.items()
print(items)

# to determine if a specified key is present in a dictionary use the in keyword.
if "course" in studentTwo:
    print("Yes, 'course' is one of the keys in studentTwo dictionary")


# CHANGE DICTIONARY ITEMS

# you can change the value of a specific item by referring to its key name
studentTwo["year"] = 2024
print(studentTwo)

# the update() method will update the dictionary with the items from the given argument. The argument must be a dictionary or an iterable object with key:value pairs.
studentTwo.update({"course" : "Bachelor of science in software development"})
print(studentTwo)


# ADD DICTIONARY ITEMS

#adding an item to the dictionary is done by using a new index key and assigning a value to it
studentTwo["campus"] = "Main Campus"
print(studentTwo)

# The update() method will update the dictionary with the items from a given argument. If the item does not exist the item will be added.
studentTwo.update({"favourite-color" : " blue"})
print(studentTwo)


# REMOVING DICTIONARY ITEMS

# the pop() methos removes the item with the specified key name.
studentTwo.pop("course")
print(studentTwo)

# the popitem() removes the last inserted item
studentTwo.popitem()
print(studentTwo)

# the del keyword removes the item with the specified key name.
del studentTwo["campus"]
print(studentTwo)

# the del keyword can also delete the dictionary completely.

# the clear() method empties the dictionary.
studentTwo.clear()
print(studentTwo)


# LOOPING THROUGH A DICTIONARY

# you can loop through a dictionary by using a for loop.
myName = {
    "FirstName" : "Pauline",
    "MiddleName" : "Akinyi",
    "SurName" : "Oraro",
    "NickName": "Hiltra"
}

for x in myName:
    print(x) # prints all the key names in a dictionary

# you can use the keys() method to return the keys of a dictionary.
for m in myName.keys():
    print(m)

# to print all values in the dictionary
for y in myName:
    print(myName[y])

# you can also use the values() method to return values of a dictionary.
for z in myName.values():
    print(z)

# you can loop through both keys and values by using the items() method

for a, b in myName.items():
    print(a, b)


# COPY DICTIONARIES

# Make a copy of a dictionary with the copy() method
realInformation = {
    "name": "Peter Alexander",
    "age": 55,
    "occupation" : "Programmer",
    "Place of work" : "Google",
    "Year of birth": 1970
}

copiedInformation = realInformation.copy()
print(copiedInformation)

# Make a copy of a dictionary with the dict() function
copiedTwo = dict(realInformation)
print(copiedTwo)


# NESTED DICTIONARIES

# a dictionary can contain dictionaries and this is called nested dictionaries

myFamily = {
    "FirstBorn":{
        "name" : "Pauline",
        "year" : 2001
    },
    "SecondBorn":{
        "name" : "Gilbert",
        "year": 2004
    },
    "ThirdBorn":{
        "name":"Treasure",
        "year":2020
    }
}

print(myFamily)

# to access items from a nested dictionary you use the name of the dictionaries starting with the outer dictionary
print(myFamily["FirstBorn"]["name"])

# you can loop through a dictionary by using the items() method 
for c, obj in myFamily.items():
    print(c)

    for k in obj:
        print(k + ':', obj[k])