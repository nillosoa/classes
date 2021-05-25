#! python3
# mouseNow.py - Displays the mouse cursor's current position.
import pyautogui

try:
    print('Screen size:', pyautogui.size())
    while True:
        # Mouse position
        x, y = pyautogui.position()
        xyString = 'x: ' + str(x).rjust(4) + '  y: ' + str(y).rjust(4)
        # The rgb color of what's in the current mouse position
        pixelColor = pyautogui.screenshot().getpixel((x, y))
        colorString = ' rgb: (' + str(pixelColor[0]).rjust(3)
        colorString += ', ' + str(pixelColor[1]).rjust(3)
        colorString += ', ' + str(pixelColor[2]).rjust(3) + ')'
        positionStr = xyString + colorString # Concatenates both strings
        print(positionStr, end='') # Prints it without a newline(\n)
        print('\b' * len(positionStr), end='', flush=True) # Erases(\b) it, so new data can be add
except KeyboardInterrupt:
    print('\nDone.')