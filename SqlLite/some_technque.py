# multiple way to write and read file using different syntax

file = open('SqlLite/youtube1.txt', 'w')

try:
    file.write('This is file number 1')
finally:
    file.close()

with open('SqlLite/youtube2.txt', 'w') as file:
    file.write('This is file number 2')


# error handeling 
