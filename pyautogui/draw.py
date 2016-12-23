#!/usr/bin/env python

import pyautogui, time, math

print('Press Ctrl-C to quit\n')

try:
    pyautogui.hotkey('command', 'tab')
    print('switching to draw window\n')
    time.sleep(1)
    pyautogui.scroll(-100)
    time.sleep(1)
    w, h = pyautogui.size()
    print(w, h)
    pyautogui.moveTo(w / 2, h / 2)
    r = 50
    pyautogui.moveRel(0, -r)
    for i in range(0, 360):
        pyautogui.moveTo(w/2 + r * math.sin(i * math.pi / 180), h/2 + r * math.cos(i * math.pi / 180))
        pyautogui.click()
        print(w/2 + r * math.sin(i * math.pi / 180), h/2 + r * math.cos(i * math.pi / 180))
except KeyboardInterrupt:
    print('Interrupted\n')
