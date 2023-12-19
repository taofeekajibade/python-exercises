# OBJECT-ORIENTED PROGRAMMING

Object Oriented Programming (OOP) is a way of organizing program by combining data and functionality into one object. It is divided into two aspects: **classes and objects.** Objects can store data using variables - variables that belong to a class, or an object are called **fields.** Similarly, the functions that belong to class are called **methods** and they can be used by objects as well. The collective names for fields and methods is **attributes.** In summary, in OOP, variables are fields, functions are methods. The two combined are called attributes.

Also, fields are divided into two: **instance/object variables** (those that belong to instance/object of the class) and **class variables** (those that belong to the class themselves).

## CLASSES
A class is created with the keyword *class.* The fields and methods of the class are listed in an indented block. A class method is distinguished from conventional function with the keyword **self.** Thus, even when a function does not take parameters, it must have the name (parameter) _self._ While any name can be used in place of _self,_ it is strongly advisable to use the general self as it is easily recognisable by both the reader and the IDEs. Below is a code sample of class definition with its attributes:

''''python
class MyClass:
    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    def class_method(self):
        print("This is a class method.")
''''

## INHERITANCE
OOP allows easy reuse of codes through inheritance. By this method, sub-classes are able to inherit some common traits from the base class. For instance, if we have a community of people, they may share some common attributes (variables) such as age, gender, ethnicity and language, Depending on their training or capacity, they may also differ in certain other afas such social class/status, politcal affliations, profession and the likes. When the population is stratified, certain common attributes can simply be inherited from the base population rather than writing such fields afresh. Thus, traits that vary among individuals, such as social class, political affiliations, or profession, can be defined in specific sub-classes. Below is a code sample of inheritance:

''''python
class Person:
    def __init__(self, age, gender, ethnicity, language):
        self.age = age
        self.gender = gender
        self.ethnicity = ethnicity
        self.language = language

class Professional(Person):
    def __init__(self, age, gender, ethnicity, language, profession):
        super().__init__(age, gender, ethnicity, language)
        self.profession = profession
''''
