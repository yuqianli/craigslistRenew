#!/usr/bin/python

import pyautogui
import os
 
counter = 0 #count the # of exceptions occur

while True:
    try:
        print ("inside try")
        pyautogui.time.sleep(2)
        renewButtonLocationX,renewButtonLocationY  = pyautogui.locateCenterOnScreen('renew.png')
        pyautogui.moveTo(renewButtonLocationX, renewButtonLocationY)
        pyautogui.click()
        pyautogui.time.sleep(2)

        pyautogui.press('backspace')

        pyautogui.time.sleep(2)

	# Exception handle when pyautogui can't locate the renew button on the screen
    except Exception:
        print ("inside exception")
        pyautogui.press('pgdn')
        counter += 1
        print ("counter =" + str(counter))
        if counter >2:
             pyautogui.press('pgup')
       
