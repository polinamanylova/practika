from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import Qt
from UI.MainMenu.elements import buttons_layout
from PyQt5.QtGui import QPixmap


# Класс главного меню
class MainMenu:
    def __init__(self):
        self.main_window = QMainWindow()
        self.main_window.setWindowTitle('Обведи не отрывая перо')
        self.central_widget = QWidget()

        # Объявление подвиджета для правильной отрисовки кнопок над фоном
        self.sub_widget = QWidget(parent=self.central_widget)
        self.sub_layout = QVBoxLayout()
        self.main_layout = QVBoxLayout()

        self.sub_layout.addLayout(self.main_layout)
        self.feather_logo = QLabel(parent=self.central_widget)
        self.app_name = QLabel(parent=self.central_widget)
        self.main_layout.addLayout(buttons_layout.main_layout)

        self.sub_widget.setLayout(self.sub_layout)
        self.sub_widget.setFixedSize(957, 593)
        self.sub_widget.setStyleSheet('''
                                            background: rgba(46, 38, 38, 0.03);
                                                border-radius: 68px;
                                                ''')

        self.sub_widget.move(426, 263)
        self.construct_logo_and_app_name()
        self.main_window.setCentralWidget(self.central_widget)

    # Создание лого в главном меню
    def construct_logo_and_app_name(self):
        self.feather_logo.move(26, 31) #расположение пера
        self.feather_logo.setPixmap(QPixmap('UI/MainMenu/elements/feather_logo_t.png'))
        self.app_name.setFixedSize(345, 158) #расположение текста
        self.app_name.setPixmap(QPixmap('UI/MainMenu/elements/app_name.png'))
        self.app_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.app_name.move(317, 78)
