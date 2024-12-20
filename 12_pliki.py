# with open('files\\U2.txt', 'r') as my_file:
#     content = my_file.read()
# print(content)
#
# with open('files\\logs.txt', 'w') as my_file2:
#     my_file2.write('Kamil')

with open('files\\rozliczenie.csv') as my_file3:
    content = my_file3.readlines()
    print(content)

for i in range (len(content)):
    content[i] = content[i].split(';')

print(content[4][2])
