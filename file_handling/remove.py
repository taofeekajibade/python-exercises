"""To delete a file, the OS module is first imported,
and then, os.remove() is run
"""

import os
from sys import argv

""" You can remove the comment in lines 9, and 14 - 32 to test this first code.
Remember to comment out the second code block below it
from line 41 till end so as to avoid conflicts.
"""
# script, filename = argv

# """ To prevent the command from runnng into error,
# we may check if the file exists before trying to delete it.
# """
# if os.path.exists(filename):
#     os.remove(filename)
# else:
#     print("The file does not exist.")

# print("Now, I will ask you for three sentences.")
# sent1 = input("sent1 - ")
# sent2 = input("sent2 - ")
# sent3 = input("sent3 - ")

# print("I am writing the lines to a new file.")
# file1 = input("> ")
# demofile = open(file1, "x")
# demofile.write(f"{sent1}\n{sent2}\n{sent3}")
# demofile.close()

# demofile = open(file1)
# print(demofile.read())
# demofile.close()


"""
The code below is written to copy the content of a file into another file.
old_file represens an existing file while new_file is the name of a file into which we want to write.
The new_file can as well be either another existing file, or an entirely new file.
"""
script, old_file, new_file = argv

print(f"I want to copy from {old_file} to {new_file}")

print(f"I need to check if the {old_file} exists: {os.path.exists(old_file)}")

file2 = open(old_file)
file_read = file2.read()

input("Enter the file name here: ")

write_file = open(new_file, "w")
write_file.write(file_read)

print(f"I have just copied the content of {old_file} into {new_file}")

write_file.close()
file2.close()