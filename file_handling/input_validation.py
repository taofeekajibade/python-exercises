while True:
    try:
        age = int(input("Enter your age here: "))

    except:
        print("Enter your age in digit.")
        
        continue

    if age < 1:
        print("Your age must be greater than 1")
        
        continue
    break

print(f"You are {age} years old.", end=" ")
if age >= 18:
    print("you are an adult.")
else:
    print("You are still a child.")