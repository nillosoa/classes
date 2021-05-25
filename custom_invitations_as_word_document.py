#! python3
# [long_script_name].py - Parses a given text file composed names and
# creates custom invitations as Docx(or word) documents.
# needs invitations_template.docx
# Use: python custom_invitation_as_word_document.py [guests.txt]

import os, sys, docx, pprint

template = docx.Document('invitations_template.docx')
invitations = docx.Document()

guests_file = sys.argv[1]
guests = []

# Parsing the text file
with open(guests_file, 'r') as gf:
    for line in gf.readlines():
        line = line.replace('\n', '')
        guests.append(line)

# Creating word documents
for gindex in range(len(guests)):
    guest = guests[gindex]
    for pindex in range(len(template.paragraphs)):
        paragraph = template.paragraphs[pindex]
        iparagraph = invitations.add_paragraph('')
        iparagraph.style = paragraph.style
        for rindex in range(len(paragraph.runs)):
            run = paragraph.runs[rindex]
            if '@guest' in run.text:
                irun = iparagraph.add_run(guest)
                irun.style = run.style
                #irun.font = run.font
            else:
                irun = iparagraph.add_run(run.text)
                irun.style = run.style
                #irun.font = run.font


    if not gindex == (len(guests) - 1):
        invitations.add_page_break()
                
invitations.save('invitations.docx')