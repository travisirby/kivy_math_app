__author__ = 'travis'

import kivy
import sympy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput

from sympy import *
from random import randint

class MyWidget(Widget):

    str = " True"
    a = 0

    def entered(self, value):
        print(value)


    def random_eq(self):
        x = symbols('x')
        self.a = randint(1,30)
        self.ids.button1.text = str(self.a**2)+str(x+self.a)


    def change_txt(self):
        x = symbols('x')
        #button_txt = simplify(diff(sin(x), x)
        if simplify(diff(sin(x), x) - (-cos(x))) == 0:
            self.ids.button1.text = self.str
        #self.ids.button1.background_color = 1,1,1,1

    def change_txt_back(self):
        x = symbols('x')
        button_txt = integrate(cos(x), x)
        self.ids.button1.text = 'x = ' + str(solve(self.a**2*x+self.a,x)).translate(None,"[]")
        #self.ids.button1.background_color = 1,1,1,0

class HelloApp(App):

    def build(self):
        return MyWidget()


if __name__ == '__main__':
    HelloApp().run()