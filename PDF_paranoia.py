#! python3
# PDF_paranoia.py - Encrypts all PDFs from the CWD and os.walk, testing the password before deleting the original file
# I HATE THIS SCRIPT. JUST AN RANDOM DEV APPRENTICE COMMENT.
import os, sys, shutil, PyPDF2

password = sys.argv[1]
WorkingDir = os.path.abspath('.')
TempDir = os.path.join(WorkingDir, 'PdfParanoiaTEMP') #I've decided to use a temporary directory instead of a list.
EncryptedDir = os.path.join(WorkingDir, 'PdfParanoiaEncrypted')

print('Working on %s and subdirectories.' %WorkingDir)
if not os.path.isdir(TempDir):
    os.mkdir(TempDir)
    print('DEBUG: Temporary directory created.')

if not os.path.isdir(EncryptedDir):
    os.mkdir(EncryptedDir)
    print('DEBUG: Encrypted directory created.')

totalpdf = 0 #Only for debugging
dots = ['...', '.  ', '.. ']
curdot = len(dots) - 1
for dirpath, dirnames, filenames in os.walk(WorkingDir):
    for filename in filenames:
        print(dots[curdot], end='\r') #Yes. I'm probably working. I think...
        curdot += 1
        if curdot > (len(dots) - 1): curdot = 0
        if filename.endswith('.pdf'):
            absFilename = os.path.join(dirpath, filename)
            try:
                shutil.copy(absFilename, os.path.join(TempDir, filename))
                totalpdf += 1
            except PermissionError:
                if os.path.isfile(absFilename):
                    raise shutil.SameFileError
                else:
                    print('INFO: Could not copy %s. Ignoring file...' %filename)
            except shutil.SameFileError:
                continue

print("Done search.")
print("Found a total of %d PDF documents." %totalpdf)
for filename in os.listdir(TempDir):
    reader_fobj = open(os.path.join(TempDir, filename), 'rb')
    writer_fobj = open(os.path.join(EncryptedDir, filename.split('.')[0] + '_encrypted.pdf'), 'wb')
    reader = PyPDF2.PdfFileReader(reader_fobj)
    writer = PyPDF2.PdfFileWriter()

    if reader.isEncrypted:
        print('File encrypted. Skipping...')
        continue

    for page in reader.pages:
        writer.addPage(page)

    writer.encrypt(password)
    writer.write(writer_fobj)
    reader_fobj.close()
    writer_fobj.close()

try:
    print('DEBUG: Trying to delete Temporary Directory...')
    shutil.rmtree(TempDir)
except:
    print('Could not delete TempDirectory. Try deleting it manually to avoid future script errors.')