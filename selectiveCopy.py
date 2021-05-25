

import shutil, os


files_ext = '.txt'
folder_name = os.getcwd()
newfolder_name = 'hello'


folder_name = os.path.abspath(folder_name)
newfolder_name = os.path.abspath(folder_name + os.sep + newfolder_name)

if not os.path.isdir(newfolder_name):
    os.mkdir(newfolder_name)

for dirname, subdirs, filenames in os.walk(folder_name):
    print('Copying files from folder %s.' %(folder_name))
    for filename in filenames:
        if filename.endswith(files_ext):
            copied = shutil.copy(filename, newfolder_name)
            print('\tWorking on %s.' %(filename))
            print('\tCopied %s to %s.' %(filename, copied))
            print()
    
    print("Done.")