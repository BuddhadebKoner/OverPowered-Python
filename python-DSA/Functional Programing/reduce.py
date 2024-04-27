from functools import reduce
# reduce (function , sequence)

numbers = [1, 2, 3, 4, 5, 6]

def multiply(x, y):
    return x * y

product = reduce(multiply, numbers)
print(product)
