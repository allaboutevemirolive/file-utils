import re

# Open the input file for reading
with open('Easy_input.txt', 'r') as f:
    # Read the entire contents of the file into a string
    data = f.read()

# Use regular expressions to find all lines that start with a number followed by a period
matches = re.findall(r'^\d+\. .*', data, re.MULTILINE)

# Open the output file for writing
with open('Easy_output.txt', 'w') as f:
    # Write the filtered lines to the output file
    for match in matches:
        f.write(match + '\n')
