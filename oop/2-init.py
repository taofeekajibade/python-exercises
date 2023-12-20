''' create a class named Student with the class keyword '''


class Student:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello everyone, my name is", self.name)

''' create an instance of the class with its argument and call its method. '''
p = Student('Taofeek Ajibade')
p.say_hello()

''' instance and method of the class in a combined form. '''
Student("Stephen Aguero").say_hello()
Student("Julius Agahowa").say_hello()
Student("Celestine Babayaro").say_hello()

print()

class myInit:
    def __init__(self, name=None):
        self.name = name
        print("This is how to initialize an instance with __init__.")
    
    def greet(self):
        if self.name:
            print(f"I am {self.name}.")
        else:
            print("I have no name whatsoever!")
    
first_instance = myInit()
first_instance.greet()

second = myInit("Kolawole").greet()