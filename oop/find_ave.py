print("Please enter any five numbers:")
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = input()
num5 = input()

sum = int(num1 + num2 + num3 + num4 + num5)
average = int(sum/5)

print(f"The average is {average}")

if num1 > num2:
    max = num1
else:
    max = num2
if max > num3:
    max = max
else:
    max = num3
if num4 > max:
    max = num4
else:
    max = max
if num5 > max:
    max = num5
else:
    max = max
print(f"{max} is the maximum value.")