a =int(input('Enter 1st number'))
b =int(input('Enter 2nd number'))
c =int(input('Enter 3st number'))

if a>b and b>c:
    print('smal number is',c)
elif b>a and c>a:
    print('small number is',a)
else:
    print('small number is',b)
