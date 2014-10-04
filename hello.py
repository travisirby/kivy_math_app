# __author__ = 'travis'

from __future__ import division
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock

from sympy import *
from random import randint

class MyWidget(Widget):

    randomNumber = 0

    def generateQuestion(self,dt=None):
        x = symbols('x')
        self.randomNumber = randint(1,30)
        self.ids.answerLabel.text = ''
        self.ids.input.text = ''
        if dt != None:  # Skip if dt is None because this is called at start of app by input in kv
            self.ids.questionLabel.text = str(self.randomNumber**2) + "x = " + str(self.randomNumber)
            return
        return str(self.randomNumber**2) + "x = " + str(self.randomNumber)


    def entered(self, value):
        x = symbols('x')
        answer = solve(Eq(self.randomNumber**2*x,self.randomNumber))
        checkAnswer = Eq(answer[0],sympify(value))
        self.ids.answerLabel.text = str(checkAnswer)
        if checkAnswer:
            Clock.schedule_once(self.generateQuestion, 3)


class HelloApp(App):

    def build(self):
        return MyWidget()


if __name__ == '__main__':
    HelloApp().run()

# how to strip: [ ]
#s+ string.translate(None,"[]")

# sympy fractions: use S(1)/2 or Rational(1,2)