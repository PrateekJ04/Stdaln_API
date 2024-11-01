# # This is a brute-force approach to find a tuple that hashes to the given value
# target_hash = 3713081631934410656
#
# # Example of checking tuples
# for i in range(100):  # Adjust range as necessary
#     for j in range(100):
#         test_tuple = (i, j)
#         if hash(test_tuple) == target_hash:
#             print(f"Found tuple: {test_tuple}")
#             break


def swap_char(s):
    x = []
    for char in s:

        if char.isupper():
            x.append(char.lower())

        elif char.islower():
            x.append(char.upper())

    print(''.join(x))

swap_char("Satish, I am Engineer")

# j="Prateek"
# a=j.swapcase()
# print(a)
