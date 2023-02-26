file = open("Medium_output.txt", "r")
lines = file.readlines()
file.close()

file = open("Medium_output.txt", "w")

for line in lines:
    line = line.strip()
    file.write("\"" + line + "\",\n")

file.close()
