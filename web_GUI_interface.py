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


# App options
"""
Additional options can be passed to eel.start() as keyword arguments.

Some of the options include the mode the app is in (e.g. 'chrome'), the port the app runs on, the host name of the app, and adding additional command line flags.

As of Eel v0.12.0, the following options are available to start():

    mode, a string specifying what browser to use (e.g. 'chrome', 'electron', 'edge', 'custom'). Can also be None or False to not open a window. Default: 'chrome'
    host, a string specifying what hostname to use for the Bottle server. Default: 'localhost')
    port, an int specifying what port to use for the Bottle server. Use 0 for port to be picked automatically. Default: 8000.
    block, a bool saying whether or not the call to start() should block the calling thread. Default: True
    jinja_templates, a string specifying a folder to use for Jinja2 templates, e.g. my_templates. Default: None
    cmdline_args, a list of strings to pass to the command to start the browser. For example, we might add extra flags for Chrome;
    eel.start('main.html', mode='chrome-app', port=8080, cmdline_args=['--start-fullscreen', '--browser-startup-dialog']). Default: []
    size, a tuple of ints specifying the (width, height) of the main window in pixels Default: None
    position, a tuple of ints specifying the (left, top) of the main window in pixels Default: None
    geometry, a dictionary specifying the size and position for all windows. The keys should be the relative path of the page,
    and the values should be a dictionary of the form {'size': (200, 100), 'position': (300, 50)}. Default: {}
    close_callback, a lambda or function that is called when a websocket to a window closes (i.e. when the user closes the window).
    It should take two arguments; a string which is the relative path of the page that just closed, and a list of other websockets that are still open. Default: None
    app, an instance of Bottle which will be used rather than creating a fresh one. This can be used to install middleware on the instance before starting eel,
    e.g. for session management, authentication, etc.

"""

