tup = (1,2,3,4,5)

list1 = ['a','b','c','d','e']

newlist =list(zip(tup,list1))
print(newlist)


newtup = tuple(newlist)
# slicing in tuple :
for i, char in newtup:
    print(i,char)

    