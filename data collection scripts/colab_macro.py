from pynput.keyboard import Key, Controller
import time
import pyautogui
import random

print(pyautogui.size())
width = pyautogui.size()[0]
height = pyautogui.size()[1]

keyboard = Controller()

hours_to_run = int(input("how many hours to run"))
time_start = time.time()
time_end = time_start+hours_to_run*60*60


i = 0
j = 5
while time.time() < time_end:
    pyautogui.moveTo(random.randint(0, width),random.randint(0, height), duration = 1)
    i += 1
    j += 1
    if i%12 == 0:
        keyboard.press('a')
        keyboard.release('a')
        keyboard.press('b')
        keyboard.release('b')
        keyboard.press('c')
        keyboard.release('c')
        keyboard.press('d')
        keyboard.release('d')
    if i%20 == 0:
        keyboard.press('p')
        keyboard.release('p')
        keyboard.press('r')
        keyboard.release('r')
    
    if j%3 == 0:
        keyboard.press(Key.backspace)
        time.sleep(0.5)
        keyboard.release(Key.backspace)
    if j%10 == 0:
        keyboard.press(Key.backspace)
        time.sleep(0.5)
        keyboard.release(Key.backspace)
    
        
    #time.sleep(1.1)
