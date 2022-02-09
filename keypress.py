# in command prompt, type "pip install pynput" to install pynput.
# require python3 
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
while True:
    with keyboard.pressed('w'):
     time.sleep(0.5)
    time.sleep(2)
    with keyboard.pressed('s'):
     time.sleep(0.5)
    time.sleep(2)
    keyboard.press('c')
    keyboard.release('c')
    time.sleep(2)
    print('loop executed')
