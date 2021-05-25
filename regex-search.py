# regex-search.py - searches all .txt files of a given directory using a regex pattern
# Usage: regex-search.py (./) (grades)
import sys, re
from os import path, listdir

mydirectory  = sys.argv[1]
regexPattern = " ".join(sys.argv[2:])
regex = re.compile(regexPattern)

if not path.isdir(mydirectory):
    print("Given directory is invalid.")
    sys.exit()

for x in listdir(mydirectory):
    if x.endswith('.txt'):
        txtfile = open(x, 'r')
        txtfile_lines = list(txtfile.readlines())
        print("For {x}:".format(x=x))
        for index in range(len(txtfile_lines)):
            line = txtfile_lines[index]
            matched = re.findall(regex, line)
            if len(matched) >= 1:
                for group in matched:
                    print("\tFound '{match}' on line {li}.".format(li=index+1, match=group))
        txtfile.close()

        