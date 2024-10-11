#Palindrome

print("Check if the word or number is Palindrome")
string = input("Enter a string: ")

s = string.replace(" ", "").lower()
is_palindrome = s == s[::-1]

if is_palindrome:
    print(f"'{string}' is a palindrome")
else:
    print(f"'{string}' is not a palindrome")
