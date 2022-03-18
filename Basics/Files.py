# Windows + . enables emojis
import os
path1 = "D:\\Coding\\Python Development\\TestFile1.txt"
path2 = "D:\\Coding\\Python Development\\TestFile2.txt"

# File Detection In Python

if os.path.exists(path1):
    print("That location exists!")
    if os.path.isfile(path1):
        print('The Given Input Is A File')
    elif os.path.isdir(path1):
        print('The Given Input Is A Directory')
else:
    print("This location doesn't exist!")

# File Reading In Python

try:
    with open(path1) as file:  # Automatically closes the file
        print(file.read())
    # Returns true if the file is closed, else returns false
    print(file.closed)
except FileNotFoundError as e:
    print('That file was not found!')
    print(e)
except Exception:
    print('Something else went wrong!')


# File Writing In Python

overWriteText = 'Hola, Amigo\nThis Is Some Text\nHave A Nice Day'
appendText = "\nI study in Jadavpur University"

with open(path2, 'w') as file:
    file.write(overWriteText)

# By Default the second parameter in open method is 'r' for read
# 'w' is for write, it over writes the previous text
# 'a' is for append, it adds text to already existing files

with open(path2, 'a') as file:
    file.write(appendText)


# reading the final file after editing

with open(path2) as file:
    print(file.read())
