from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QRadioButton, QVBoxLayout, QHBoxLayout, QGroupBox, QButtonGroup
from random import shuffle

app = QApplication([])  # создание приложения
main_win = QWidget()  # создание главного окна
main_win.setWindowTitle('Memory card')

main_win.c_q = -1
main_win.total = 0
main_win.score = 0

label = QLabel('')

btn1 = QRadioButton('')
btn2 = QRadioButton('')
btn3 = QRadioButton('')
btn4 = QRadioButton('')

answers = [btn1, btn2, btn3, btn4]

rg = QButtonGroup()
rg.addButton(btn1)
rg.addButton(btn2)
rg.addButton(btn3)
rg.addButton(btn4)

push_btn = QPushButton('Следующий вопрос')

# создание группы радиокнопок с вариантами ответов
group1 = QGroupBox('Варианты ответов')
group2 = QGroupBox('Результаты теста')

# создание вертикального лэйаута с кнопками 1 и 2
layout1 = QVBoxLayout()
layout1.addWidget(btn1)
layout1.addWidget(btn2)

# создание вертикального лэйаута с кнопками 3 и 4
layout2 = QVBoxLayout()
layout2.addWidget(btn3)
layout2.addWidget(btn4)

# создание лэйаута со ВСЕМИ кнопками
layout_buttons = QHBoxLayout()
layout_buttons.addLayout(layout1)
layout_buttons.addLayout(layout2)

lb_result = QLabel('')
lb_correct = QLabel('')
lb_true = QLabel('')
vl = QVBoxLayout()
vl.addWidget(lb_correct, alignment = Qt.AlignCenter)
vl.addWidget(lb_true, alignment = Qt.AlignCenter)
# устанавливаем лэйаут со ВСЕМИ кнопками в группу кнопок
group1.setLayout(layout_buttons)
group2.setLayout(vl)

# создаём самый главный лэйаут, где будут не только радиокнопки, но и надпись и пуш-кнопка
layout_main = QVBoxLayout()
layout_main.addWidget(lb_result)
layout_main.addWidget(label)  # добавляем надпись-вопрос
layout_main.addWidget(group1)  # добавляем группу радиокнопок
layout_main.addWidget(group2)
layout_main.addWidget(push_btn)  # добавляем пуш-кнопку

# устанавливаем самый главный лэйаут, где есть ВСЁ, в окно приложения
main_win.setLayout(layout_main)

questions = list()

def next_quest():
    if main_win.c_q != (len(questions)-1):
        main_win.c_q += 1
    else:
        shuffle(questions)
        main_win.c_q = 0
    ind = main_win.c_q
    ass(questions[ind])
    main_win.total += 1

def show_ans():
    group1.hide()
    group2.show()
    push_btn.setText('Следующий вопрос')

def show_correct(res):
    lb_correct.setText(res)
    lb_correct.show()
    lb_true.setText(answers[0].text())
    lb_true.show()
    show_ans()

def kaka():
    rg.setExclusive(False)
    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)
    rg.setExclusive(True)

def check_ans():
    if answers[0].isChecked():
        show_correct('правильно')
        main_win.score += 1
    else:
        show_correct('неверно')
    lb_result.setText('Правильных ответов '+str(main_win.score)+'/'+str(main_win.total))

def show_quest():
    group1.show()
    group2.hide()
    push_btn.setText('Ответить')
    kaka()

def start_test():
    if push_btn.text() == 'Следующий вопрос':
        next_quest()
        show_quest()
    elif push_btn.text() == 'Ответить':
        check_ans()

def ass(q):
    shuffle(answers)
    answers[0].setText(q.right_ans)
    answers[1].setText(q.w1)
    answers[2].setText(q.w2)
    answers[3].setText(q.w3)
    label.setText(q.quest)
    lb_correct.setText(q.right_ans)
    show_quest()

class Question():
    def __init__(self, quest, right_ans, w1, w2, w3):
        self.quest = quest
        self.right_ans = right_ans
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3

q1 = Question('Какой национальности не существует?', 'говноедцы', 'чеченцы', 'немцы', 'ненцы')
questions.append(q1)
q2 = Question('Сколько хромосом у нормального человека?', '46', '47', '333', '50')
questions.append(q2)
q3 = Question('Кто убил Пушкина?', 'Дантес', 'дантист', 'какой-то говнаедец', 'Гитлер')
questions.append(q3)
q4 = Question('Ты кака?', 'нет', 'да', 'да', 'да')
questions.append(q4)
q5 = Question('Как называется явлеие когда животное поедает экскременты?', 'капрофагия', 'испражнение', 'мочеиспускание', 'школа')
questions.append(q5)
q6 = Question('В каком году была придумана песня "Моча съела говно" - Казённый унитаз?', '2016', '2000', '2021', '2022')
questions.append(q6)
q7 = Question('В каком году была придумана песня "Глисты и булочка" - Казённый унитаз?', '2021', '2016', '1996', '2019')
questions.append(q7)
q8 = Question('В каком году была создана группа Казённый унитаз?', '2007', '2000', '1995', '1994')
questions.append(q8)
q9 = Question('Мама любит белый хлеб, Дедушка любит серый хлеб, а папа чёрный. Вопрос: что любит папа?', 'бананы', 'хлеб', 'квас', 'цвет')
questions.append(q9)
q10 = Question('Как переводится black cock?', 'чёрный петух', 'чёрный хлеб', 'никак', 'чёрный банан')
questions.append(q10)

# показываем окно и запускаем приложение
shuffle(questions)
start_test()
push_btn.clicked.connect(start_test)
main_win.show()
app.exec_()