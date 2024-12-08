# Write a Python program to remove the nth index character from a nonempty string

def remove_nth_char(l1, charindex):
    n = []
    if len(l1) > 0:
        for i in range(len(l1)):
            n.append(l1[i])
            if charindex == i:
                n.pop(i)

    l1 = ''.join(n)
    return l1


print(remove_nth_char("Prateek", 2))
print(remove_nth_char("Prateek", 4))

"""Alternate Solution:
def remove_char(str, n):
      first_part = str[:n] 
      last_pasrt = str[n+1:]
      return first_part + last_pasrt
    
print(remove_char('Python', 0))
print(remove_char('Python', 3))
print(remove_char('Python', 5))"""