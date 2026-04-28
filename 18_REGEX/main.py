# A regex or regular expression is a sequence of characters that form a search pattern. It can be used to check if a string contains the specified search pattern.

# Python has a built in package called re which can be used to work with regular expressions

# the search() function searches the string for a match and returns a match object if there is a match. If there is more than one match, only the first occurrence of the match will be returned. If there is no match, the value None will be returned.

import re

my_text = "The rain in Kenya"
my_search = re.search("^The.*Kenya$", my_text)

if my_search:
    print("yes we have a match")
else:
    print("no match")

# the match object is an object containing information about the search and the result. If there is no match the value none will be returned instead of the match object.
print(my_search)

# the span() returns a tuple containing the start and end positions of the match.

my_fifth_search = re.search(r"\bK\w+", my_text)
print(my_fifth_search.span())

#the string returns the string passed into the function.
my_sixth_search = re.search(r"\bK\w+", my_text)
print(my_sixth_search.string)

# group() returns the part of the string where there was a match
my_seventh_search = re.search(r"\bK\w+", my_text)
print(my_seventh_search.group())


# the findall() function returns a list containing all matches. If there is no match, an empty list will be returned.
my_second_search = re.findall("ai", my_text)
print(my_second_search)

# the split() function returns a list where the string has been split at each match
my_third_search = re.split("\s", my_text)
print(my_third_search)

# the sub() function replaces the matches with the text of your choice
my_fourth_search = re.sub("\s", "9", my_text)
print(my_fourth_search)

# METACHARACTERS

#  Are characters with special meaning
this_text = "Python is a programming language. Python is popular."

# [ ] A set of characters. A match will occur if any of the characters in the set are present in the searched string
search_one = re.findall("[a-m]", this_text)
print(search_one)

# \ signals a special sequence and can also be used to escape special characters.
search_two = re.findall("\d", this_text)
print(search_two)

# . any character except a new line character
search_three = re.findall("P..hon", this_text)
print(search_three)

# ^ starts with
search_four = re.findall("^Python", this_text)
print(search_four)

# $ ends with
search_five = re.findall("popular.$", this_text)
print(search_five)

# * zero or more occurrences
search_six = re.findall("Pytho*n", this_text)
print(search_six)

# + one or more occurrences
search_seven = re.findall("Pytho+n", this_text)
print(search_seven)

# ? zero or one occurrences
search_eight = re.findall("Pytho?n", this_text)
print(search_eight)

# {n} exactly n occurrences
search_nine = re.findall("Pytho{2}n", this_text)
print(search_nine)