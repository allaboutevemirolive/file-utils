import re

inputFile = 'Hard_input.txt'

# your desired output file
outputFile = 'Hard_output.txt'
jsonFile = 'Hard_json.txt'

with open(inputFile, 'r', encoding="utf-8") as f:
    data = f.read()

# find all lines that start with a number followed by a period
matches = re.findall(r'^\d+\. .*', data, re.MULTILINE)

# These characters have special meanings in file systems and 
# cannot be used as part of a filename or folder name.
symbols = '/ \ : * ? " < > | '

# remove symbols from matches
for match in matches:
    for symbol in symbols:
        match = match.replace(symbol, " ")

# create text file for mass file creation
with open(outputFile, 'w', encoding="utf-8") as f:
    for match in matches:
        f.write(match + '\n')

# create json file for vscode user
with open(jsonFile, 'w', encoding="utf-8") as f:
    f.write("{\n")
    f.write('"java.project.sourcePaths": [\n')
    for match in matches:
        f.write("\"" + match + "\",\n")
    f.write("]\n")
    f.write("}")
