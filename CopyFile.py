# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification time)

import shutil
source = 'D:\\Coding\\Python Development\\TestCopy.txt'
destination = 'D:\\Coding\\Python Development\\TestCopy2.txt'

shutil.copyfile(source, destination)  # source,destination
