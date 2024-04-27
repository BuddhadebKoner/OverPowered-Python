# Create an empty list
my_list = []

# Append an item to the end of the list
my_list.append(5)
print("After appending:", my_list)

# Extend the list by appending elements from another iterable
my_list.extend([6, 7, 8])
print("After extending:", my_list)

# Insert an item at a specified position
my_list.insert(1, 10)  # Two arguments: index and element
print("After inserting:", my_list)

# Remove the first occurrence of an item from the list
my_list.remove(6)  # To remove element 6
print("After removing:", my_list)

# Remove and return the item at the specified position
popped_item = my_list.pop(2)  # One argument: index of the list
# It will return which element was popped

print("Popped item:", popped_item)
print("After popping:", my_list)


# Index of the first occurrence of an item in the list

index = my_list.index(5)
print("Index of 5:", index)


# Clear all items from the list
#my_list.clear()
#print("After clearing:", my_list)

# Count the number of occurrences of an item in the list
if my_list:
    count = my_list.count(5)
    print("Count of 5:", count)
else:
    print("List is empty.")

# Reverse the elements of the list in place
my_list.reverse()
print("After reversing:", my_list)

# Sort the items of the list in place
# Not necessary it will always be numbers
my_list = [3, 1, 4, 1, 5, 9, 2]  # Should be strings
my_list.sort()  # Sorts in ascending order
print("After ascending sorting:", my_list)
my_list.sort(reverse=True)  # Sorts in descending order
print("After descending sorting:", my_list)

# Shallow copy of the list
copied_list = my_list.copy()
print("Copied list:", copied_list)

