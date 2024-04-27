# write a python program to find area and perimeter ofa rectangular

# Get user input for the length and width of the rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate area and perimeter
area = length * width
perimeter = 2 * (length + width)

# Display the area and perimeter
print(f"Area of the rectangle: ",area)
print(f"Perimeter of the rectangle: ",perimeter)
