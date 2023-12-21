# Object Oriented Programming (OOP)

Object Oriented Programming (OOP) is a way of organizing program by combining data and functionality into one object. It is divided into two aspects: **classes and objects.** Objects can store data using variables - variables that belong to a class, or an object are called **fields.** Similarly, the functions that belong to class are called **methods** and they can be used by objects as well. The collective names for fields and methods is **attributes.** Also, fields are divided into two: **instance/object variables** (those that belong to instance/object of the class) and **class variables** (those that belong to the class themselves). In summary, in OOP, variables are fields, functions are methods. The two combined are called attributes.

## Classes
A class is created with the keyword *class.* The fields and methods of the class are listed in an indented block. A class method is distinguished from conventional function with the keyword **self.** Thus, even when a function does not take parameters, it must have the name (parameter) _self._ While any name can be used in place of _self,_ it is strongly advisable to use the general self as it is easily recognisable by both the reader and the IDEs. Below is a code sample of class definition with its attributes:

```python
class MyClass:
    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    def class_method(self):
        print("This is a class method.")     
```
As shown in the code above, a method is a function which belongs to a class (is defined within a class) and whose first parameter is a reference to the instance that calls the method. That is, any instance of the class that would use the method does so by way of referencing through the parameter, usually denoted with the word **self.** It is already noted that _self_ is not a python keyword, but rather, a naming convention.

## The `__init__` Method

Generally, the attributes of an instance are defined immediately it is created. The `__init__` is a method that is used to initialize an instance of a class and it is automatically called after the instance is created.

```python
class myInit:
    def __init__(self):
        print("This is how to initialize an instance with __init__")

first_instance = myInit()
```
***
OUTPUT:
        This is how to initialize an instance with __&#95;init&#95;__
***

A further example to distinguish between class variable and instance variable with detailed explanation is provided below:

```python
class School:

    status = 'private'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

a = School('Micfis International School')
b = School('Calvary College')

a.status                  # shared by all schools
# output: 'private'
b.status                  # shared by all schools
# output: 'private'
a.name                  # unique to a
# output: 'Micfis International School'
b.name                  # unique to b
# output: 'Calvary College'
```
**Class and Instance Variables**

- In the highlighted text, we see the definition of a class called "School" in Python.
- A class is a blueprint for creating objects (instances) that share similar characteristics and behaviours.
- Inside the class, there are two variables defined: "status" and "name".
- The variable "status" is a class variable, which means it is shared by all instances of the class.
- The variable "name" is an instance variable, which means it is unique to each instance of the class.

**Creating Instances of the School Class**

- After defining the School class, the highlighted text shows the creation of two instances of the class: "a" and "b".
- The instances are created by calling the class name as if it were a function, passing the desired arguments.
- In this case, the argument passed is the name of the private.
- The first instance is created with the name 'Micfis International School' and assigned to the variable "a".
- The second instance is created with the name 'Calvary College' and assigned to the variable "b".

**Accessing Class and Instance Variables**

- The highlighted text also demonstrates how to access the class and instance variables of the School class.
- To access a class variable, we use the syntax "class_name.variable_name".
- In this case, we can see that both "a.status" and "b.status" return the value 'private', which is the value of the class variable "status".
- To access an instance variable, we use the syntax "instance_name.variable_name".
- Here, "a.name" returns the value 'Micfis International School', which is the value of the instance variable "name" for the instance "a".
- Similarly, "b.name" returns the value 'Calvary College', which is the value of the instance variable "name" for the instance "b".

In summary, it is observed that:
- The code demonstrates the concept of class and instance variables in Python.
- Class variables are shared by all instances of a class, while instance variables are unique to each instance.
- Instances of a class can be created by calling the class name as a function and passing the desired arguments.
- Class and instance variables can be accessed using the syntax "class_name.variable_name" and "instance_name.variable_name" respectively.

## Inheritance
OOP allows easy reuse of codes through inheritance. By this method, sub-classes are able to inherit some common traits from the base class. For instance, if we have a community of people, they may share some common attributes (variables) such as age, gender, ethnicity and language, Depending on their training or capacity, they may also differ in certain other afas such social class/status, politcal affliations, profession and the likes. When the population is stratified, certain common attributes can simply be inherited from the base population rather than writing such fields afresh. Thus, traits that vary among individuals, such as social class, political affiliations, or profession, can be defined in specific sub-classes. Below is a code sample of inheritance:

```python
class Person:
    def __init__(self, age, gender, ethnicity, language):
        self.age = age
        self.gender = gender
        self.ethnicity = ethnicity
        self.language = language
        print(f"The person is {self.age} years old, a {self.gender}, {self.ethnicity}, and speaks {self.language}")

class Professional(Person):
    def __init__(self, age, gender, ethnicity, language, profession):
        super().__init__(age, gender, ethnicity, language)
        self.profession = profession
```

Certainly! This code defines two classes in Python: `Person` and `Professional`.

1. **Person Class:**
   - The `Person` class is a basic class that represents a person.
   - It has an `__init__` method (initializer) that takes four parameters: `age`, `gender`, `ethnicity`, and `language`.
   - The `__init__` method is used to initialize instance variables `age`, `gender`, `ethnicity`, and `language` with the values passed as parameters.

2. **Professional Class (Inherits from Person):**
   - The `Professional` class is a subclass of the `Person` class. This is indicated by `(Person)` in the class definition.
   - It has an additional parameter in its `__init__` method, namely `profession`, which represents the person's profession.
   - The `super().__init__(...)` line is used to call the initializer of the superclass (`Person`) with the values for `age`, `gender`, `ethnicity`, and `language`. This is done to reuse the initialization logic of the `Person` class.
   - After calling the superclass initializer, the `profession` attribute is initialized with the provided value.

Below is an example of how these classes might be used:

```python
# Creating an instance of the Person class
person = Person(25, 'Male', 'Caucasian', 'English')

# Creating an instance of the Professional class
professional = Professional(30, 'Female', 'Asian', 'Spanish', 'Engineer')

# Accessing attributes of the Person class
print(person.age, person.gender, person.ethnicity, person.language)

# Accessing attributes of the Professional class (including inherited attributes from Person)
print(professional.age, professional.gender, professional.ethnicity, professional.language, professional.profession)
```
This code demonstrates the basic usage of the `Person` and `Professional` classes, showing how the `Professional` class inherits attributes from the `Person` class and extends them with an additional attribute.