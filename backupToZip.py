#! python3
   # backupToZip.py - Copies an entire folder and its contents into
   # a ZIP file whose filename increments.

import zipfile, os

def backupToZip(folder):
    # Backup the entire content of 'folder' to a zip archive
    folder = os.path.abspath(folder)

    # Figure out the filename
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.isfile(zipFileName):
            break
        number = number + 1

    # Create the .zip file
    print("Creating %s..." %(zipFileName))
    backupZip = zipfile.ZipFile(zipFileName, 'w')

    # Walk the entire folder tree and compress the files in each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s.' %(foldername))
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)
        # Add all files in this folder to the zip file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # Don't backup the zip files
            backupZip.write(os.path.join(foldername, filename))
        backupZip.close()

    print('Done.')

backupToZip(os.getcwd())