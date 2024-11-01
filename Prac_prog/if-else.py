n = int(input().strip())

x = n % 2
if x == 0 and n > 2 and n <= 5:
    print("Not Weird")
if n > 20 and x==0:
    print("Not Weird")
elif x == 0 and n >= 6 and n <= 20:
    print("Weird")
elif x != 0:
    print("Weird")
