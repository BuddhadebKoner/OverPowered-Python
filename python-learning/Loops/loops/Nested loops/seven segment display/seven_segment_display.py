# Take input the number which you want to show
n = int(input('Enter number between 0 to 9: '))

# Display zero
if n == 0:
    print('You Entered', n)
    width = 4
    height = 6
    i = 0
    while i < height:
        j = 0
        while j < width:
            if (i == 0 or i == height - 1 or j == 0 or j == width - 1):
                print('*', end=' ')
            else:
                print(' ', end=' ')
            j += 1
        print()
        i += 1

# Display one
elif n == 1:
    print('You Entered', n)
    width = 5
    height = 6
    i = 0
    while i < height:
        j = 0
        while j < width:
            if (i == height - 1 or j == 2 or (i == 1 and j == 0) or (i == 0 and j == 1)):
                print('*', end=' ')
            else:
                print(' ', end=' ')
            j += 1
        print()
        i += 1

# Display two
elif n == 2:
    print('You Entered', n)
    width = 4
    height = 5
    i = 0
    while i < height:
        j = 0
        while j < width:
            if (i == 0 or i == 2 or i == (height - 1) or (j == width - 1 and i <= (height / 2)) or (j == 0 and i >= (height / 2))):
                print('*', end=' ')
            else:
                print(' ', end=' ')
            j += 1
        print()
        i += 1

# Display three
elif n == 3:
    print('You Entered', n)
    width = 4
    height = 5
    i = 0
    while i < height:
        j = 0
        while j < width:
            if (i == 0 or i == 2 or i == (height - 1) or j == (width - 1)):
                print('*', end=' ')
            else:
                print(' ', end=' ')
            j += 1
        print()
        i += 1

# Display four
elif n == 4:
    print('You Entered', n)
    width = 4
    height = 5
    i = 0
    while i < height:
        j = 0
        while j < width:
            if (i == ((height - 1) / 2) or j == (width - 1) or (j == 0 and i <= (height / 2))):
                print('*', end=' ')
            else:
                print(' ', end=' ')
            j += 1
        print()
        i += 1

# Display five
elif n == 5:
    print('You Entered', n)
    width = 4
    height = 5
    i = 0
    while i < height:
        j = 0
        while j < width:
            if (i == 0 or i == 2 or i == (height - 1) or (j == 0 and i <= (height / 2)) or (j == (width - 1) and i >= (height / 2))):
                print('*', end=' ')
            else:
                print(' ', end=' ')
            j += 1
        print()
        i += 1

# Display six
elif n == 6:
    print('You Entered', n)
    width = 4
    height = 5
    i = 0
    while i < height:
        j = 0
        while j < width:
            if (j == 0 or i == 0 or i == (height - 1) or i == ((height - 1) / 2) or (j == (width - 1) and i >= (height / 2))):
                print('*', end=' ')
            else:
                print(' ', end=' ')
            j += 1
        print()
        i += 1

# Display seven
elif n == 7:
    print('You Entered', n)
    width = 4
    height = 5
    i = 0
    while i < height:
        j = 0
        while j < width:
            if (i == 0 or i + j == width):
                print('*', end=' ')
            else:
                print(' ', end=' ')
            j += 1
        print()
        i += 1

# Display eight
elif n == 8:
    print('You Entered', n)
    width = 4
    height = 5
    i = 0
    while i < height:
        j = 0
        while j < width:
            if (i == 0 or i == (height - 1) or i == ((height - 1) / 2) or j == (width - 1) or j == 0):
                print('*', end=' ')
            else:
                print(' ', end=' ')
            j += 1
        print()
        i += 1

# Display nine
elif n ==9:
    print('You Entered', n)
    width =4 
    height=5 
    i=0 
    while i<height: 
       j=0 
       while j<width: 
          if(i==0 or i==(height-1)or(i==((height-1)//2))or(j==(width-1))or(j==0 and 
           i<=((height-1)//2))): 
             print("*",end=" ") 
          else: 
             print(" ",end=" ") 
          j=j+1 
       print() 
       i=i+1 

else:
    print('Oops! You entered a wrong digit. Try again.')