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


class UserInterface():
    __rootWidget = None

    def __init__(self, currentRootWidget):
        self.__rootWidget = currentRootWidget

    def changeto_questions_widget(self,dt):
        self.__rootWidget.clear_widgets()
        self.__rootWidget.add_widget(MyWidget())


    def add_title_widget(self):
        self.__rootWidget.add_widget(TitleWidget())
        Clock.schedule_once(self.changeto_questions_widget, 3)

class MainApp(App):

    def build(self):
        rootForm = FloatLayout()
        ui = UserInterface(rootForm)
        ui.add_title_widget()
        return rootForm


if __name__ == '__main__':
    MainApp().run()

# how to strip []
# string.translate(None,"[]")

# sympy fractions: use S(1)/2 or Rational(1,2)

