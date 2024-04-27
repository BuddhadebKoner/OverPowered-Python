"""
public methods
"""


# first account
class Account1:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.acc_pass = acc_pass


s1 = Account1("1234", "xyz@123")

print(s1.acc_no, s1.acc_pass)  # in this case account password is the sensitive things so , out of the scope I don't
# need this value 's1.acc_pass'

"""
private Methods
"""


class Account2:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass  # Private variable with double underscore prefix
        print("Account Number is :", self.acc_no, "password is :", self.__acc_pass)


s2 = Account2("1234", "xyz@123")

# print("Account Number is :", s2.acc_no, "password is inaccessible:", s2.__acc_pass)  # This will raise an
# AttributeError

"""
another use case
"""


class Example:
    def __init__(self):
        self.public_variable = 42
        self.__private_variable = "secret"

    def get_private_variable(self):
        return self.__private_variable


obj = Example()

print("Public variable:", obj.public_variable)
# Attempting to access private variable directly would raise an AttributeError
# print("Private variable:", obj.__private_variable)

# Accessing private variable through a public method
print("Private variable:", obj.get_private_variable())


"""
Last one  use case 
"""


class Car:
    def __init__(self, make, model, year, mileage):
        self.make = make                   # Public attribute
        self.model = model                 # Public attribute
        self.year = year                   # Public attribute
        self.__mileage = mileage           # Private attribute

    def get_mileage(self):
        return self.__mileage            # Public method to access private attribute

    def __update_mileage(self, new_mileage):
        self.__mileage = new_mileage    # Private method to update mileage

    def drive(self, miles):
        self.__update_mileage(self.__mileage + miles)
        print(f"Driving {miles} miles. Total mileage: {self.__mileage}")


car1 = Car("Toyota", "Camry", 2020, 10000)

print(f"Car: {car1.make} {car1.model} {car1.year}")
print(f"Initial mileage: {car1.get_mileage()} miles")

# Attempting to access private attribute directly
# This would raise an AttributeError
# print(car1.__mileage)

# Driving the car and updating mileage
car1.drive(200)
car1.drive(300)
