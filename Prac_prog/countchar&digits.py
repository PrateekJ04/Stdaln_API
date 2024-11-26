# Write a Python program that accepts a string and calculate the number of digits and letters
# Sample Data : "Python 3.2"
# Expected Output :
# Letters 6
# Digits 2
#
#
# string="Python 3.2"
# str1=string.split()
# str2=str1[0]
# str3=str1[1]
# x=0
# y=0
# for i in string:
#     if i in string:
#         x+=1
#
#
# for j in str3:
#     if j in str3 and "." not in j:
#         y+=1


s = input("Input a string")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)