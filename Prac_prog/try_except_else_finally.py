#Try the block of code in try except else and finally

a = 100
b=5

try:
    c=a/b
    print(c)

except ZeroDivisionError as z:

    print(f"you got a exception: {z}")

except TypeError as T:

    print(f"you got a exception: {T}")

except ValueError as V:
    print(f"you got a exception: {V}")

else:
    print("Need to give proper input")

finally:
    print("Code execution is completed")
