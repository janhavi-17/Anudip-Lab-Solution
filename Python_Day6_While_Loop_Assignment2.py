#2.Write a python program finding the factorial of a given number using a while loop

def factorial(number):
    # Initialize the result to 1
    result = 1
    
    # Loop to multiply the result with each number until it reaches 1
    while number > 1:
        result *= number
        number -= 1
    
    return result

# Input from the user
number = int(input("Enter a number: "))

# Calculate the factorial
fact = factorial(number)

# Display the result
print("The factorial of ", number, "is", fact)


"""Ans: Enter a number: 9
The factorial of  9 is 362880"""
