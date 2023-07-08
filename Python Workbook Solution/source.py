filename = input("Enter the file name: ")
# Open the file and read its contents
try:
    with open(filename, "r") as file:
        contents = file.read()
except IOError:
    print("Could not open file")
    exit()

# Split the contents into words
words = contents.split()

# Find the length of the longest word
max_length = max(len(word) for word in words)

# Find all the words with the longest length
longest_words = [word for word in words if len(word) == max_length]

# Output the results
if len(longest_words) == 1:
    print(f"The longest word in the file is {longest_words[0]} with length {max_length}.")
else:
    print(f"There are {len(longest_words)} words with length {max_length}:")
    for word in longest_words:
        print(word)