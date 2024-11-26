# Write a Python program to get the Fibonacci series between 0 to 50

t=[0]
n=int(input("Enter integer between 1 to 100: "))
b=0
a=1
if n>1:
    for i in range(2,n+1):
        temp=a+b
        a=b
        b=temp
        t.append(temp)
print(f"The Fibo series till requested no.{n} is {t}")

"""Solution :x,y=0,1
while y<50:
    print(y)
    x,y = y,x+y
    """