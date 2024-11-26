# Generator function: Python Generator functions return a generator object that is iterable, i.e., can be used as an Iterator.
# Generator objects are used either by calling the next method of the generator object
# or using the generator object in a “for in” loop.
def count_up_to(max):
    current = 1
    try:
        while current <= max:
            yield current  # Yield the current number
            current += 1
    finally:
        print("Cleanup code executed, generator is finished.")

# Using the generator
counter = count_up_to(10)
for num in counter:
    print(num)

print("xxxxx=================================================================================xxxxxx")

def fib(limit):
    a, b = 0, 1
    while b < limit:
        yield b
        a, b = b, a + b

# Create a generator object
x = fib(200)

# Iterate over the generator object and print each value
for i in x:
    print(i)
print("xxxxx==============================================================================xxxxx===================")