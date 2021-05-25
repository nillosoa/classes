#! python3
# custom_seating_cards.py - Generates seatings cards in the png(or other hardcoded format)
# for each guest(and line) in guests.txt

from PIL import Image, ImageDraw, ImageFont
import os

GuestsFile = 'guests.txt'
GuestsFolder = 'SeatingCards' # Where to save the created cards
GuestsFolder = os.path.abspath('./' + GuestsFolder)

if not os.path.isdir(GuestsFolder):
    os.mkdir(GuestsFolder)

if not os.path.isfile('flower-clipart.jpg'):
    raise Exception('Missing flower-clipart.jpg')

FlowerIcon = Image.open('flower-clipart.jpg').resize((100, 133))
NameFont = ImageFont.truetype('arial', 32)

with open(GuestsFile, 'r') as gf:
    for guest in gf.readlines():
        IMG = Image.new('RGBA', (288, 360), 'white')
        Draw = ImageDraw.Draw(IMG, 'RGBA')

        Draw.text((5, 10), 'Instructions: Cut the gray rectangle.', 'black')
        Draw.rectangle((10, 30, 280, 350), outline='gray', width=3)

        IMG.paste(FlowerIcon, (15, 216))
        Draw.text((20, 140), 'Dear,', 'purple')
        Draw.text((20, 150), guest, 'purple', NameFont)
        IMG.save(os.path.join(GuestsFolder, guest.strip() + '.PNG'))