''''
a = 5

forA = ord('A')
while (forA<=ord('E')):
    j=0
    while(j<a):
        print(chr(forA),end=' ')
        j+=1
    forA+=1
    print()
'''     

a = int(input("Enter the number"))
i = 1
p = 65


while (i<=a):
    j=1
    while(j<a):
        print(chr(p),end='')
        j+=1
    i+=1
    p+=1
    print()