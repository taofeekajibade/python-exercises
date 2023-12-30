"""define a simple function that takes no argument"""
def Say_hello():
    print("Hello, you are welcome here.")

"""define a function that takes one argument"""
def One_args(argv):
    print(f"Welcome, {argv}")

""""define a function with two arguments"""
def print_two_nums(*argv):
    args1, args2 = argv
    print(f"args1: {args1}, args2: {args2}")
    # print(f"The user name is {args1} {args2}")

"""It can also be written in this way"""
def print_two_args(args1, args2):
    # print(f"args1: {args1}, args2: {args2}")
    print(f"The user name is {args1} {args2}")

"""define a function to add two numbers"""
def addition(a, b):
    print(f"The addition of {a} and {b} is: {a +b}")

"""define a function to multply two numbers"""
def multiply(x, y):
    print(f"The multiplication of {x} and {y} is: {x * y}")

Say_hello()
One_args("Taofeek")
print_two_nums("Taofeek", "Ajibade")
print_two_args("Abdulhayy", "Adelani")
addition(45, 67)
multiply(15, 12)
addition(45 + 15, 67 + 33) # we can do some isolated calculations inside each variable.
