import math

# user input ---
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

d =b**2 - 4*a*c

# formula --- 
root1 = (-b + math.sqrt(d)) / (2*a)
root2 = (-b - math.sqrt(d)) / (2*a)

# Display the roots
print("1st root -- :", round(root1,2))
print("2nd root -- :", round(root2,2))
