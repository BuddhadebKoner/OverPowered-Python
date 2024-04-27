# find area of a scalene triangle


import math
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

#semi-perimeter
s = (a + b + c) / 2
# formula -----
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

area = round(area, 2)

# Display the area
print("Area of the scalene triangle: ",area)
