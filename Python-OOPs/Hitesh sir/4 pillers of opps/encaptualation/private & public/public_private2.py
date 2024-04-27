class Person:

    @staticmethod
    def __hello():  # this is the private  methods
        print("Hello user")

    def welcome(self):  # this is private methods
        self.__hello()


p1 = Person()
p1.welcome()  # indirectly access the private method
