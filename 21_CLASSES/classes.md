# Python Classes & Object-Oriented Programming (OOP)

Python is an **object-oriented language** which allows you to structure your code using **classes** and **objects**.

- A **class** is a blueprint that defines what an object should look like.
- An **object** is an instance created from that class.

---

## 1. Creating a Class & an Object

Use the `class` keyword to define a class. To create an object, use the class name followed by parentheses.

```python
class my_class:
    x = 111

print(my_class)        # <class '__main__.my_class'>

my_object = my_class()
print(my_object.x)     # 111
```

### Multiple Objects from One Class

Each object is independent and has its own copy of the class properties.

```python
object1 = my_class()
object2 = my_class()
print(object1.x)  # 111
print(object2.x)  # 111
```

### Deleting an Object

```python
del my_object
```

### `pass` — Empty Class Placeholder

Class definitions cannot be empty. Use `pass` to avoid a syntax error when the body hasn't been implemented yet.

```python
class person:
    pass
```

---

## 2. The `__init__()` Method

`__init__()` is a built-in method that is **automatically called** every time a new object is created from the class. It is used to assign values to object properties when the object is being initialized.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("John", 20)
student2 = Student("Jane", 22)
student3 = Student("Jack", 21)

print("The first student is", student1.name, "and he is", student1.age, "years old.")
print("The second student is", student2.name, "and she is", student2.age, "years old.")
print("The third student is", student3.name, "and he is", student3.age, "years old.")
```

---

## 3. The `self` Parameter

`self` is a reference to the **current instance** of the class and is used to access properties and methods that belong to that object.

| Rule | Detail |
|------|--------|
| Must be the **first parameter** of any method | Without it, Python doesn't know which object to use |
| Can technically be named anything | But `self` is the strong convention — don't change it |
| Not passed when calling the method | Python passes it automatically |

```python
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
```

---

## 4. Class Properties

Properties are variables that store data for each object. They are accessed using **dot notation**.

### Instance Properties vs Class Properties

| Type | Defined In | Belongs To | Shared? |
|------|-----------|------------|---------|
| **Instance property** | Inside `__init__()` | Each individual object | No |
| **Class property** | Outside any method | The class itself | Yes — all objects share it |

```python
class Dog:
    species = "Canis familiaris"   # class property — shared by all

    def __init__(self, name, age):
        self.name = name           # instance property — unique per object
        self.age = age

dog1 = Dog("Buddy", 5)
print(dog1.name)      # Buddy  (instance property)
print(dog1.species)   # Canis familiaris  (class property)
```

### Modifying & Adding Properties

```python
person1 = this_person("Alice", 30)
person1.name = "Charlie"   # modify existing property
print(person1.name)        # Charlie

dog1.breed = "Labrador"    # add a new property to an existing object
print(dog1.breed)          # Labrador
```

### Deleting a Property

```python
del person1.name
```

---

## 5. Class Methods

Methods are **functions that belong to a class** and define the behaviour of objects. All methods must have `self` as the first parameter.

```python
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
```

### The `__str__()` Method

A special method that controls what is returned when an object is **printed**. Without it, printing an object shows a memory address.

```python
class another_person:
    def __init__(self, name, country, age):
        self.name = name
        self.country = country
        self.age = age

    def __str__(self):
        return f"{self.name} is from {self.country} and is {self.age} years old."

person_two = another_person("David", "UK", 35)
print(person_two)
# David is from UK and is 35 years old.
```

---

## 6. Inheritance

Inheritance allows a class to **inherit all the methods and properties** from another class.

| Term | Also Called | Description |
|------|-------------|-------------|
| **Parent class** | Base class | The class being inherited from |
| **Child class** | Derived class | The class that inherits from the parent |

### Parent Class

```python
class Organization:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def organization_info(self):
        print("Organization Name: " + self.name)
        print("Location: " + self.location)

first_org = Organization("Tech Company", "New York")
first_org.organization_info()
```

### Child Class

Use `super().__init__()` to call the parent class constructor and inherit its properties.

```python
class Employee(Organization):
    def __init__(self, name, location, employee_name, employee_id):
        super().__init__(name, location)       # inherit from Organization
        self.employee_name = employee_name
        self.employee_id = employee_id

    def employee_info(self):
        print("Employee Name: " + self.employee_name)
        print("Employee ID: " + str(self.employee_id))

employee1 = Employee("Tech Company", "New York", "Pauline Oraro", 12345)
employee1.employee_info()
```

> **`super()`** gives you access to the parent class without needing to name it explicitly — making your code easier to maintain.

---

## Special Methods Summary

| Method | Description |
|--------|-------------|
| `__init__(self, ...)` | Called automatically when an object is created |
| `__str__(self)` | Controls what is returned when the object is printed |

---

## Quick Reference

| Concept | Syntax |
|---------|--------|
| Define a class | `class MyClass:` |
| Create an object | `obj = MyClass()` |
| Access a property | `obj.property` |
| Modify a property | `obj.property = value` |
| Delete a property | `del obj.property` |
| Delete an object | `del obj` |
| Initialize with values | `def __init__(self, ...)` |
| Define a method | `def method_name(self):` |
| Inherit from a parent | `class Child(Parent):` |
| Call parent constructor | `super().__init__(...)` |
