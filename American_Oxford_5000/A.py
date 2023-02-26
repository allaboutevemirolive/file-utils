import re

# Open the file
with open('high_frequency_words.txt', 'r') as f:
    text = f.read()

# Split the text by newline character
lines = text.split("\n")

# Iterate through the lines and remove everything after the first word
cleaned_lines = []
for line in lines:
    cleaned_line = line.split(" ")[0]
    cleaned_lines.append(cleaned_line)

# Join the cleaned lines with newline character
cleaned_text = "\n".join(cleaned_lines)

# Write the cleaned text to a new file
with open('cleaned_high_frequency_words.txt', 'w') as f:
    f.write(cleaned_text)
