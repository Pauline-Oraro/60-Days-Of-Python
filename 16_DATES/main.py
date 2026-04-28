# A date in python is not a data type of its own but we can import a module named datetime to work with dates as date objects.

# The date contains year, month, day, hour, minute, second and microsecond.

import datetime

today = datetime.datetime.now()
print(today)

# return the year and name of weekday
print(today.year)
print(today.strftime("%A"))

# To create a date we can use the datetime() class constructor of the datetime module. The datetime() class requires three parameters to create a date: year, month, day.

my_birthday = datetime.datetime(2001,1,11)
print(my_birthday)

# The datetime object has a method for formatting date objects into readable strings. The method is called strftime().

print(today.strftime("%B %d, %Y"))