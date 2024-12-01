# Write a Python program to find common items from two lists.
# input
# color1 = "Red", "Green", "Orange", "White"
# color2 = "Black", "Green", "White", "Pink"
# output
# {'Green', 'White'}


def common_items_in_list(l1,l2):
    c=[]
    for i in l1:
        for j in l2:
            if i==j:
                c.append(i)
    return c
color1 = "Red", "Green", "Orange", "White"
l1=list(color1)
color2 = "Black", "Green", "White", "Pink"
l2=list(color2)
result=set(common_items_in_list(l1,l2))

print(f"The common items in list are {result}")