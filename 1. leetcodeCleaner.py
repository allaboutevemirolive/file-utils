import re

inputFile = 'Hard_input.txt'
outputFile = 'Hard_output.txt'

with open(inputFile, 'r', encoding="utf-8") as f:
    data = f.read()

# find all lines that start with a number followed by a period
matches = re.findall(r'^\d+\. .*', data, re.MULTILINE)

# These characters have special meanings in file systems and 
# cannot be used as part of a filename or folder name.
symbols = '/ \ : * ? " < > | '

for match in matches:
    for symbol in symbols:
        match = match.replace(symbol, " ")

with open(outputFile, 'w', encoding="utf-8") as f:
    for match in matches:
        f.write(match + '\n')
