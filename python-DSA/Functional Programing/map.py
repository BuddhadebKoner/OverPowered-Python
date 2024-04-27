# Example

# map (function, sequence)


def square(n):
    return n ** 2

squared_numbers = map(square, range(1,50))
print(list(squared_numbers)) 


# more than one sequence 

list1 = [1,2,3,4,5]
list2 = [5,4,3,2,1]

def sum(x,y):
    return x+y

Totalsum = map(sum,list1,list2) # two sequence

print(list(Totalsum))