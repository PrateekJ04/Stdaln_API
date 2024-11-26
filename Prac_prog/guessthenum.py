# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
import random

a= random.randint(1, 9)

num=int(input("Enter the number: "))
if num == a:
    print(f"You guessed it right!!!!, its {num} ")
elif num<=a or num+1==a:
    print(f"You guessed it too low!!")
elif  num>= a:
    print(f"You guessed it too high!!")
else:
    print("Try again, You missed it this time")

print(f"The real no. is {a}")

"""Solution:import random
number = random.randint(1,9)
guess = 0
count = 0
while guess != number and guess != "exit":
    guess = input("What's your guess?")
    
    if guess == "exit":
        break
    
    guess = int(guess)
    count += 1
    
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("You got it!")
        print("And it only took you",count,"tries!")"""

