
# List comprehensions are excellent for filtering data based on specific criteria. For instance: 
# Example: Filter out negative numbers from a list
numbers = [1, -2, 3, -4, 5]
positive_numbers = [x for x in numbers if x >= 0]
print(positive_numbers)  