#  Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700

a=1500
b=2700
x=[]
for i in range(a,b+1):
    if i%7==0 and i%5==0:
        x.append(str(i))
y=','.join(x)
print(y)
