# List comprehensions can be used to extract specific information from complex data structures, such as lists of dictionaries:

# Example: Extract names from a list of dictionaries
people = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
names = [person['name'] for person in people]
print(names)

