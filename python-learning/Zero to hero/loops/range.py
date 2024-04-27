#range is a function that is return squencial numbers
myrange = range(10) # range(10) that mean range(stop) stop at 9th index because ,
# starting is by default 0

print(type(myrange)) # <class 'range'>

# catch the range values :
for i in myrange:
    print(i)
# 2 argument in the range function
for i in range(3,10): # range(start,stop)
    print(i)
    
# 3 argument in the range function
for i in range(0,100,10): # range(start,stop,step)
    # by default step is 1
    print(i)


