#1.Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.

#Declaring the Function with two parameters
def div(x,y):

# Check if the divisor is not zero to avoid division by zero error
    if y == 0:
        return "Division by zero is not allowed."
    return x / y

    
# Call the function and pass two numbers
result = div(20,10)

#Diplaying the Result
print("Division is:",result)


#Ans:Division is: 2.0
