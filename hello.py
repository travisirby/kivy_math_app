# __author__ = 'travis'

from __future__ import division
from kivy.app import App
from kivy.uix.widget import Widget

from sympy import *
from random import randint


class MyWidget(Widget):

    str = " True"
    a = 0

    def generateQuestion(self):
        x = symbols('x')
        self.a = randint(1,30)
        #return str(self.a**2)+str(x+self.a)
        return "2x = 5"

    def entered(self, value):
        x = symbols('x')
        ans = solve(Eq(2*x,5))
        self.ids.answerLabel.text = str(Eq(ans[0],sympify(value)))
        print(value)


class HelloApp(App):

    def build(self):
        return MyWidget()


if __name__ == '__main__':
    HelloApp().run()

# how to strip: [ ]
#s+ string.translate(None,"[]")

# sympy fractions: use S(1)/2 or Rational(1,2)