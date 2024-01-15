def reverse_str(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse_str(text)

user_input = input("Enter a text here: ")

if is_palindrome(user_input):
    print("The text is a palindrome.")
else:
    print("That is not a palindrome.")
