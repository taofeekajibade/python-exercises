"""
try:
   print(x)
except:
   print("An exception has occurred!")

try:
    print(0/10)
    print(2*5)
except ZeroDivisionError:
    print("You cannot divide a value by zero")
except:
    print("Something else went wrong.")

"""


try:
    with open('data.txt') as file:
        new_file = file.read()
except FileNotFoundError as fnf_errn:
    print(fnf_errn)
    print("The file cannot be loaded.")
