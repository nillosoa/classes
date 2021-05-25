
text = """The ADJECTIVE panda walked to the NOUN1 and then VERB. A nearby NOUN2
truck was unaffected by these events.
"""

print('Enter an adjective:')
ADJECTIVE = input()

print('Enter a noun:')
NOUN = input()

print('Enter a verb:')
VERB = input()

print('Enter another noun:')
NOUN2 = input()

print("\n\n")
text = text.replace("ADJECTIVE", ADJECTIVE)
text = text.replace("NOUN1", NOUN)
text = text.replace("VERB", VERB)
text = text.replace("NOUN2", NOUN2)
print(text)

madlib = open('madlib.txt', 'w')
madlib.write(text)
madlib.close()