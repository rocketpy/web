#  Eel  - For little HTML GUI applications, with easy Python/JS interop

# PyPi: https://pypi.org/project/Eel/
# Eel examples: https://github.com/ChrisKnott/Eel/tree/master/examples


# pip install Eel


# Starting the app
# Suppose you put all the frontend files in a directory called web, including your start page main.html, then the app is started like this;

import eel


eel.init('web')
eel.start('main.html')


"""
This will start a webserver on the default settings (http://localhost:8000) and open a browser to http://localhost:8000/main.html.

If Chrome or Chromium is installed then by default it will open in that in App Mode (with the --app cmdline flag),
regardless of what the OS's default browser is set to (it is possible to override this behaviour).
"""

