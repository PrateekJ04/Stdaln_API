# Write a Python program to change a given string to a
# new string where the first and last chars have been exchanged

one_str=input("Enter a valid string say any name: ")

new_str=""

if new_str in one_str:
    new_str=one_str[-1]+one_str[1:-1]+one_str[0]
    print(new_str)