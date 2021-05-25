#! python3
# instantMessengerBot.py - Sends a steam message to someone from
# the persontomessage variable


from time import sleep
import pyautogui

personToMessage = 'Md'
Message = 'Hello you!'

steamIcon = 'steamLogo.png'


pyautogui.hotkey('win', 'd') # Get's to the desktop
sleep(0.5)

pyautogui.click(pyautogui.size()[0] // 2, pyautogui.size()[1] // 2) # I forget to 'deselect' the icon

# if this doesn't work, try taking a screenshoot of your desktop
# and cutting it, so steam's icon is on focus
iconLocation = pyautogui.locateCenterOnScreen(steamIcon, grayscale=False)
if not iconLocation: raise Exception('Couldn\'t find Steam\'s icon. Try replacing it with a screenshoot of your own.')
pyautogui.click(iconLocation, clicks=2)

sleep(0.5)
friendsLocation = pyautogui.locateCenterOnScreen('nonRaisedFriends.png', grayscale=True)
if not friendsLocation: raise Exception('Couldn\'t find nonRaisedFriends on screen.')
pyautogui.click(friendsLocation)

viewFriendsList = pyautogui.locateCenterOnScreen('viewFriendsList.png', grayscale=True)
if not viewFriendsList: raise Exception('Can\'t find "View Friends List" on screen.')
pyautogui.click(viewFriendsList)

sleep(0.4)
magnifierIcon = pyautogui.locateCenterOnScreen('magnifierIcon.png', grayscale=True)
if not magnifierIcon: raise Exception('Could not locate magnifierIcon on screen.')
pyautogui.click(magnifierIcon)
pyautogui.typewrite(personToMessage)
sleep(0.4)
pyautogui.click(magnifierIcon[0], magnifierIcon[1] + 35, clicks=2)
sleep(0.5)
pyautogui.typewrite(Message)
pyautogui.hotkey('enter')