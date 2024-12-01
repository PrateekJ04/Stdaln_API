#Find Duplicate letters in string

a= "samsung"
b=[]

for char in a:
    if a.count(char)>1 and char not in b :
        b.append(char)

print("Duplicate characters in a string: ", b)
