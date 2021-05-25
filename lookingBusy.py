#! python3
# lookingBusy.py - moves the cursos just a little bit each 10 minutes,
# so you don't get in trouble for sleeping at work(maybe).


import pyautogui, time

sleep_time = 60 * 10

while True:
    pyautogui.moveRel((-1, -1))
    time.sleep(sleep_time)