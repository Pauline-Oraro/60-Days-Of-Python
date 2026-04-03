# A data type is the type of data a variable has.
# Variables can store data of different types. For example, a variable can store a string, an integer, a float, or a boolean value.
# In Python the data type is set when you assign a value to a variable.

#String data type. This is a sequence of characters enclosed in quotes. It can be single quotes, double quotes, or triple quotes.
stringDataType = "This is a string data type"
print(stringDataType)
print(type(stringDataType))

#Integer data type. This is a whole number without a decimal point.
integerDataType = 42
print(integerDataType)
print(type(integerDataType))

#Float data type. This is a number with a decimal point.
floatDataType = 3.33
print(floatDataType)
print(type(floatDataType))

#complex data type. This is a number with a real and an imaginary part. The imaginary part is denoted by the letter j.
complexDataType = 1j
print(complexDataType)
print(type(complexDataType))

#list data type. This is an ordered collection of items, which can be of different types.
listDataType = ["pauline", "junior", "jack"]
print(listDataType)
print(type(listDataType))

#tuple data type. A tuple is an ordered and immutable collection of items, which can be of different types.
tupleDataType = ("apples", "bananas", "cherries")
print(tupleDataType)
print(type(tupleDataType))


#range data type. This is a sequence of numbers, typically used in loops.
rangeDataType = range(0,7)
print(rangeDataType)
print(type(rangeDataType))


#dict data type. This is a collection of key-value pairs, where each key is unique.
dictDataType = {"name": "pauline", "age": 25, "city":"nairobi"}
print(dictDataType)
print(type(dictDataType))

#set data type. This is an unordered collection of unique items.
setDataType = {"pauline", "junior", "jack"}
print(setDataType)
print(type(setDataType))

#frozenset data type. This is an unordered collection of unique items that cannot be modified.
frozensetDataType = frozenset({"pauline", "junior", "jack"})
print(frozensetDataType)
print(type(frozensetDataType))

#bool data type. This is a data type that can only have two values: True or False.
boolDataType = True
print(boolDataType)
print(type(boolDataType))

#bytes data type. This is a sequence of bytes, which is used to store binary data.
bytesDataType = b"Hello, World!"
print(bytesDataType)
print(type(bytesDataType))

#bytearray data type. This is a mutable sequence of bytes, which is used to store binary data.
bytearrayDataType = bytearray(5)
print(bytearrayDataType)
print(type(bytearrayDataType))


#memoryview data type. This is a memory view object that allows you to access the memory of another object without copying it.
memoryviewDataType = memoryview(bytesDataType)
print(memoryviewDataType)
print(type(memoryviewDataType))


# if you want to specify the data type you can use the built-in functions.
stringType = str("This is python programming")
print(stringType)

integerType = int(42)
print(integerType)

floatType = float(3.333)
print(floatType)

complexType = complex(4j)
print(complexType)

listType = list(("kate", "nicole", "treasure"))
print(listType)

tupleType = tuple(("candy", "lolipop", "jawbreaker"))
print(tupleType)

rangeType = range(0,10)
print(rangeType)

dictType = dict(name="pauline", age=25, city="nairobi")
print(dictType)

setType = set(("akinyi", "omondi", "anyango"))
print(setType)

frozensetType = frozenset(("mombasa", "nairobi", "kisumu"))
print(frozensetType)

boolType = bool(1)
print(boolType)

bytesType = bytes(5)
print(bytesType)

bytearrayType = bytearray(5)
print(bytearrayType)

memoryviewType = memoryview(bytesType)
print(memoryviewType)