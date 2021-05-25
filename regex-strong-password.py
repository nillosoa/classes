

import re

sizeRegex = re.compile(r'(.{8,})')
upperRegex = re.compile(r'([A-Z])')
lowerRegex = re.compile(r'([a-z])')
numeralRegex = re.compile(r'(\d+)')
test = "HelloPassword"

sizeGroup = re.findall(sizeRegex, test)
upperGroup = re.findall(upperRegex, test)
lowerGroup = re.findall(lowerRegex, test)
numeralGroup = re.findall(numeralRegex, test)
TESTS = len(sizeGroup[0]) > 8 and str(upperGroup[0]).isupper() and str(lowerGroup[0]).islower() and str(numeralGroup[0]).isdecimal()

print("Has more than 8 characters?", len(sizeGroup[0]) > 8)
print("Has an upper letter character?", str(upperGroup[0]).isupper())
print("Has lower letter characters?", str(lowerGroup[0]).islower())
print("Has at least one numeral?", str(numeralGroup[0]).isdecimal())
print("Is it safe?", TESTS)