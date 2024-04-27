# While Loop:
# The while loop in Python is used to repeatedly execute a block of code as long as a specified condition is true. It follows conditional traversal methods, meaning it continues iterating until the specified condition evaluates to False.

# Syntax:
# while condition:
#     # code block to be executed

# Example:
count = 0  # Variable 'count' is the iterator, which controls the iteration process
while count < 10:
    print('This is a loop')
    count += 1  # Incrementing the count by 1 in each iteration

# Explanation:

# - The while loop checks the condition 'count < 10' before each iteration.

# - If the condition is true, the code block inside the loop is executed.

# - In this example, 'count' starts from 0 and increments by 1 in each iteration.

# - The loop continues until 'count' becomes equal to or greater than 10.

# - Once the condition becomes false, the loop terminates, and the program moves to the next statement after the loop.

# Note:
# - Be cautious while using a while loop to avoid infinite loops where the condition never becomes false. Infinite loops can lead to program freezing or crashing.

# - It's essential to ensure that the condition in a while loop eventually becomes false to prevent infinite looping.

# - The loop variable (in this case, 'count') is often used to control the number of iterations and is typically incremented or decremented within the loop block.

# - Each cycle of execution in the loop, where the condition is evaluated and the code block is executed, is termed as an iteration.

# - It's a good practice to initialize the loop variable before entering the while loop to ensure predictable behavior.

