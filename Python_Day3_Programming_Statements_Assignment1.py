#1.Using input() function take one number from the user and using ternary operators check whether the number is even or odd

#Taking input from the user
num = int(input("Enter the Number: "))

#Checking if the number is even or odd using a ternary operator
result = "Even" if num % 2 == 0 else "Odd"

#Print the Result
print("The Given number is:", result)

"""#Ans: Enter the Number: 7
The Given number is: Odd"""
