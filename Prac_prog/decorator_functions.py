#Use decorator to call a function
""""""


def my_decorator(func):
    def inner_function():
        print("Before: I am inside inner_function")
        func()
        print("After: This program is executed")
    return inner_function


@my_decorator
def outer_function():
    print("In Between Function Call: I am inside Outer Function")

outer_function()

