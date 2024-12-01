# Write a Python program to get the frequency of the elements in a list.
# input
# my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
# outout
# {10: 4, 20: 4, 40: 2, 50: 2, 30: 1}

# def freq_of_item(list1):
#     a=[]
#     b=[]
#     for i in list1:
#         if list1.count(i)>0:
#             a.append(i)
#             b.append((list1.count(i)))
#     return dict(zip(a,b))
# my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
# result= freq_of_item(my_list)
# print(f"The occurrence of each item in list is: {result}")
import collections
my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
print("Original List : ",my_list)
ctr = collections.Counter(my_list)
print("Frequency of the elements in the List : ",ctr)