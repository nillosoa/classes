

import shutil, os

prefix = 'spam'
file_ext = '.txt'

folder = os.getcwd()

print('Getting all files that matches the prefix(%s) and extension(%s):' %(prefix, file_ext))
flist = []
for _file in os.listdir(folder):
    if _file.startswith(prefix) and _file.endswith(file_ext):
        flist.append(_file)
        print('Total files: %d.' %(len(flist)), end='\r')


flist.sort()
number = 0
print('\n')
print('Starting to rename them.')
for _file in flist:
    number += 1
    renameto = prefix + str(number) + file_ext
    print('\tRenaming %s to %s...' %(_file, renameto))
    shutil.move(_file, renameto)
