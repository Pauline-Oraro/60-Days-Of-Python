# Python has several functions for creating, reading, updating and deleting files.

from pathlib import Path

# The key function for working with files in python is the open() function and it takes two parameters; filename and mode.

# there are four different methods for opening a file:
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist.
# "a" - Append - Opens a file for appending, creates the file if it does not exist.
# "w" - Write - Opens a file for writing, creates the file if it does not exist.
# "x" - Create - Creates the specified file, returns an error if the file exists

# in addition you can specify if the file should be handled as binary or text mode.
# "t" - Text - Default value. Text mode.
# "b" - Binary - Opens a file in binary mode.

# by default the read() method returns the whole text but you can also specify how many characters you want to return

# can return one line by using the readline() method

# it is a good practice to always close the file after you are done with it. You can do this using the close() method.

file = open(Path(__file__).parent / "demofile.txt")
print(file.read())
print(file.read(5))
print(file.readline())
file.close()

# can use the with statement when opening a file
with open(Path(__file__).parent / "demofile.txt") as my_file:
    print(my_file.read())

# to write to an existing file you must add a parameter to the open() function: "a" for append and "w" for write. The "a" parameter will append to the end of the file, while the "w" parameter will overwrite any existing content in the file.

with open(Path(__file__).parent / "demofile.txt", "a") as this_file:
    this_file.write(" Now the file has more content!")

with open(Path(__file__).parent / "demofile.txt") as this_file:
    print(this_file.read())


# to delete a file, you must import the OS module, and run its os.remove() function.