# Write a Python program to check whether an alphabet is a vowel or consonant

letters=input("Enter a letter to know whether it is a vowel or consonant: ")
vowels="aeiou"

for i in vowels:
    if i==letters:
        print("It is a vowel")
        break
    else:
        print("It is a consonant")
        break

