from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QToolButton, QHBoxLayout, QVBoxLayout
from UI.LevelSwitcher.elements import difficulty_indicator
from UI.common.back_menu import BackMenu
import core.GLOBAL

# Создание класса формы с кнопками уровней
class LevelSwitcher(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Создание прямоугольников на заднем фоне
        self.white_rectangle = QLabel(self.central_widget)
        self.white_rectangle.setFixedSize(882, 473)
        self.white_rectangle.setStyleSheet('''
                                        background: rgba(6, 6, 6, 0.04);
                                        border-radius: 60px;''')
        self.white_rectangle.move(250, 404)
        self.gray_rectangle = QLabel(self.central_widget)
        self.gray_rectangle.setFixedSize(782, 473)
        self.gray_rectangle.setStyleSheet('''
                                        background: rgba(6, 6, 6, 0.08);
                                        border-radius: 60px;''')
        self.gray_rectangle.move(878, 249)

        # Объявление главного шаблона формы и добавление в него индикатора сложности (добавляется извне)
        self.main_layout = QVBoxLayout()
        self.difficulty_indicator = difficulty_indicator.DifficultyIndicator()
        self.difficulty_indicator.main_widget.setParent(self.central_widget)
        self.difficulty_indicator.main_widget.move(14, 46)

        # Создание и добавление таблички УРОВНИ
        self.level_label = QLabel(self.central_widget)
        self.level_label.move(890-self.level_label.width(), 249)
        self.level_label.setText('   УРОВНИ  ')
        self.level_label.setFixedSize(354, 104)
        self.level_label.setStyleSheet('''background: rgba(3, 3, 3, 0.85);
                                          border-radius: 50px;
                                          font-weight: 400;
                                          color:white;
                                          font-size: 64px;''')

        # Создание формы с кнопками
        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setContentsMargins(150, 0, 150, 0)
        # Последовательная генерация кнопок
        for i in range(1, 6):
            self.level_button = QToolButton()
            self.level_button.setText(str(i))
            self.level_button.setFixedSize(137, 131)
            # Добавление только что созданной кнопке функции по нажатию. (sender запоминает и выдает указатель на конкретный объект)
            self.level_button.clicked.connect(lambda: setAndStartLevel(self.sender().text()))
            self.level_button.setStyleSheet('''
                                            background: rgba(6, 6, 6, 0.66);
                                            border-radius: 25px;
                                            color: white;
                                            font-size: 64px;
                                            ''')
            self.buttons_layout.addWidget(self.level_button)

        # Добавление меню возвращения
        self.back_menu = BackMenu()
        self.back_menu.setContentsMargins(1000, 0, 0, 0)
        self.main_layout.setContentsMargins(0, 400, 0, 0)
        self.main_layout.addLayout(self.buttons_layout)
        self.main_layout.addLayout(self.back_menu)

        self.central_widget.setLayout(self.main_layout)


def setAndStartLevel(level_number):
    core.GLOBAL.CURRENT_LEVEL_NUMBER.text = level_number
    core.GLOBAL.CURRENT_WINDOW.text = 'LevelWindow'
