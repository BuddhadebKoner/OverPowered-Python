"""
when one class (child/derive) derives the property & methods of another class (parent/base)
"""


# define a superclass
class super_class:
    pass
    # attributes and method definition


# inheritance
class sub_class(super_class):
    pass
    # attributes and method of super_class
    # attributes and method of sub_class


# example -- >
class Person:
    def __init__(self, fame, name):
        self.firstname = fame
        self.lastname = name

    def printname(self):  # this is the syntax to inherit the
        print(self.firstname, self.lastname)


# Use the Person class to create an object, and then execute the printname method:

x = Person("ms", "dhoni")
x.printname()


# Create a class named Student, which will inherit the properties and methods from the Person class:
class Student(Person):  # child class (parents class)
    pass


# Use the Student class to create an object, and then execute the printname method:
x = Student("virat", "koholi")
x.printname()
