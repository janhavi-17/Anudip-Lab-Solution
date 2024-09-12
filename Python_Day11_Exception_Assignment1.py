#1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

def divide_numbers(a, b):
#Handling a Exception
    try:
        result = a / b
        print(f"The result of {a} divided by {b} is: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# Example usage
num1 = float(input("Enter the numerator: "))
num2 = float(input("Enter the denominator: "))

#Result
divide_numbers(num1, num2)


"""Ans: Enter the numerator: 4
Enter the denominator: 0
Error: Division by zero is not allowed."""
