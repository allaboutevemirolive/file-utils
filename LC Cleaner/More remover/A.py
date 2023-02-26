import re

# Open the txt file and read the contents
with open("input.txt", "r") as f:
    data = f.read()

# Use regular expressions to replace the unwanted characters
data = re.sub("\t[\d]+\.[\d]+%\t(Easy|Medium|Hard)\t", "", data)

# Write the cleaned data back to the txt file
with open("1.txt", "w") as f:
    f.write(data)
