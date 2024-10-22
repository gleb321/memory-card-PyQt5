from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QTableWidget, QListView, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout,
        QGroupBox, QButtonGroup, QRadioButton,
        QPushButton, QLabel, QSpinBox)
from memo_app import app
from memo_card_layout import layout_card

txt_Question = QLineEdit('')
txt_Answer = QLineEdit('')
txt_Wrong1 = QLineEdit('')
txt_Wrong2 = QLineEdit('')
txt_Wrong3 = QLineEdit('')


layout_form = QFormLayout()

layout_form.addRow('Питання:', txt_Question)
layout_form.addRow('Правильна відповідь:', txt_Answer)
layout_form.addRow('Неправильныий варіант №1:', txt_Wrong1)
layout_form.addRow('Неправильныий варіант №2', txt_Wrong2)
layout_form.addRow('Неправильныий варіант №3:', txt_Wrong3)

btn_create = QPushButton('Додати запитання')
btn_clear = QPushButton('Очистити')

lb_statistics = QLabel("Статистика" )
lb_attempts = QLabel("Разів відповіли: " + "0")
lb_right = QLabel("Вірних відповідей: " + "0")
lb_success = QLabel("Успішність: " + "0")

btn_back = QPushButton('Назад')


layout_main = QVBoxLayout()
layout_main.addLayout(layout_form)

btn_line1 = QHBoxLayout()
btn_line1.addWidget(btn_create)
btn_line1.addWidget(btn_clear)
layout_main.addLayout(btn_line1)

layout_main.addWidget(lb_statistics)
layout_main.addWidget(lb_attempts)
layout_main.addWidget(lb_right)
layout_main.addWidget(lb_success)

layout_main.addWidget(btn_back)
