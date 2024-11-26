# Count the number of even and odd numbers from a series of numbers
# Input
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
# Output
# Number of even numbers : 4
# Number of odd numbers : 5

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
x=0
y=0
for i in numbers:
    if i%2==0:
        x+=1
    else:
        y+=1

print(f"Count of odd number : {y}\n"f"Count of even number: {x}")
