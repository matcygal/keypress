# in command prompt, type "pip install pynput" to install pynput.
# require python3 
from pynput.keyboard import Key, Controller
import time
import random


keyboard = Controller()
keylist = ['c', 'x', 'b', 'n', 'u','i','o']
while True:
    rng_key = random.choice(keylist)
    with keyboard.pressed('s'):
     time.sleep(2)
    time.sleep(random.randint(100,299))
    with keyboard.pressed('s'):
     time.sleep(2)
    time.sleep(random.randint(100,299))
    keyboard.press(rng_key)
    keyboard.release(rng_key)
    time.sleep(random.randint(100,299))
    print('loop executed')

