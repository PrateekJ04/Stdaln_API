#Write a Python program to check a triangle is valid or
#
# t1=int(input("Enter side 1 measurement: "))
# t2=int(input("Enter side 2 measurement: "))
# t3=int(input("Enter side 3 measurement: "))
#
# if t1>0 and t2>0 and t3>0:
#     print("\nIt is a triangle")
#
# else:
#     print("\nNot a valid triangle")

def triangle_check(l1,l2,l3):
    if (l1>l2+l3) or (l2>l1+l3) or (l3>l1+l2):
        print('No, the lengths wont form a triangle')
    elif (l1==l2+l3) or (l2==l1+l3) or (l3==l1+l2):
        print('yes, it can form a degenerated triangle')
    else:
        print('Yes, a triangle can be formed out of it')
length1 = int(input('enter side 1\n'))
length2 = int(input('enter side 2\n'))
length3 = int(input('enter side 3\n'))
triangle_check(length1,length2,length3)

