#!/usr/bin/python3

# if statement

"""
x = int(input("Enter a value here: "))
if x < 0:
    x = /  
    print("You have entered a negative value")
elif x == 0:
    print("You entered zero")
elif x == 1:
    print("This is one")
else:
    print("That is more than 1")


# for statement
# it iterates over items of any sequence in the order the appear

laptops = ["HP", "Dell", "Acer", "Samsung", "Apple"]
for model in laptops:
    print(model, "-", len(model), end='; ')


users = {'Taofeek': 'Daily', 'Abdulhayy': 'Weekly', 'Ataulhayy': 'Daily',
         'Nurulhayy': 'Weekly'}

# Iterate over a copy of user records

for user, frequency in users.copy().items():
    if frequency == 'Daily':
        del users[user]

# create a new collection
heavy_users = {}
for user, frequency in users.items():
    if frequency == 'Daily':
        heavy_users[user] = frequency
        print(heavy_users)

# range

for number in range(100):
    if number % 2 == 0:
        print(number, end=', ')

print(list(range(2, 100)))
print(range(2, 100, 3))

"""


username = 'Taofeek'
passkey = 'cleargoal'

print("Enter your name and password here")

name = input()
Pass = str(input())

if name == username:
    print("Hello,", username)
    if Pass == passkey:
        print("You are welcome to your inbox,", username)
    else:
        print("You have entered a wrong password")