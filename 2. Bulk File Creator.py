import os

inputFile = 'Easy_input.txt'

# Open the file in read mode
with open(inputFile, 'r') as file:
    # Read the contents of the file into a list
    folder_names = file.readlines()

# Strip the newline character from the end of each name
folder_names = [name.strip() for name in folder_names]

for folder_name in folder_names:
    os.makedirs(folder_name)
