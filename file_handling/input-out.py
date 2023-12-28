""" import the necessary module for argv """
from sys import argv

""" enter the name of the file to be opened """
script, filename = argv

text = open(filename)

print(text.read())

''' enter another file name below '''

print("Enter a new filename: ")
new_file = input("> ")

read_file = open(new_file)
print(read_file.read())

read_file.close() # remember to close the file after using it.

"""A third file here.
This appends a new content at the end of an existing file.
"""
print("Enter a new filename: ")
new_file = input("> ")

read_file = open(new_file, "a")
read_file.write("\nI am adding a new content as a demo.")
read_file.close()

"""open the file again to read its updated content."""
read_file = open(new_file)
print(read_file.read())

read_file.close()


"""open a third file. this is an entirely new text file.
this opens a new fileand write some content in it.
"""

print("Enter a new filename: ")
nfile = input("> ")

third_file = open(nfile, "x")
third_file.write("I am enjoying this file handling thing.")

third_file = open(nfile)

print(third_file.read())

third_file.close()