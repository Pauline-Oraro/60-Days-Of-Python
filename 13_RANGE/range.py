# The built in range() function returns an immutable sequence of numbers commonly used for looping a specific number of times. This set of numbers has its own data type called range.

# The range() function can be called with 1, 2, or 3 arguments using this syntax: range(start, stop, step).

# The range object is a data type that represents an immutable sequence of numbers and is not directly displayable. ranges are often converted to lists for display.

# If the range function is called with only one argument the argument represents the stop value.

first_range = range(10)
print(first_range)
print(list(first_range))

# if the range function is called with two arguments the first argument represents the start value and the second argument represents the stop value.

second_range = range(1, 10)
print(second_range)
print(list(second_range))

# if the range function is called with three arguments the third argument represents the step value. The step value means the difference between each number in the sequence. It is oprional and if not provided it defaults to 1.

third_range = range(1, 10, 2)
print(third_range)
print(list(third_range))

# ranges are often used in for loops to iterate over a sequence of numbers.

for i in range(10):
    print(i)

# Ranges can be sliced to extract a subsequence.

sliced_range = range(10)
print(sliced_range[2])
print(sliced_range[2:5])
print(sliced_range[:3])

# ranges support membership testing with the in operator

fourth_range = range(0, 10, 2)
print(5 in fourth_range)
print(6 in fourth_range)
print(7 in fourth_range)
print(8 in fourth_range)

# ranges support the len() function to get the number of elements in the range.
print(len(fourth_range))