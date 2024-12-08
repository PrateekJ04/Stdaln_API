# Write a Python program to count the number of characters (character frequency) in a string.
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
from csv import DictReader
from itertools import count

def char_count(string1):
    x = []
    y = []

    for i in string1:
        if i in string1:
            count = string1.count(i)
            x.append(i)
            y.append(count)
    result = dict(zip(x, y))
    return result
string1 = input("Enter a valid string: ")
print(char_count(string1))
