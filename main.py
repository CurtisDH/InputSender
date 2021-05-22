import os
import sys

from pynput.keyboard import Key, Controller
from pynput import keyboard
import time
import random


config_name = 'data.txt'

# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

FN = os.path.join(application_path, config_name)

#FN = os.path.join(sys.path[0],"data.txt")


def AwaitForKeyPress(key):
    if key is not None:
        if key.char.format(Key) == ToggleKey:
            getText(FN)
    # getText(FN)


def getText(fileName):
    print(open(fileName))
    with open(fileName) as f:
        data = str(f.read())
        f.close()
        keypressArray = []
        for i in data:
            keypressArray.append(i)
        print(keypressArray)
    time.sleep(2)
    keyboardZ.press(Key.backspace)
    for item in keypressArray:
        time.sleep(random.uniform(.02, .07))
        if str(item) == "\n":
            keyboardZ.press(Key.enter)
        for ignore in ignoreChars:
            if str(item) == str(ignore):
                continue
        keyboardZ.press(str(item))
        keyboardZ.release(str(item))


if __name__ == '__main__':
    keyboardZ = Controller()
    ignoreChars = ['!']
    ToggleKey = '*'.format(Key)
    active = False
    print("main")


def on_press(key):
    if not active:
        try:
            print('alphanumeric key {0} pressed'.format(
                key.char))
            try:
                if key.char.format(key) == ToggleKey:
                    AwaitForKeyPress(key)
            finally:
                print("error but caught")
        except AttributeError:
            print('special key {0} pressed'.format(
                key))


def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

listener.start()
