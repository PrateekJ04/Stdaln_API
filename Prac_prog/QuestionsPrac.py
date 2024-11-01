#Find the maximum number in an array

num_list=[100,50,24,67,93,44]
num_list.sort()


#MaxNum=max(num_list)
#MinNum=min(num_list)
#print(MaxNum)
#print(MinNum)

Maxnum=num_list[0]

for num in num_list:

    if num>Maxnum:
        Maxnum=num

print(Maxnum)


# Minimum number
Minnum=num_list[0]
for num in num_list:

    if num<Minnum:
        num=Minnum

print(Minnum)

""""Find the duplicate characters in String"""
#name="Prateek"
def find_duplicates(s):
    seen = set()
    duplicates = set()

    for char in s:
        if char in seen:
            duplicates.add(char)
        else:
            seen.add(char)

    return list(duplicates)


# Example usage:
string = "Prateek"
print("Duplicate characters:", find_duplicates(string))

"""Count Number of characters in String"""


def count_characters(s):
    # Initialize an empty dictionary to store counts
    char_count = {}

    # Count occurrences of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


# Example usage:
string = "Successful"
print("Character counts:", count_characters(string))