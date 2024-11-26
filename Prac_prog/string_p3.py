# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5
# Expected Result : 615

num= int(input("Enter a valid integer in range 1-10: "))

n=num
nn=num*95
nnn=num*27

print(f"Result of the provided number for expression n+nn+nnn is {n+nn+nnn}")
