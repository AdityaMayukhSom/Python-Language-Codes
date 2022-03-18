# File IO Basics.

'''

"r" - Open File For Reading - Default
"w" - Open a file for writing
"x" - Creates file if file does no exist
"a" - Add more content to a file
"t" - Text Mode - Default 
"b" - Binary Mode
"+" - Read And Write

'''

path1 = 'D:\\Coding\\Python Development\\FileIOBasics1.txt'
path2 = 'D:\\Coding\\Python Development\\FileIOBasics2.txt'
f1 = open(path1, "r")
f2 = open(path2, "a")


'''

content = f1.read()
print(content)

for i in content:
    print(i)

for i in f1:
    print(i, end="")
print(f1.readline())
print(f1.readline())

'''


f2.write("\nMy name is Dipta Majhi")


f1.close()  # You should always close the opened file
f2.close()  # You should always close the opened file
