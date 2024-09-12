#2. Write a Python program to get the largest and smallest number from a list without builtin functions. 

def find_largest_and_smallest(numbers):
    # Initialize both to the first element in the list
    largest = smallest = numbers[0]
    
    # Iterate through the list to find the largest and smallest
    for number in numbers[1:]:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number
    
    return largest, smallest

# Example usage
numbers = [10, 45, 2, 78, 34, 9, 88, 4]
largest, smallest = find_largest_and_smallest(numbers)

#Print the Result
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")


"""Ans:Largest number: 88
Smallest number: 2"""
