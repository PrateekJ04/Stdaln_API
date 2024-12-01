# Write a Python program to get the difference between the two lists
# Input
# list1 = [1, 2, 3, 4]
# list2 = [1, 2]
# Output
# [3,4]

def difference_in_lists(l1,l2):
    l3=[]
    for i in l1:
        for j in l2:
            if i not in l2 and l3.count(i)<1:
               l3.append(i)
    return l3
list1 = [5,6,9,2,3,4]
list2 = [3,4]
result = difference_in_lists(list1,list2)
print(f"The difference between two list is {result}")

#Alternate Solution: list1 = [1, 2, 3, 4]
# list2 = [1, 2]
# print(list(set(list1) - set(list2)))