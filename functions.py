""""
A function is a piece of instruction to computer on what to do with a variable,
or a combination of variables.
"""

# Asks user to enter their name
name = input("What is your name?\n")

# Remove whitespaces an capitalize
name = name.strip().title()

# Says hello to user
print("Hello,", name)