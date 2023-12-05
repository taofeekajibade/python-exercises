#!/usr/bin/python3

with open('secretpass.txt') as passFile:
    password = passFile.read().strip()

print("Enter your password")

userpassword = input()

if userpassword == password:
    print("Access granted")
    if userpassword == '09873a':
        print("Add more special characters to the password")
else:
    print("You have no permission here")
