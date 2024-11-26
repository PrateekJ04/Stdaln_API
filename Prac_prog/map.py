"""The map() function is used to apply a given function to every item of an iterable, such as a list or tuple, and returns a map object (which is an iterator).

Let’s start with a simple example of using map() to convert a list of strings into a list of integers."""


s = ['1', '2', '3', '4']
res = map(int, s)
print(list(res))


