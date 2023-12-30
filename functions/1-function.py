from sys import argv

script, input = argv

def print_all(a):
    print(a.read())

def rewind(a):
    a.seek(0)

def print_a_line(line, a):
    print(line, a.readline())

current_file = open(input)

print("Now, we print the entire file.\n")

print_all(current_file)

print("Okay, we can rewind and go back to the start.")
rewind(current_file)

print("I want to print the first four lines.")

latest_line = 1
print_a_line(latest_line, current_file)

latest_line = latest_line + 1
print_a_line(latest_line, current_file)

latest_line = latest_line + 1
print_a_line(latest_line, current_file)