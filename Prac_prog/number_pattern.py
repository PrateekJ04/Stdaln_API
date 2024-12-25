# Write a Python program to construct the following pattern, using a nested loop number.
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

num=9

for i in range(1,num+1):
    for j in range(0,i):
            if j<=i:
                print(i,end='')
    i+=1
    print()

"""for i in range(10):
    print(str(i) * i)"""