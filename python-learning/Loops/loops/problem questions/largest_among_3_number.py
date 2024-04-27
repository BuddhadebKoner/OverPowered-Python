a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
c = int(input('Enter 3rd number: '))

if a > b:
    if a > c:
        print('largest is ',a)
    else:
        print('largest is ',c)
else:
    if b > c:
        print('largest is ',b)
    else:
        print('largest is ',c)


