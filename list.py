#!/usr/bin/python3

# A list of comma-separated values enclosed within a square bracket.
# A list can contain items of either same, or different data types.

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
myFav = ["html", "css", "js", "python", "C"]
myLibrary = ["react", "django", "angular", "nodejs", "vue"]

# List support indexing and slicing
print(myList[:3])
print(myFav[2:])
print(myLibrary[-2:])

# Lists can also be concatenated
print(myList + myFav)

# Lists are mutable i.e their values can be changed

myFav[4] = "C++"
print(myFav)

# Values can also be appended to list using append() method
#
myList.append(11)
myFav.append("Typescript")

print(myList)
print(myFav)

# List allows slice to mutate values
# Slice has two end points - beginning index and ending index
# An ommitted first index defaults to zero
# An ommitted second index defaults to the size
# of the string that is being sliced.

secList = myList[0:3] 

myList[3:7] = [41, 51, 61, 71]

newList = myList
print(newList)
print(secList)
# Lenght of list can also be printed

print(len(myList))
print(len(myFav))
print(len(myLibrary))
# Fibonacci code

a = 0
b = 1
while b < 200:
    print(b, end=',')
    a, b = b, b+a
