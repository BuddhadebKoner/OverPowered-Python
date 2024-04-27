Student = {1, 2, 2, "hello", "world", "hello"}

# Set is mutable 
# But the elements are unique & immutable
# So we can pass tuple in the set but not list or dictionary

print(Student)  # Ignore all duplicate values
# There don't have any key concept
print(type(Student))

# Create an empty set -->

# If you write like this 
myset = {}
print(type(myset))  # It is a dictionary not set

mynewset = set()  # Important syntax
print(type(mynewset))  # Now this is a set

# Some popular methods -->

collection = set()

collection.add(5)
collection.add(5)  # It will ignore
collection.add(10)
print(collection)

collection.remove(5)
print(collection)  # Have single value only

# To empty a set 

collection.clear()
print(collection)

# Pop --> 

subjects = {"c++", "java", "php", "javascript"}

# It will pop random element from the set
print(subjects.pop())
print(subjects.pop())

# Union & intersection methods [same like in mathematics]

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))  # It will return new set 
print(set1.intersection(set2))  # Common elements

