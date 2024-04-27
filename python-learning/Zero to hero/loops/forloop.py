# Loops in Python
# Loops are control structures that iterate over a sequence of elements until a certain condition is met.

# for Loop:
# The for loop in Python iterates over a sequence of items, such as a list, tuple, string, or range. It follows sequential traversal, meaning it processes each element in the sequence in order.

# Syntax:
# for variable in sequence:
#     # code block to be executed

# Example:
Mytuple = (1, 3, 5, 6, 8, 9, 10)

# Iterating over the tuple, linier search
for el in Mytuple:  # 'el' is the loop variable that takes each element of 'Mytuple' in each iteration
    if el == 10:
        print('10 is present in the tuple')
        break  # Exit the loop once the condition is met

# Explanation:
# - The loop iterates over each element of the tuple 'Mytuple'.
# - In each iteration, the current element is assigned to the loop variable 'el'.
# - The if statement checks if the current element 'el' is equal to 10.
# - If the condition is met, it prints a message indicating that 10 is present in the tuple.
# - The 'break' statement is used to exit the loop immediately once the condition is satisfied.
# - Without the 'break', the loop would continue iterating over the remaining elements of the tuple, which is unnecessary once the target element is found.

# pass statement
for i in range(10):
    #empty placeholder for future code
    pass

