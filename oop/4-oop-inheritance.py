# create a class to represent a community of people

class MicfisSchool:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        print("We are glad to introduce {}, a {} member of this community".format(self.name, self.gender))

    print("_____________________________________________________________\n")

    def introduce(self):
        print("{} is {:d} years of age".format(self.name, self.age))

# Staff class can inherit the attributes of the super class - Micfisschool
class Staff(MicfisSchool):
    def __init__(self, name, age, gender, salary):

         # the attributes inherited from the school community.
        MicfisSchool.__init__(self, name, age, gender)

        # an additional field available only to any object of this class only.
        self.salary = salary        

    def introduce(self):
        MicfisSchool.introduce(self)
        print("Monthly wage is {:d}".format(self.salary))

# Student class can inherit the attributes of the super class - Micfisschool
class Student(MicfisSchool):
    def __init__(self, name, age, gender, score):
        MicfisSchool.__init__(self, name, age, gender)      #the attributes inherited from the school community.
        self.score = score # an additional field available only to any object of this class only.
    
    def introduce(self):
        MicfisSchool.introduce(self)
        print("{}, a student of this school scored a total {:d} in his exams.".format(self.name, self.score))

t = Staff('Mr. Egbedele', 45, 'male', 72000)
x = Staff('Mrs. Olaniyi', 35, 'female', 85000)
y = Student('Akeem Olayiwola', 16, 'male', 97)

members = [t, x, y]
for member in members:
    member.introduce()
    