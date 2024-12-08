# Write a Python program to sum all the items in a list
# Example sum_list([1,2,-8])
# Return -5

def sum_list(list1):
    return sum(list1)

list1=[1,2,-8]
result= sum_list(list1)

print(f"Value of the sum of list is {result}")

"""Alternate Solution from iterations: def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,-8]))"""
