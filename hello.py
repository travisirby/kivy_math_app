# __author__ = 'travis'

from __future__ import division
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock

from sympy import *
from random import randint

class MyWidget(Widget):

    randomNumber = 0
    question_left_side = ''
    question_right_side = ''

    def generateQuestion(self,dt=None):
        x = symbols('x')
        y = symbols('y')

        self.randomNumber = randint(1,30)
        self.ids.answerLabel.text = ''
        self.ids.input.text = ''

        self.question_left_side = str(self.randomNumber**2*x*y)
        self.question_right_side = str(self.randomNumber)

        full_equation = self.question_left_side + " = " + self.question_right_side

        if dt != None:  # Skip if dt is None because this is called at start of app by input in kv
            self.ids.questionLabel.text = full_equation
            return

        return full_equation


    def entered(self, user_answer):
        x = symbols('x')
        y = symbols('y')

        solve_equation = solve(Eq(sympify(self.question_left_side), sympify(self.question_right_side)))
        print str(solve_equation) + "solve_equation"

        user_answer = self.check_for_asterisk(user_answer)
        try:
            user_answer = sympify(user_answer)
        except:
            print "SYMPIFY OF USER ANSWER FAILED"

        try:
            compare_answer = Eq(solve_equation[0], user_answer)
        except:
            print "compare_answer first try failed"
            compare_answer = Eq(solve_equation[0][x], user_answer)

        print str(compare_answer) + "compare_answer"

        #self.ids.answerLabel.text = str(checkAnswer)
        #if type(checkAnswer) == bool:
        #    Clock.schedule_once(self.generateQuestion, 3)


    def check_for_asterisk(self, equation):
        i = 0
        while i < len(equation):
            if equation[i].isalpha():
                if i != 0 and equation[i-1] != "*":
                    if equation[i-1].isalnum():
                        equation = equation[:i] + "*" + equation[i:]
                        i += 1
                if i+1 != len(equation) and equation[i+1] != "*":
                    if equation[i+1].isalnum():
                        equation = equation[:i+1] + "*"  + equation[i+1:]
                        i += 1
            elif equation[i] == "(":
                if i != 0 and equation[i-1] != "*":
                    if equation[i-1].isalnum():
                        equation = equation[:i] + "*" + equation[i:]
                        i += 1
            elif equation[i] == ")":
                if i+1 != len(equation) and equation[i+1] != "*":
                    if equation[i+1].isalnum():
                        equation = equation[:i+1] + "*" + equation[i+1:]
                        i += 1
            i += 1
        return equation


class HelloApp(App):

    def build(self):
        return MyWidget()


if __name__ == '__main__':
    HelloApp().run()

# how to strip: [ ]
#s+ string.translate(None,"[]")

# sympy fractions: use S(1)/2 or Rational(1,2)

