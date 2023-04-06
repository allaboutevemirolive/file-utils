with open("2.txt", "r") as file:
    lines = file.readlines()
    cleaned_lines = []
    for i in range(0, len(lines), 2):
        cleaned_line = lines[i].strip() + ". " + lines[i+1].strip()
        cleaned_lines.append(cleaned_line)

with open("3.txt", "w") as file:
    for cleaned_line in cleaned_lines:
        file.write(cleaned_line+'\n')
