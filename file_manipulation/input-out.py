""" import the necessary module for argv """
from sys import argv

""" enter the name of the file to be opened """
script, filename = argv

text = open(filename)
print(f"Here is the file {filename}:")
print(text.read())

''' enter another file name below '''
print("Enter a new filename: ")
new_file = input("> ")

read_file = open(new_file)
print(read_file.read())