# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           for indexing[] use [start:stop:step]
#           for slicing() use (start,stop,step)
#           'start' includes the letter at that index
#           'stop' does not include the letter at that index

# indexing[]

name = "Aditya Mayukh Som"
numList = "123456789"
fname = name[0:13]
lname = name[14:]
evenNum = numList[1::2]
oddNum = numList[0::2]
reversedName = name[::-1]

print(fname)
print(lname)
print(evenNum)
print(oddNum)
print(reversedName)
