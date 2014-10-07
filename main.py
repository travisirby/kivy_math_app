# __author__ = 'travis'

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

from levels import Levels
import app_utils

from sympy import *

class MyWidget(Widget):

    question = ""
    answer = ""
    user_answer = ""
    level = Levels()

    def get_question(self):
        self.question = Levels.generate_question(self.level)

    def set_question(self):
        self.ids.questionLabel.text = self.question

    def new_question(self,dt=None):
        self.ids.answerLabel.text = ''
        self.ids.input.text = ''

        self.get_question()
        self.set_question()
        self.get_answer()

        return self.question

    def get_answer(self):
        self.answer = Levels.generate_answer(self.level)


    def check_user_answer(self):
        x = symbols('x')
        y = symbols('y')

        self.user_answer = app_utils.check_for_asterisks(self.user_answer)

        try:
            compare_answer = Eq(self.answer[0], self.user_answer)
        except:
            print "compare_answer if answer is a list of ints failed"
            try:
                compare_answer = Eq(self.answer[0][x], sympify(self.user_answer))
            except:
                print "compare_answer if answer is a list of dicts failed"
                compare_answer = None

        return compare_answer


    def user_answer_submitted(self, answer_submitted):
        self.user_answer = answer_submitted

        answer_result = self.check_user_answer()

        self.ids.answerLabel.text = str(answer_result)

        try:
            if answer_result:
                Clock.schedule_once(self.new_question, 3)
        except:
            print "failed to compare checkAnswer"


class TitleWidget(Widget):
   pass


class MyLayout(FloatLayout):

    def on_start(self):
        self.add_widget(TitleWidget())

    def goto_questions(self,dt=None):
        self.clear_widgets()
        self.add_widget(MyWidget())


class MainApp(App):

    def build(self):
        rootForm = MyLayout()
        rootForm.on_start()
        return rootForm


if __name__ == '__main__':
    MainApp().run()

# how to strip []
# string.translate(None,"[]")

# sympy fractions: use S(1)/2 or Rational(1,2)

