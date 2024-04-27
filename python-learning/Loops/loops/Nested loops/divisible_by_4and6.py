a = int(input('Enter first range'))
b = int(input('Enter secound range'))

print('Divisible by 4 and 6 between the given range')
while (a<=b):
    if a%4 == 0 and a%6 == 0:
        print(a)
    a+=1
