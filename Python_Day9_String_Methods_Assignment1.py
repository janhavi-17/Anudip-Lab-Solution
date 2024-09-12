#1. Write a Python program to Count all letters, digits, and special symbols from the given string
#Input = “P@#yn26at^&i5ve” Output: Chars = 8 Digits = 2 Symbol = 3

# Input string
Input= "P@#yn26at^&i5ve"

# Initialize counters
chars_count = 0
digits_count = 0
symbols_count = 0

# Iterate through each character in the string
for char in Input:
    if char.isalpha():
        chars_count += 1
    elif char.isdigit():
        digits_count += 1
    else:
        symbols_count += 1

# Print the results
print(f"Chars = {chars_count}")
print(f"Digits = {digits_count}")
print(f"Symbols = {symbols_count}")


"""Ans: Chars = 8
Digits = 3
Symbols = 4"""
