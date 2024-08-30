#1.Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd.

#Taking input from User
num = int(input("Enter a Number:"))

#Checking Number is Even or Odd
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

"""#Ans:Enter a Number:88
88 is Even"""
