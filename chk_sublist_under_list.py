# Write a Python program to check whether a list contains a sublist.
# Input
# a = [2,4,3,5,7]
# b = [4,3]
# c = [3,7]
# print(is_Sublist(a, b))
# print(is_Sublist(a, c))
# Output

# a = [2,4,3,5,7]
# b = [4,3]
# c = [3,7]
# a_new=set(a)
# b_new=set(b)
# c_new=set(c)
#
# if b_new.issubset(a_new):
#     print("b is sublist of a ")
# if c_new.issubset(a_new):
#     print("c is  sublist of a")
# if b_new.issubset(a_new)==False and c_new.issubset(a_new)==True:
#     print("c is  sublist of a")
# if c_new.issubset(a_new)==False and b_new.issubset(a_new)==True:
#     print("b is  sublist of a")
# if c_new.issubset(a_new)==False and b_new.issubset(a_new)==False:
#     print("Not a sublist")


def is_Sublist(l, s):
    sub_set = False
    if s == []:
        sub_set = True
    elif s == l:
        sub_set = True
    elif len(s) > len(l):
        sub_set = False

    else:
        for i in range(len(l)):
            if l[i] == s[0]:
                n = 1
                while (n < len(s)) and (l[i + n] == s[n]):
                    n += 1

                if n == len(s):
                    sub_set = True

    return sub_set


a = [2, 4, 3, 5, 7]
b = [4, 3]
c = [3, 7]
print(is_Sublist(a, b))
print(is_Sublist(a, c))