__author__ = 'travis'

import kivy

from kivy.app import App
from kivy.uix.widget import Widget

class MyWidget(Widget):
    pass

class HelloApp(App):

    def build(self):
        return MyWidget()


if __name__ == '__main__':
    HelloApp().run()