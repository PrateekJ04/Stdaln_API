# Write a Python program to remove duplicates from a list.
# Input a = [10,20,30,20,10,50,60,40,80,50,40]
# Output {40, 10, 80, 50, 20, 60, 30}

# a = [10,20,30,20,10,50,60,40,80,50,40]
# a=set(a)
#
# print(a)

#===========================================================================================================#

def remove_duplicates(a):
    x=[]
    for i in a:
        if not a.count(i)>1 or i not in x:
            x.append(i)

    return x
a = [10,20,30,20,10,50,60,40,80,50,40]
result=remove_duplicates(a)
result = set(result)
print(f"The unique in list are: {result}")