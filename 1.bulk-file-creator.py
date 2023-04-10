import os

# Change the working directory to the directory containing the script
# assuming that the input file is located in the same directory as the script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Specify the relative path to the input file
inputFile = 'Hard_output.txt'

# Construct the full path to the input file
inputFilePath = os.path.join(os.getcwd(), inputFile)

# Open the file in read mode
with open(inputFilePath, 'r') as file:
    # Read the contents of the file into a list
    folder_names = file.readlines()

# Strip the newline character from the end of each name
folder_names = [name.strip() for name in folder_names]

# Create the specified folders
for folder_name in folder_names:
    os.makedirs(folder_name)
