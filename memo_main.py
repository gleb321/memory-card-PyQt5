from memo_card_layout import *
from memo_menu_layout import *
from time import sleep
from PyQt5.QtWidgets import QWidget
from random import shuffle, choice

card_width, card_height = 600, 500
text_wrong = 'Невірно'
text_correct = 'Правильно'


class Question():
    def __init__(self, question, answer, wrong_ans1, wrong_ans2, wrong_ans3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_ans1
        self.wrong_answer2 = wrong_ans2
        self.wrong_answer3 = wrong_ans3
        self.actual = True
        self.count_asked = 0
        self.count_right = 0
    def got_right(self):
        self.count_asked += 1
        self.count_right += 1
    def got_wrong(self):
        self.count_asked += 1


q1 = Question('Яблуко', 'apple', 'application', 'pinapple', 'apply')
q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
q3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
q4 = Question('Число', 'number', 'digit', 'amount', 'summary')

questions = [q1, q2, q3, q4]


def new_question():
    random_question = choice(questions)
    radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
    shuffle(radio_list)
    global answer
    answer = radio_list[0]  # мы не знаем, какой это из радиобаттонов, но можем положить сюда правильный ответ и запомнить это
    wrong_answer1, wrong_answer2, wrong_answer3 = radio_list[1], radio_list[2], radio_list[3]
    answer.setText(random_question.answer)
    wrong_answer1.setText(random_question.wrong_answer1)
    wrong_answer2.setText(random_question.wrong_answer2)
    wrong_answer3.setText(random_question.wrong_answer3)
    lb_Question.setText(random_question.question)


def rest():
    N = box_Minutes.value()
    win_card.hide()
    sleep(N)
    win_card.show()


btn_Sleep.clicked.connect(rest)


def check_result():
    ''' проверка, правильный ли ответ выбран
    если ответ был выбран, то надпись "верно/неверно" приобретает нужное значение
    и показывается панель ответов '''
    correct = answer.isChecked()
    if correct:
        lb_Result.setText('Правильно')
        # Question.got_right()
    else:
        lb_Result.setText('Неправильно')
        # answer.got_wrong()


def switch_screen():
    if btn_OK.text() == 'Відповісти':
        check_result()
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn_OK.setText('Наступне питання')
    else:
        new_question()
        RadioGroupBox.show()
        AnsGroupBox.hide()
        btn_OK.setText('Відповісти')
        # сбросить выбранную радио-кнопку
        RadioGroup.setExclusive(False) # сняли ограничения, чтобы можно было сбросить выбор радиокнопки
        rbtn_1.setChecked(False)
        rbtn_2.setChecked(False)
        rbtn_3.setChecked(False)
        rbtn_4.setChecked(False)
        RadioGroup.setExclusive(True) # вернули ограничения, теперь только одна радиокнопка может быть выбрана





# Кнопка очистить поля
def clear_lines():
    txt_Question.clear()
    txt_Answer.clear()
    txt_Wrong1.clear()
    txt_Wrong2.clear()
    txt_Wrong3.clear()


btn_clear.clicked.connect(clear_lines)


#Кнопка создать новый вопрос
def add_question():
    question = txt_Question.text()
    answer = txt_Answer.text()
    wrong_ans1 = txt_Wrong1.text()
    wrong_ans2 = txt_Wrong2.text()
    wrong_ans3 = txt_Wrong3.text()
    q = Question(question, answer, wrong_ans1, wrong_ans2, wrong_ans3)
    questions.append(q)
    clear_lines()


btn_create.clicked.connect(add_question)


def menu_stat():
    # lb_attempts.setText("Разів відповіли: " + str(Question().count_asked))
    # lb_right.setText("Вірних відповідей: " + str(Question().count_asked))
    # lb_success.setText("Успішність: " + str(Question().count_asked))
    win_card.hide()
    win_menu.show()


btn_Menu.clicked.connect(menu_stat)


def card_stat():
    win_menu.hide()
    win_card.show()

btn_back.clicked.connect(card_stat)

win_card = QWidget()
win_card.resize(card_width, card_height)
win_card.move(300, 300)
win_card.setWindowTitle('Memory Card')

win_card.setLayout(layout_card)
new_question()

btn_OK.clicked.connect(switch_screen)

win_menu = QWidget()
win_menu.setLayout(layout_main)

win_card.show()
app.exec_()

