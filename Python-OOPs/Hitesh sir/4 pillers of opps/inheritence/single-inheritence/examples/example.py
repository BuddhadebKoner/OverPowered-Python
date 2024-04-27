class Dog:  # parent
    # attribute and method of the parent class
    @staticmethod
    def bark():
        print("I can bark")

    @staticmethod
    def eat():
        print("I can eat")


class Animal(Dog):  # child
    def __init__(self, name):
        self.name = name


dog1 = Animal("Tomy")
dog2 = Animal("Mote")

print(dog1.name,dog2.name)  # no doughty it will work
print(dog1.bark())  # it will also work
print(dog2.eat())
