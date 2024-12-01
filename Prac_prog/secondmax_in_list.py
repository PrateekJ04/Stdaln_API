# Write a Python program to get the smallest number from a list.
# max_num_in_list([1, 2, -8, 0])
# return 2

"""If value of i reaches to the max then max value will be i only"""
def secondmax_in_list(list1):
    max_ = float('-inf')
    secondmax=float('-inf')
    for i in list1:
      if i>max_:
            secondmax=max_
            max_=i
      elif i>max_ or secondmax!=max_:
            secondmax=i
    return secondmax

list1=[9,6,4,3,8,15,17,65,54]
print(secondmax_in_list(list1))