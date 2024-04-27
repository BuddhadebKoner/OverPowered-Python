# Example
# filter (function , sequence)

def is_even(n):
    return n % 2 == 0


even_numbers = filter(is_even, range(1,100))
print(list(even_numbers)) 

# note : do not add or remove elements from the list during iteration
