#2.Python program to check if a given number is an Armstrong number

# Input number from the user
num = int(input("Enter a number: "))

# Convert the number to string to easily iterate over digits
num_str = str(num)

# Calculate the number of digits
num_digits = len(num_str)

# Initialize sum to 0
sum_of_powers = 0

# Iterate over each digit in the number
for digit in num_str:
    # Convert digit back to integer and raise it to the power of num_digits
    sum_of_powers += int(digit) ** num_digits

# Check if the sum of the powers is equal to the original number
if sum_of_powers == num:
    print(num," is an Armstrong number.")
else:
    print(num," is not an Armstrong number.")


"""Ans:Enter a number: 123
123  is not an Armstrong number."""
