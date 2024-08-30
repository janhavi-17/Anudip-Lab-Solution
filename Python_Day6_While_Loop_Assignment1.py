#1.Write a python program to check whether a number is palindrome or not?

def is_palindrome(number):
    # Store the original number
    original_number = number
    # Initialize the reverse of the number
    reverse_number = 0

    while number > 0:
        # Get the last digit of the number
        last_digit = number % 10

        # Update the reverse number
        reverse_number = (reverse_number * 10) + last_digit

        # Remove the last digit from the original number
        number = number // 10

    # Check if the original number is equal to its reverse
    return original_number == reverse_number

# Input from the user
number = int(input("Enter a number: "))

# Check if the number is a palindrome
if is_palindrome(number):
    print(number," is a palindrome.")
else:
    print(number," is not a palindrome.")


"""Ans: Enter a number: 101
101 is a palindrome."""
