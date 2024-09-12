#2. Write a Python program to remove duplicate characters of a given string.
#Input = “String and String Function” Output: String and Function


# Input string
Input = "String and String Function"

# Split the string into words
words = Input.split()

# Use a set to track seen words and a list to store unique words
seen_words = set()
unique_words = []

# Iterate through each word in the list
for word in words:

# Add the word to the unique_words list if it hasn't been seen before
    if word not in seen_words:
        unique_words.append(word)
        seen_words.add(word)

# Join the unique words back into a string
output_string = ' '.join(unique_words)

# Print the result
print("Output is: ",output_string)

#Output is:  String and Function

