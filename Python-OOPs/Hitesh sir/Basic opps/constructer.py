# Car class
class Car:
    # Class attribute
    model = "Royal Enfield" 
    
    # Constructor method (called when an object of the class is created)
    def __init__(self):
        print(self) # self is the new object which is created s1
        print("This is in the init function")

# Creating an object of Car class
s1 = Car()
'''you can see _init_() function is executed just after calling Car()'''

# Dog class
class Dog:
    # Default constructor
    def __init__(self):
        pass
    
    # Parameterized constructor
    def __init__(self, name, age): # commonly we use self, variable name would be anything [self parameter is the reference] 
        self.name = name # assigning name to the instance variable
        self.age = age   # assigning age to the instance variable

# Creating Dog objects
d1 = Dog("Moti", 10)    
d2 = Dog("Tomy", 7)

# Printing attributes of Dog objects
print(d1.name, d1.age, d2.name, d2.age) 
