# Combining and pairing elements of two lists using list comprehension 

# The basic syntax of list comprehension in Python is:

# [expression for item in iterable if condition]

# expression: The expression to be evaluated and included in the resulting list.

# item: Variable representing each element in the iterable.

# iterable: The iterable object (e.g., list, tuple, string) that is being iterated over.

# condition (optional): A condition that filters elements from the iterable.
# Only elements for which the condition evaluates to True are included in the resulting list.

print([(x,y) for x in [10,20,30] for y in [30,10,40] if x != y])


# Explanation:

# Basic List Comprehension: The first example demonstrates generating a list of squares of numbers 1 to 5 using a simple expression x**2 inside the list comprehension.
# List Comprehension with Condition: In the second example, a condition if x % 2 == 0 is used to filter out only the even numbers from 1 to 10.