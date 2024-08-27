#2.Using input function take two number and then swap the number

#Taking Two numbers from the User
num_1 = int(input("Enter 1st Number: "))
num_2 = int(input("Enter 2nd Number: "))

#Swaping the numbers
num_1, num_2 = num_2, num_1

#Print the Swaped Values
print("After Swapping: ", num_1, num_2)

"""#Ans: Enter 1st Number: 45
Enter 2nd Number: 34
After Swapping:  34 45"""
