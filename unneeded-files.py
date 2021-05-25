

import os

foldertree = os.getcwd()
maxsize = 104857600
foldertree = os.path.abspath(foldertree)

for foldername, subfolders, filenames in os.walk(foldertree):
    for filename in filenames:
        joinedfile = os.path.join(foldername, filename)
        filesize = os.path.getsize(joinedfile)
        if  filesize > maxsize:
            print('%r has %d mb. It is bigger than specified %d mb.' %(joinedfile, (filesize / 1024 / 1024), (maxsize / 1024 / 1024)))


print("Done.")