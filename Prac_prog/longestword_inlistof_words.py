# Write a Python function that takes a list of words and returns the length of the longest one


# r=["Rohit","Prateek","Akshay","Srinivas","Naveenkumar"]
# def longest_word(r):
#     lw = len(r[0])
#     for i in r:
#         temp=len(i)
#         if len(i) > lw:
#             lw = len(i)
#             temp=i
#     print(f"The longest word--> {temp}, with length of word--> {lw}")
#
# longest_word(r)
"""The Alternate Solution"""
def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return print(word_len[-1][1])
find_longest_word(["PHP","Naveenkumar", "Exercises", "Backend"])