Press * once you're running the main.py to manually type all text in a document that you need to label data.txt
and place into the directory where you are running the main.py from

You may need to pip install pynput to get this to work

This is a sample text document to display how the key sender works.

If you'd like to compile to application you can use pyinstaller
which will turn it into a usable executable for the build platform.

If you run into issues with pyinstaller try add these commands at the end of your
terminal

--hidden-import-pynput.keyboard._win32
--hidden-import-pynput.mouse._win32

I'm assuming you'd need to replace _win32 with your operating system respectively
i.e _linux for a linux build, _darwin for mac

Sources

https://pynput.readthedocs.io/en/latest/keyboard.html
https://www.pyinstaller.org