# 1. Write a Python program to count the occurrences of each word in a given sentence 
#string = “To change the overall look of your document. To change the look available in the gallery” 

# Define the input string
string = "To change the overall look of your document. To change the look available in the gallery"

# Convert the string to lowercase and split it into words
words = string.lower().split()

# Create a dictionary to store word counts
word_count = {}

# Iterate through the words and count their occurrences
for word in words:
    # Remove punctuation from each word
    word = word.strip('.,!?')
    # Update the word count in the dictionary
    word_count[word] = word_count.get(word, 0) + 1

# Print the word counts
for word, count in word_count.items():
    print(word,count)

"""Ans: to 2
change 2
the 3
overall 1
look 2
of 1
your 1
document 1
available 1
in 1
gallery 1"""

