#2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

def get_integer():
#Handling a Exception
    try:
        user_input = input("Enter an integer: ")
        user_input = int(user_input)
        print(f"You entered the integer: {user_input}")
    except ValueError:
        print("Error: That's not a valid integer. Please enter an integer.")

# Example usage
get_integer()


"""Ans: Enter an integer: 2.5
Error: That's not a valid integer. Please enter an integer."""

