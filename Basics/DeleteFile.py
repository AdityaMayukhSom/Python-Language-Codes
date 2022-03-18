import os
import shutil

fileSource = 'D:\\Coding\\Python Development\\DeleteMe.txt'
emptyDirectorySource = ''
nonemptyDirectorySource = ''

try:
    # to remove file
    os.remove(fileSource)

    # to remove empty folder, use rmdir()
    # rmdir stands for remove directory
    os.rmdir(emptyDirectorySource)

    # to remove a folder that contains files use rmtree()
    # rmtree stands for remove tree
    # This function is considered dangerous becuase it deletes all the files and folders inside given directory
    shutil.rmtree(nonemptyDirectorySource)

except FileNotFoundError:
    print('File Does Not Exist!')
except PermissionError:
    print('You Do Not Have Permission To Do That!')
except OSError:
    print('Use cannot delete a folder that contains file using rmdir()')
else:
    print('Deleted Successfully!')
finally:
    print('Program Ends!')
