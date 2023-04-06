import re

def remove_numbers(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
        new_data = re.sub(r'\d+', '', data)
    with open(file_name, 'w') as file:
        file.write(new_data)

remove_numbers('input.txt')
