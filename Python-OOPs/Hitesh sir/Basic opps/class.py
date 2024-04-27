# A class is a blueprint for creating objects.

class Student:  # Class names should typically use CamelCase convention.
    name = "Buddhadeb"  # It's good practice to capitalize constants.

# Creating an object (instance).
s1 = Student()  # Here s1 is an object variable.
print(s1)  # This will print the object's memory address.

print(s1.name)  # Accessing the 'name' attribute of the object.
print(s1.name)  # Accessing again, demonstrating the same value for every object.

# Example:
class Car:
    model = "Royal Enfield" 
    color = "Onyx Black"
    price = 200000

car1 = Car()
# Printing car attributes.
print(car1.color, car1.model, car1.price) 
