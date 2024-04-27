# Define individual variables for marks
marks1 = 94.7
marks2 = 76.2
marks3 = 82.9
marks4 = 56.1

# Consolidate marks into a list
marks = [94.7, 76.2, 82.9, 56.1]        # List of marks
# Print the list of marks
print("List of marks:", marks)
# Print the type of marks
print("Type of marks:", type(marks))        # Print the type of marks (list)

# Define list for student details
student = ["buddhadeb", 10, 17, "westbengal"]           # List containing student details 
# Print the list of student details
print("Student details:", student)

# Here you can see a difference between string and list
# In Python, strings are immutable, so you cannot directly modify individual characters
# str = 'hello'
# str[4] = 'y'  # This is not possible
# But in lists, you can modify individual elements

# Update the first element of the student list

student[0] = "jeet"                              # Update the first element of the student list to "jeet"
print("Updated student details:", student)       # Print the updated student details

# Here string slicing is possible
print("Sliced marks:", marks[1:4])                   # Print a slice of the marks list
# Lists also support slicing and negative indexing
