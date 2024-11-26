#  Write a Python program to construct the following pattern, using a nested for loop.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(5):
    for j in range(5):
        if j<=i:
            print("*",end='')
    print('')

for i in range(5):
    for k in range(5):
        if k>=i:
            print("*",end='')
    print('')

