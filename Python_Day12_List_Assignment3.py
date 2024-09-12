#3. Write a Python program to find duplicate values from a list and display those

def find_duplicates(items):
    duplicates = []
    seen = set()  # Set to track unique items

    for item in items:
        if item in seen and item not in duplicates:
            duplicates.append(item)  # Add item to duplicates if already seen
        seen.add(item)  # Track the item as seen

    return duplicates

# Example usage
numbers = [10, 20, 30, 40, 10, 50, 30, 60, 70, 20]
duplicates = find_duplicates(numbers)

#Print the Result
print(f"Duplicate values in the list: {duplicates}")


#Ans:Duplicate values in the list: [10, 30, 20]
