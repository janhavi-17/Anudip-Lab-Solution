#5.Write a Python program that determines the largest of three numbers entered by the user.

# Get three numbers from the user
num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))
num_3 = float(input("Enter the third number: "))

# Determine the largest number using if-else statements
if num_1 >= num_2 and num_1 >= num_3:
    largest = num_1
elif num_2 >= num_1 and num_2 >= num_3:
    largest = num_2
else:
    largest = num_3

# Print the largest number
print("The largest number is: ", largest)

"""#Enter the first number: 10
Enter the second number: 90
Enter the third number: 81.60
The largest number is:  90.0"""
