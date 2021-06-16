"""
This is an example of kaki app usin kivymd modules.
"""
import os


from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory

# main.py app class for kaki app with kivymd modules
class LiveApp(MDApp, App):
    """ Hi Windows users """

    DEBUG = 1 # set this to 0 make live app not working

    # *.kv files to watch
    KV_FILES = {
        #os.path.join(os.getcwd(), "restaurant.kv"),
        os.path.join(os.getcwd(), "booking.kv"),

    }

    # class to watch from *.py files
    CLASSES = {
        #"Restaurant": "main",
        "MyGrid":"main"

    }

    # auto reload path
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]


    def build_app(self):

        return Factory.MyGrid()




# finally, run the app
if __name__ == "__main__":
    LiveApp().run()