arr = [57, -57, 57, 57]
x = list(arr)
x.sort()
x.reverse()
st=set(x)
result=max([c for c in st if c!=max(st)])
print(result)
# for i in st:
#     if i!=max(st):
#         print(i)
