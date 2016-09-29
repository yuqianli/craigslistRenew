#!/usr/bin/python

import pyautogui
import os
 
counter = 0

while True:
    try:
        print ("inside try")
        pyautogui.time.sleep(2)
        renewButtonLocationX,renewButtonLocationY  = pyautogui.locateCenterOnScreen('renew.png')
        pyautogui.moveTo(renewButtonLocationX, renewButtonLocationY)
        pyautogui.click()
        pyautogui.time.sleep(2)

        pyautogui.press('backspace')
        #emailButtonLocationX,emailButtonLocationY  = pyautogui.locateCenterOnScreen('email.png')
        #pyautogui.click(emailButtonLocationX, emailButtonLocationY)
        pyautogui.time.sleep(2)
    except Exception:
        print ("inside exception")
        pyautogui.press('pgdn')
        counter += 1
        print ("counter =" + str(counter))
        if counter >2:
             pyautogui.press('pgup')
        
       # pyautogui.press('backspace')




