#1. Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.

#Declaring a Function
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())  # strip() removes any leading/trailing whitespace including newline characters
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
read_file("ABC.txt")


#Ans: Hey! There is Begining of New Era
