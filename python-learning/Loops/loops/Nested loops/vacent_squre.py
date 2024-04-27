a = int(input('Enter the side of squre'))

i=0
while(i<a):
    j=0
    while(j<a):
        if i==0 or j==0 or i==(a-1) or j==(a-1):
            print('* ',end='')
        else:
            print('  ',end='')
        j+=1
    print()
    i+=1
        
