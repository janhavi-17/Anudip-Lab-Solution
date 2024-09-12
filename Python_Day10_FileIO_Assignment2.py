#2. Write a function in Python to count and display the total number of words in a text file “ABC.txt”

#Declaring Function
def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            total_words = len(words)
            print(f"Total number of words in {filename}: {total_words}")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
count_words_in_file("ABC.txt")

#Ans: Total number of words in ABC.txt: 7
