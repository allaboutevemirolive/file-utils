import os

# Prompt the user for the file name
file_name = "input.txt"

# Open the file and read its contents
with open(file_name, "r", encoding="utf-8") as f:
    text = f.read()

# Replace all the specified symbols with underscores
symbols = "~ ! @ # $ % ^ & * ( ) _ + { } | : \" < > ? - = [ ] \\ ; ' , /"
for symbol in symbols:
    text = text.replace(symbol, " ")

# Save the modified text back to the file
with open(file_name, "w", encoding="utf-8") as f:
    f.write(text)

print("Done!")
