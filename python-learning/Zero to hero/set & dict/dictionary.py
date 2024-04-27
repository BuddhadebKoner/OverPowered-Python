myDict = {
    'name': 'Buddhadeb',
    'age': 30,
    'city': 'New York',
    'subjects': ("python", "c++")  # Changed list to tuple
}
# Dictionary is mutable
myDict['age'] = 23

print(myDict)

nullDict = {}    # Changed Nulldec to nullDict and corrected spelling
print(nullDict)  # null dictionary

# Nested dictionary ->
student = {
    'name': 'rahul',
    'roll': 69,
    'Marks': {    # Inner dictionary
        'phy': 97,
        'math': 20,
        'c++': 100
    }
}

print(student['Marks'])

# Dictionary Methods -->
print(student.keys())
print(list(student.keys()))  # Type casting list

# To find the total number of keys
print(len(student))

# Value methods
print(list(student.values()))

# Item methods
print(list(student.items()))
# It will return items in tuple format

pairs = list(student.items())
print(pairs[1])

# Get methods -->
print(myDict['name'])  # Normal life
# If wrong key return error
print(myDict.get('name2'))  # Mentos life
# Return None

# Update methods -->
newDict = {
    'city' : 'bardhaman',
    'age': 20 # here age is already have in the dicionary so this will be overwrite not create new key .
}
student.update(newDict)
print(student)
