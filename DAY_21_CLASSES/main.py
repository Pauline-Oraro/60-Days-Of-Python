# Python is an object oriented language which allows you to structure your code using classes and objects.

# A class defines what an object should look like and an object is created based on that class. A class is like a blueprint for creating objects.

# to create a class use the keyword class.

class my_class:
    x = 111

print(my_class)

# to create an object use the class name followed by parentheses.
my_object = my_class()
print(my_object.x)

# you can delete objects by using the del keyword.

# you can create multiple objects from the same class and each object is independent and has its own copy of the class properties.
object1 = my_class()
object2 = my_class()
print(object1.x)
print(object2.x)

# class definations cannot be empty but if you for some reason have a class definition with no content put in the pass statement to avoid getting an error.

class person:
    pass


# __init__()method

# All classes have a built-in method called __init__() which is always executed when the class is being initiated. It is used to assign values to object properties or to perform operations that are necessary when the object is being created.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("John", 20)
print("The first student is" , student1.name, " and he is " , student1.age, " years old.")

student2 = Student("Jane", 22)
print("The second student is" , student2.name, " and she is " , student2.age, " years old.")

student3 = Student("Jack", 21)
print("The third student is" , student3.name, " and he is " , student3.age, " years old.")


# SELF PARAMETER

# The self parameter is a reference to the current instance of the class and it is used to access properties and methods that belong to the class. 
# It must be the first parameter of any method in the class. Without self python would not know which object properties you want to access. 
# It does not have to be named self you can call it whatever you like but it has to be the first parameter of any method in the class. but it is strongly recommended to use self as it is the convention in python and makes your code more readable to others.

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print("Car brand: " + self.brand)
        print("Car model: " + self.model)
        print("Car year: " + str(self.year))

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()

car2 = Car("Honda", "Civic", 2019)
car2.display_info()

car3 = Car("Ford", "Mustang", 2021)
car3.display_info()


# CLASS PROPERTIES

# Properties are variables that belong to a class. they store data for each object created from the class
# you can access properties using the dot notation.

class this_person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person1 = this_person("Alice", 30)
print(person1.name)

person2 = this_person("Bob", 25)
print(person2.age)

# you can modify the value of properties

person1.name = "Charlie"
print(person1.name)

# you can delete properties from objects using the del keyword.

# properties defined inside __init__() belong to each object and are called instance properties. Properties defined outside methods belong to the class itself and are called class properties and are shared by all objects

class Dog:
    species = "Canis familiaris" # class property

    def __init__(self, name, age):
        self.name = name # instance property
        self.age = age # instance property

dog1 = Dog("Buddy", 5)
print(dog1.name) # accessing instance property
print(dog1.species) # accessing class property

# you can add new properties to existing objects
dog1.breed = "Labrador"
print(dog1.breed) # accessing new property


# CLASS METHODS

# Methods are functions that belong to a class and they define the behavior of objects created from the class and all methods must have the self parameter as the first parameter

class my_person:
    def __init__(self, name, country, age):
        self.name = name
        self.country = country
        self.age = age

    def info(self):
            print("Name: " + self.name)
            print("Country: " + self.country)
            print("Age: " + str(self.age))

person_one = my_person("Pauline", "USA", 28)
person_one.info()

# the __str__() method is a special method that controls what is returned when the object is printed.

class another_person:
    def __init__(self, name, country, age):
        self.name = name
        self.country = country
        self.age = age
    def __str__(self):
        return f"{self.name} is from {self.country} and is {self.age} years old."

person_two = another_person("David", "UK", 35)
print(person_two)


# PYTHON INHERITANCE

# Inheritance allows us to define a class that inherits all the methods and properties from another class.
#  The parent class being inherited fromand is also called the base class while the child class is the class that inherits from another class also called the derived class.

class Organization:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def organization_info(self):
        print("Organization Name: " + self.name)
        print("Location: " + self.location)

first_org = Organization("Tech Company", "New York")
first_org.organization_info()

class Department(Organization):
    pass
department1 = Department("Tech database department", "New York")
department1.organization_info()

class Employee(Organization):
    def __init__(self, name, location, employee_name, employee_id):
        super().__init__(name, location)
        self.employee_name = employee_name
        self.employee_id = employee_id

    def employee_info(self):
        print("Employee Name: " + self.employee_name)
        print("Employee ID: " + str(self.employee_id))

employee1 = Employee("Tech Company", "New York", "Pauline Oraro", 12345)
employee1.employee_info()