print("example 1")


class Manager:
    @staticmethod
    def final_review():
        print("Final Review")


class Reviewer(Manager):
    @staticmethod
    def review():
        print("Reviewing...")


class Writer(Reviewer):
    @staticmethod
    def writes():
        print("Writes the code\n")


o = Writer()
o.final_review()
o.review()
o.writes()


print("example 2")


class Person:
    def __init__(self):
        print('Person - Hii')

    def age(self, a):
        print('Printing the age: ', a)


class Father(Person):
    def __init__(self):
        print('Father - Hii')
        super().__init__()

    def age(self, a):
        print('Printing the age(Father): ', a)
        super().age(a - 1)


class Mother:
    pass


class Mother(Father):
    def __init__(self):
        print('Mother - Hii')
        super().__init__()

    def age(self, a):
        print('Printing the age(Mother): ', a)
        super().age(a + 5)


o = Mother()
o.age(30)
