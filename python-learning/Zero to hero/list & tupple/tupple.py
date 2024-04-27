# Create a tuple
my_tuple = (1, 2, 3, 4, 5)
print(type(my_tuple))

# Access an element by index
element = my_tuple[2]
print("Element at index 2:", element)

# Slice the tuple
sliced_tuple = my_tuple[1:4]
print("Sliced tuple:", sliced_tuple)

# Get the length of the tuple
length = len(my_tuple)
print("Length of the tuple:", length)

# Check if an element is present in the tuple
is_present = 5 in my_tuple
print("Is 5 present in the tuple:", is_present)

# Concatenate two tuples
concatenated_tuple = my_tuple + (6, 7, 8)
print("Concatenated tuple:", concatenated_tuple)

# Count the number of occurrences of an item in the tuple
count = my_tuple.count(5)
print("Count of 5:", count)

# Index of the first occurrence of an item in the tuple
try:
    index = my_tuple.index(5)
    print("Index of 5:", index)
except ValueError:
    print("Item 5 not found in the tuple.")

# Shallow copy of the tuple
copied_tuple = my_tuple[:]
print("Copied tuple:", copied_tuple)
