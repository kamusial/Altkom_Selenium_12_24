with open('files\\U2.txt', 'r') as my_file:
    content = my_file.read()
print(content)

with open('files\\logs.txt', 'w') as my_file2:
    my_file2.write('Kamil')