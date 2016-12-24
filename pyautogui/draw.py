#!/usr/bin/env python

import pyautogui, time, math, os

print('Press Ctrl-C to quit\n')

try:
    if os.name == 'posix':
        pyautogui.hotkey('command', 'tab')
    else:
        pyautogui.hotkey('ctrl', 'tab')
    print('switching to draw window\n')
    time.sleep(1)
    pyautogui.scroll(-100)
    time.sleep(1)
    w, h = pyautogui.size()
    print(w, h)
    pyautogui.moveTo(w / 2, h / 2)
    r = 100
    pyautogui.moveTo(w / 2 + r * math.sin(0 * math.pi / 180), h / 2 + r * math.cos(0 * math.pi / 180))
    for i in range(0, 360):
        pyautogui.dragTo(w / 2 + r * math.sin(i * math.pi / 180), h / 2 + r * math.cos(i * math.pi / 180))
    time.sleep(1)
    pyautogui.moveTo(w / 2, h / 2)
    pyautogui.dragRel(0, -r, 2, button='left')
    pyautogui.moveTo(w / 2, h / 2)
    pyautogui.dragRel(0, r, 2, button='left')
    pyautogui.moveTo(w / 2, h / 2)
    pyautogui.dragRel(-r * math.cos(30 * math.pi / 180), r / 2, 2, button='left')
    pyautogui.moveTo(w / 2, h / 2)
    pyautogui.dragRel(r * math.cos(30 * math.pi / 180), r / 2, 2, button='left')
    print('Done')
except KeyboardInterrupt:
    print('Interrupted\n')
