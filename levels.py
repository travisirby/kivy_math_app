from __future__ import division # use float for fraction by default instead of int

from sympy import *
from random import randint

class Levels():

    question_left_side = ""
    question_right_side = ""

    def generate_question(self):
        x = symbols('x')
        y = symbols('y')

        randomNumber = randint(1,30)

        self.question_left_side = str(randomNumber**2*x)
        self.question_right_side = str(randomNumber*y)

        full_equation = self.question_left_side + " = " + self.question_right_side

        return full_equation


    def generate_answer(self):
        x = symbols('x')
        y = symbols('y')
        answer = solve(Eq(sympify(self.question_left_side), sympify(self.question_right_side)))
        return answer


    def level_one(self):
        pass

