
a = int(input('Enter the number: '))

i = 1

while i <= a:
    if a % i == 0:
        print(i, end=' ')
    i += 1
