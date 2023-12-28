#!/usr/bin/python3
"""
A simple program that reads from a password list and compares user password to determine
their access to the portal.
"""

# open userpassword file and closes file automatically 
with open('secretpass.txt') as passfile:
    password = [passcode.strip() for passcode in passfile]

# accepts user password
userpass = input("Enter you saved password\n")

# check if the entered password matches any correct password
if userpass in password: #compares userpassword to the saved password
    print("You are welcome to your page.\n")
    if userpass == '09873a':
        print("Add more special characters to make your password stronger.\n")
    else:
        print("You have a good password.")
else:
    print("You have no permission to access this portal.\nGoodbye!")