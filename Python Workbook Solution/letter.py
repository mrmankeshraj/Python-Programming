import sys
letters = []

if len(sys.argv) != 2:
    print("You should enter one file name to be read: ")
    quit()

try:
    with open(sys.argv[1], "r") as file:
        words = file.read().split()
        letters = [letter.lower() for word in words for letter in word if letter.isalpha()]
except IOError:
    print("Could not open file")
    exit()

com_char = {}
for letter in letters:
    if letter in com_char:
        com_char[letter] += 1
    else:
        com_char[letter] = 1

for key, value in com_char.items():
    print(f"{key}: {value}")