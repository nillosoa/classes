#! python3
# brute-force_password_breaker.py - tests a dictionary of words against a PDF file.

import PyPDF2, sys

documentname = sys.argv[2]
wordsfile    = sys.argv[1]

words    = []
password = None

print('Reading dictionary...')
with open(sys.argv[1]) as wf:
    for line in wf.readlines():
        line = line.replace('\n', '')
        words.append(line)

print('Starting tests')
with open(documentname, 'rb') as df:

    document = PyPDF2.PdfFileReader(df)
    for word in words:
        print('Testing against: ' + word, end='\r')
        status = document.decrypt(word)
        if status == 1:
            password = word
            break

print()
if password:
    print('Test concluded.')
    print('Password:', password)
else:
    print('Password not on given dictionary.')