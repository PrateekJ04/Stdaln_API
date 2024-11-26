# File operations and file handling in python

f = open("testfile.txt", "w")
f.write("This is a newly created file and written some text")
f.close()

x = open("testfile.txt", "a")
x.write("\nThis is a newly added line in existing file")
x.close()

s = open("testfile.txt", "r")
print(s.read())
s.close()
