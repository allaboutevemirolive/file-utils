import re

inputFile = 'Hard_input.txt'
outputFile = 'Hard_output.txt'
jsonFile = 'Hard_json.txt'

with open(inputFile, 'r', encoding="utf-8") as f:
    data = f.read()

# find all lines that start with a number followed by a period
matches = re.findall(r'^(\d+)\. (.*)', data, re.MULTILINE)

# create text file for mass file creation
with open(outputFile, 'w', encoding="utf-8") as f:
    for match in matches:
        # format the number with leading zeros
        file_number = match[0].zfill(4)
        # replace spaces with hyphens and make everything lowercase
        file_name = match[1].replace(' ', '-').lower()
        # write the formatted output to file
        f.write(f"{file_number}.{file_name}\n")

# create json file for vscode user
with open(jsonFile, 'w', encoding="utf-8") as f:
    f.write("{\n")
    f.write('"java.project.sourcePaths": [\n')
    for match in matches:
        file_number = match[0].zfill(4)
        file_name = match[1].replace(' ', '-').lower()
        f.write(f"\"{file_number}.{file_name}\",\n")
    f.write("]\n")
    f.write("}")
