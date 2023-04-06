
# Prompt the user for the file name
file_name = "Easy_output.txt"

# Open the file and read its contents
with open(file_name, "r", encoding="utf-8") as f:
    text = f.read()

# Replace all the specified symbols with underscores
# symbols = "~ ! @ # $ % ^ & * ( ) _ + { } | : \" < > ? - = [ ] \\ ; ' , /"
symbols = '/ \ : * ? " < > | '
# These characters have special meanings in file systems and cannot be used as part of a filename or folder name.
# symbols = "~ ! @ # $ % ^ & * ( ) + { } | : \" < > ? = [ ] \\ ; ' , /"
for symbol in symbols:
    text = text.replace(symbol, " ")

# Save the modified text back to the file
with open('Easy_output_symbols_Removed.txt', "w", encoding="utf-8") as f:
    f.write(text)
