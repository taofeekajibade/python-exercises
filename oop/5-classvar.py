"""create a class"""
class Employee:
    """define the instance variables"""
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = (f"{first}.{last}@company.com")

    def fullname(self):
        """define fullname method"""
        return (f"{self.first} {self.last}")

    def apply_raise(self):
        self.pay = (f"The new pay is now {int(self.pay * 1.24)}")
        return self.pay
        

emp_1 = Employee('Taofeek', 'Ajibade', 70000)
emp_2 = Employee('Oriogbade', 'Alomaja', 45000)
emp_3 = Employee('Elizabeth', 'Olaniyi', 84000)
print(emp_1.fullname())
print(emp_2.fullname())
print(emp_3.fullname())
print()
print(emp_1.pay)
print(emp_2.pay)
print(emp_3.pay)
print()
print(emp_1.apply_raise())
print(emp_2.apply_raise())
print(emp_3.apply_raise())
print()
print(emp_1.email.lower())
print(emp_2.email.lower())
print(emp_3.email.lower())
print()