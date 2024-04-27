class Parent:
    def __init__(self):
        print("Parent class constructor")

    @staticmethod
    def parent_method():
        print("Parent method")


class Child(Parent):
    def __init__(self):
        super().__init__()  # Calling the constructor of the superclass/ parent class
        print("Child class constructor")

    def child_method(self):
        super().parent_method()  # Calling the method of the superclass
        print("Child method")


# Creating an instance of the Child class
child_instance = Child()

# Calling methods of the Child class
child_instance.child_method()

"""
We have two classes, Parent and Child, where Child inherits from Parent.

In the Child class's __init__ method, we call super().__init__() 
to call the constructor of the superclass (Parent),
which prints "Parent class constructor".

Similarly, in the child_method of the Child class,
we call super().parent_method() to call the parent_method of the superclass (Parent),
 which prints "Parent method".

This way, super() allows us to access and utilize methods 
and properties of the superclass in the subclass,
facilitating code reuse and maintaining the inheritance hierarchy.
"""
