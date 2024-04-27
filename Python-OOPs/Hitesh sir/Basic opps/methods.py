'''
In a class, all functions are called methods.
'''


# NORMAL METHODS --->

class Methods:
    def __init__(self, value):  # class constructor method
        print("In class Methods...")
        self.value = value
        print("The value is:", self.value)

    def welcome(self):  # this is object-level method, that's why it has a self parameter
        print('Welcome here')


obj1 = Methods(10)
obj1.welcome()

'''
Create a Student class that takes name & marks of 3 subjects as arguments in the constructor, then create a method to print the average.
'''


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        total = sum(self.marks)
        num_subjects = len(self.marks)
        print("Hi", self.name, "Your Average is:", total / num_subjects)


s1 = Student("Tony Stark", [99, 76, 54, 100])
s1.get_avg()

s1.name = "Iron Man"  # You can change the value of attributes
s1.get_avg()

# STATIC METHODS -->

'''
Methods Are dont use self parameter(work at class lavel not obj lavel) 
'''


class Car:

    @staticmethod  # decorator which is convert to a static methods
    # "decorator" allow to wrap another function in order to extend the behaviour of warped function ,
    # without permanently modifying it
    def print_hello():
        print("hello")

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
