

import re

def re_strip(text, replace=" ", replacewith=""):
    regex = re.compile(replace)
    return re.sub(regex, replacewith, text)

print(re_strip("This string has no spaces in it"))
print(re_strip("This string had all vowels replaced with x", '[aeiouAEIOU]', 'x'))