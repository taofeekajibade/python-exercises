class Person:
    def __init__(self, first, last, age, id):
        self.first = first
        self.last = last
        self.age = age
        self.id = id

    def getName(self):
        return (f"{self.first} {self.last}")
    
    def getemail(self):
        return self.name + '@company.com'
    
    def isEmployed(self):
        return False
    
class Employee(Person):
    def __init__(self, first, last, age, id):
        Person.__init__(self, first, last, age, id)

    def bioData(self):
        return (f"{self.age} years' of age and his ID is {self.id}")
    def isEmployed(self):
        return True
    
tao = Person('Taofeek', 'Ajibade', 33, 103)
print(tao.getName())

tao = Employee('Ataulhayy', 'Adigun', 16, 342)
print(f"Mr {tao.getName()} is {tao.bioData()}. He is {tao.isEmployed()}")