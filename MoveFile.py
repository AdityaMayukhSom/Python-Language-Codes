import os

source = 'D:\\Coding\\Python Development\\TestCopy.txt'
destination = 'D:\\Coding\\Moved.txt'  # Change the name of the fmoved file

try:
    # Checks if there is already a file with same name at destination
    if os.path.exists(destination):
        print('File already exists!')
    else:
        os.replace(source, destination)
        print('File Was Moved')
except FileNotFoundError:
    print('File Not Found At Given Source')
