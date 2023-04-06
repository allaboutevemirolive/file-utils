with open("Medium_output.txt", "r") as file:
    data = file.read()
    ''''
    f'"1. Easy/{line}
    f'"2. Medium/{line}
    f'"3. Hard/{line}
    '''
    formatted_data = [f'"2. Medium/{line}"' for line in data.split("\n")]

with open("new_file.txt", "w") as new_file:
    new_file.write(",\n".join(formatted_data))