from PyQt5.QtWidgets import QWidget, QLabel, QToolButton, QMainWindow
from PyQt5.QtGui import QPixmap
import core.GLOBAL
from UI.common.ellipse import Ellipse

# Класс окна с правилами
class RulesWindow(QMainWindow):
    def __init__(self):
        super(RulesWindow, self).__init__()
        self.central_widget = QWidget()
        self.sub_widget = QWidget()

        # Создание таблички ПРАВИЛА ИГРЫ
        self.rules_label = QLabel(parent=self.central_widget)
        self.rules_label.setFixedSize(550, 123)
        self.rules_label.setText('     ПРАВИЛА ИГРЫ')
        self.rules_label.setStyleSheet('''background: rgba(0, 0, 0, 0.83);
                                          color:white;
                                          font-size: 50px;
                                          border-radius: 50px;''')
        self.rules_label.move(139, 48)

        # Создание таблички с правилами непосредственно
        self.rules_itself = QLabel(parent=self.central_widget)
        self.rules_itself.setText(
            '''   Правила игры\n   заключаются в том, что\n   игрок должен обвести\n   сложную замкнутую\n   фигуру, не отрывая пера\n   и не проходить по одним и\n   тем же линиям дважды.\n   Если же пользователь\n   оторвет перо или дважды\n   пройдет по той же линии,\n   то игра начнется сначала.\n ''')
        self.rules_itself.setStyleSheet('''
                                        background: rgba(1, 1, 1, 0.69);
                                        color:white;
                                        font-weight: 400;
                                        font-size: 50px;
                                        border-radius: 50px;''')
        self.rules_itself.setFixedSize(815, 744)
        self.rules_itself.move(346, 209)

        # Объявление кнопки возвращения в главное меню
        self.back_to_main_menu_button = QToolButton(parent=self.central_widget)
        self.back_to_main_menu_button.setFixedSize(220, 88)
        self.back_to_main_menu_button.setText('В ГЛАВНОЕ\nМЕНЮ')
        self.back_to_main_menu_button.setStyleSheet('''background: rgba(0, 0, 0, 0.88);
                                                                        border-radius: 37px;
                                                                        font-size: 29px;
                                                                        color: #FFFFFF;''')
        self.back_to_main_menu_button.clicked.connect(lambda: return_to('MainMenu'))
        self.back_to_main_menu_button.move(self.rules_itself.x() + self.rules_itself.width() + 100, 865)
        self.setCentralWidget(self.central_widget)

        # Создание эллипсов
        self.white_ellipse_1 = Ellipse((196, 196, 196, 1), 32)
        self.white_ellipse_1.correctStyleSheet(f'''background: rgba{self.white_ellipse_1.color};
                                               border-radius: 16px; ''')
        self.white_ellipse_1.setParent(self.central_widget)
        self.white_ellipse_2 = Ellipse((196, 196, 196, 1), 75)
        self.white_ellipse_2.correctStyleSheet(f'''background: rgba{self.white_ellipse_1.color};
                                               border-radius: 37px; ''')
        self.white_ellipse_2.setParent(self.central_widget)
        self.white_ellipse_1.move(629, 119)
        self.white_ellipse_2.move(1057, 229)


def return_to(widget):
    core.GLOBAL.CURRENT_WINDOW.text = widget
