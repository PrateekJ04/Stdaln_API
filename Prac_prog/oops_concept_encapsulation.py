#4.Encapsulation
#In Encapsulation we hide the internal behavior of the functionality
# and it cannot be called while creating object of class directly
#In order to call this we need to return part of a functionality which can be exposed, using public method

class Try_Encapsulaion():
    __a=""
    def private_method(self):
        rent=10000
        accountBalance=11100
        afterwithdrawn=accountBalance-rent
        self.__a=afterwithdrawn
        return self.__a
    def public_method(self):
        print(f"Balance Amount after rent payment: {Try_Encapsulaion.private_method(self)}")

enc=Try_Encapsulaion()
enc.public_method()

print("=================================================After My Method Execution===================================")

# Methods from other platforms for Encapsulation Understanding

class MyClass:
    def __init__(self):
        self.__private_variable = 42  # Private variable

    @property
    def private_variable(self):
        return self.__private_variable

    @private_variable.setter
    def private_variable(self, value):
        if value >= 0:
            self.__private_variable = value
        else:
            print("Value must be non-negative!")

# Creating an instance of MyClass
obj = MyClass()

# Accessing the private variable via a property (getter)
print(obj.private_variable)  # Output: 42

# Modifying the private variable via a property (setter)
obj.private_variable = 100
print(obj.private_variable)  # Output: 100
