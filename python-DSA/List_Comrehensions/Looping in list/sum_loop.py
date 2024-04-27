# WRITE  a program to find the sum and mean of element in a list

num_list = [1,2,3,4,5,6,7,8,9,10]

sum = 0
for i in num_list:
    sum += i
print("Sumof all number in list is : ",sum)
print("Avarage of elements in the list : ", float(sum/float(len(num_list))))




# Using the enumerate() function , 
# this is used you want to point both index as well as item in the list. the Enumerate() will return the an enumerate object which is containts the index and value of the items list as a tuple


for index ,i in enumerate(num_list):
    print(i," is in index number ",index)



