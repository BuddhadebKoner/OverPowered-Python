# Define strings with different quotation styles
str1 = "this is a string " 
str2 = 'buddhadeb koner'
str3 = """this is tripple cotation string"""

# Escaping sequence using \n
print("hello guys \nhow are you")

# Concatenation of strings
print(str1 + str2)

# Length of a string
print(len(str3))
str4 = str1 + " " + str2  # Including space 
print(len(str4))

# String indexing - starts from 0
ch = str1[0]
print(ch)

# Slicing of a string
print(str1[1:4])  # Output: his

# Negative indexing
str5 = "Apple"
print(str5[-5:-2])  # Output: App


# Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print("Concatenation:", result)  # Output: Hello World

# Length
my_string = "Hello World"
length = len(my_string)
print("Length:", length)  # Output: 11

# Accessing Characters
first_char = my_string[0]
substring = my_string[3:7]
print("First Character:", first_char)  # Output: H
print("Substring:", substring)   # Output: lo W

# Splitting
words = my_string.split()
print("Splitting:", words)     # Output: ['Hello', 'World']

# Joining
my_string = ' '.join(words)
print("Joining:", my_string)  # Output: Hello World

# Case Conversion
my_string = "hello world"
upper_case = my_string.upper()
lower_case = my_string.lower()
capitalized = my_string.capitalize()
title_case = my_string.title()
print("Upper Case:", upper_case)              # Output: HELLO WORLD
print("Lower Case:", lower_case)              # Output: hello world
print("Capitalized:", capitalized)             # Output: Hello world
print("Title Case:", title_case)              # Output: Hello World

# Replacement
new_string = my_string.replace("world", "Python")
print("Replacement:", new_string)                  # Output: hello Python

# Checking Substring
substring_check = "Hello" in my_string
print("Substring Check:", substring_check)        # Output: True


