"""Create and runs the application. This is the starting module of the program."""

from application import Application

try:
    # create a test application object
    app = Application()

    # run the application
    app.run()
except Exception as ex:
    print(f"\033[91mAn unexpected error has occurred. Please contact your system administrator.\nError Message: {ex}\033[0m")

