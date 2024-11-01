#Can we update the values of list inside set

# s1={8,7,21,"Prateek","7"}
# print(type(s1))
# print(s1)

#Empty dict with user input values

# name1="Prateek"
# name2="Rohit"
# name3="Ashish"
# name4="Bhavesh"
# value1=input("Enter a valid Designation: ")
# value2=input("Enter a valid Designation: ")
# value3=input("Enter a valid Designation: ")
# value4=input("Enter a valid Designation: ")
# dict1={name1:value1,name2:value2,name3:value3,name4:value4}
# print("Choose from given names to identify the designation",dict1.keys())
# a=input("I have a query what is your designation: ")
# print("Designation of this employee is: ", dict1.get(a))
#=====================================================================================================

"""Slicing of the Input String, This says in indexing[start:stop:skip]"""
# n1="Prateek"
#
# print(n1[:-1])#will remove only last character [For Prateek output will be 'Pratee']
# print(n1[::-1])# will reverse the string Prateek=keetarP
# print(n1[2:3])#will give the character a 2 i.e. a
# print(n1[1:5:2])#will skip alternate character and give the result between index rt
#=====================================================================================================

# """List Functions for check"""
# list1=[3,5,71,53,46,12,65,0]
#
# list1.append(9)#adds 1 element to list
# print(list1)
# list1.extend([5,2,23,67,98])#adds multiple element to list by providing list as a argument
# print(list1)
# list1.pop(5)#Bydefault removes last element in list, else removes the element provided as per argument index
# print(list1)
# list1.sort()#sorts the element of list in ascending order
# print(list1)
# list1.reverse()#sorts the element of the list in descending order
# print(list1)
# print(sum(list1))#Sums all the elements of the list
#
# print(list1.count(5))#Counts the occurance of element in the list
#
# list3=list1.copy()#Makes a copy of existing list
#
# print(list3)
#
# # print(list1.clear())#clears the whole list
#
# print(list1.index(98))#provides index of the given value in list
#
# list3.insert(8,6)#Adds a value before given index
# print(list3)

#=====================================================================================================

# Seperator use and check whether it is getting used in a sentense, ByDefault value of the seperator is Blank space' '
#
# print("Hey","There!!","guys","we","are","using","python", sep="----" , end=" ")

#=====================================================================================================
#Loop elements in dictionary with while and for loop

d1={1:"Prateek",2:"Sam",3:"Jack",4:"Man8",5:"Aquaman","Age":29,"Hobby":"Music"}
# print(d1)
# print(d1.values())

# for u in d1:
#     print(u,":",d1[u],sep="")
#
# print("\nAll elements are printed")

# print(len(d1))
#
# q = 0
# while q <= len(d1):
#     print(d1.get(q))
#     q += q
#     break
