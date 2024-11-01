# class Solution:
#     def is_palindrome(self, x: int) -> bool:
#         a = str(x)
#         if a == a[::-1]:
#             print("The given no. is palindrome")
#             return True
#         return False

num=[1,2,0,5,0,0,15,0]
pos=0

for i in num:
    if i!=0:
        num[pos]=i
        pos+=1
while pos<len(num):
    num[pos]=0
    pos+=1

print(num)


