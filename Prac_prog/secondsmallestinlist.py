# Write a Python program to find the second smallest number in a list.
# input
# second_smallest([1, 2, -8, -2, 0])
# output
# -2

def secondsmallest_in_list(a):
    smallest = float('inf')
    secondsmallest = float('inf')
    for i in a:
        if i<smallest:
            secondsmallest = smallest
            smallest = i
        elif i < secondsmallest:
            secondsmallest = i
    return secondsmallest


a = [1, 2, -8, -2, 0,-3]
result = secondsmallest_in_list(a)
print(f"Second smallest no. in list is: {result}")
