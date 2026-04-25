# Pandas is a python library used for working with data sets. It has functions for analyzing, cleaning, exploring and manipulating data.

# Pandas allows us to analyze big data and make conclusions based on statistical theories. Pandas can clean messy data sets and make them readable and relevant.

# installing pandas: pip install pandas. Pandas is usually imported under the pd alias.

# A pandas series is like a column in a table.Data sets in Pandas are usually multi-dimensional tables called Dataframes. Series is like a column a dataframe is the whole table.

# creating pandas series with default index

import pandas as pd

nums  = [1,2,3,4,5]
series = pd.Series(nums)
print(series)

# creating pandas series with custom index

my_nums = [1,2,3,4,5]
my_series = pd.Series(my_nums, index=[1,2,3,4,5])
print(my_series)

fruits  = ['Orange', 'Banana', 'Mango']
fruits = pd.Series(fruits, index=[1,2,3])
print(fruits)

# creating pandas series from a dictionary

my_name = {
    'name' :'Paulie Oraro',
    'country': 'Kenya',
    'city':'Nairobi',
    'occupation':'Software engineer',
    'age':25
}

dict_series = pd.Series(my_name)
print(dict_series)

# creating a constant pandas series

constant_numbers = pd.Series(11, index = [1,2,3,4,5])
print(constant_numbers)

# creating dataframes from lists of lists

my_data = [
    ['Pauline', 'Kenya', 'Nairobi'],
    ['Alexandra', 'Tanzania', 'Dodoma'],
    ['Johnny', 'Uganda', 'Kampala']
]
my_dataframe = pd.DataFrame(my_data, columns = ['Names', 'Country', 'City'])
print(my_dataframe)

# creating dataframe using dictionary 

students = {
    'Name' : ['Paulie', 'Kate', 'Alexa', 'Joseph'],
    'Country' : ['Kenya', 'Uganda', 'Tanzania', 'Rwanda'],
    'City': ['Nairobi', 'Kampala', 'Dodoma', 'Kigali']
}
students_table = pd.DataFrame(students)
print(students_table)

# creating dataframes from a list of dictionaries

his_students = [
    {'Name': 'Asaph', 'Country': 'Finland', 'City': 'Helsinki'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}
]
his_students_table = pd.DataFrame(his_students)
print(his_students_table)
print(his_students_table.columns)
country = his_students_table['Country']
print(country)
