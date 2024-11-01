# num = int(input("Enter a valid integer: "))
# temp = num
# digit_count = len(str(num))
# print(digit_count)
# sum = 0
# for i in range(1, num + 1):
#     if temp > 0:
#         digit = temp % 10
#         sum += digit ** digit_count
#         temp=temp // 10
#     i += 1
# if sum==num:
#     print("The provided number is armstrong number: ",sum)
# else:
#     print("The provided number is not a armstrong number")
#========================================================================***************=================================================
# num = int(input("Enter a valid integer: "))
num1=int(input("Enter first number for range: "))
num2=int(input("Enter second number for range: "))

#temp = num2

print("The armstrong numbers in given range are: ")
for num in range(num1, num2 + 1):
    digit_count = len(str(num))
    sum = 0
    temp = num
    while temp>0:
        digit = temp % 10
        sum += digit ** digit_count
        temp //= 10
    if sum==num:
        print(sum)


