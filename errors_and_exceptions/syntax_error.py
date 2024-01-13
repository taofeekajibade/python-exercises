while True:
    try:
        x = int(input("Enter a value between 1 and 10 "))
        print(f"You have entered {x}")
        break
    except ValueError:
        print("That is not a valid value. Try again. ")