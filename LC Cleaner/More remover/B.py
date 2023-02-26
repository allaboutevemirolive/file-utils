with open("1.txt", "r") as file:
    lines = file.readlines()
    cleaned_lines = []
    for line in lines:
        if "%" not in line:
            cleaned_lines.append(line)

with open("2.txt", "w") as file:
    for cleaned_line in cleaned_lines:
        file.write(cleaned_line)
