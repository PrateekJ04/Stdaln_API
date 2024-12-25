# 3.Polymorphism

# In Python method overloading is not directly allowed
# Method overriding is done and child class prefers its own method declared
# and for accessing parent method via inheriting then we need to use super() keyword
class One():
    def sum_of_numbers(self, a=10, b=20, c=40):
        return print(a + b + c)


class Two(One):
    def sum_of_numbers(self, a=70, b=80, c=10, d=5):
        super().sum_of_numbers(10,20,50)
        return print(a + b + c + d)


obj = Two()
# Here method in class Two overrides the method in class One and provides the output in Class Two method
obj.sum_of_numbers()
