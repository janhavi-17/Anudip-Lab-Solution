#1.Python program to check if the given string is a palindrome 

# Input string from the user
s = input("Enter a string: ")

# Convert to lowercase and remove non-alphanumeric characters
s = s.lower()
s = ''.join(c for c in s if c.isalnum())

# Check if the string is a palindrome
length = len(s)
is_palindrome = True
for i in range(length // 2):
    if s[i] != s[length - i - 1]:
        is_palindrome = False
    break

# Output the result
if is_palindrome:
    print(s," is a palindrome.")
else:
    print(s," is not a palindrome.")


"""Ans: Enter a string: SOs
sos  is a palindrome."""
