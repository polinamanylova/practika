from PyQt5.QtWidgets import QGridLayout, QToolButton, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt
import core.GLOBAL
from sys import exit

# Файл с содержанием кнопок главного меню. Название отражают содержание

main_layout = QGridLayout()

play_button = QToolButton()
play_button.setFixedSize(267, 240)
play_button.setStyleSheet('''
                            background: rgba(3, 3, 3, 0.89);
                            border: 1px solid #060606;
                            color:white;
                            font-size: 30px;
                            border-radius: 50px;''')
play_button.setIcon(QIcon('UI/MainMenu/elements/play_button.png'))
play_button.setText('ИГРАТЬ')
play_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
play_button.setIconSize(QSize(111, 111))
play_button.clicked.connect(lambda : send_change_signal("LevelSwitcher"))

about_game_button = QToolButton()
about_game_button.clicked.connect(lambda : send_change_signal('RulesWindow'))
about_game_button.setFixedSize(193, 180)
about_game_button.setText('ОБ ИГРЕ')
about_game_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
about_game_button.setIcon(QIcon('UI/MainMenu/elements/star.png'))
about_game_button.setIconSize(QSize(129, 112))
about_game_button.setStyleSheet('''
                                background: #010101;
                                font-size:25px;
                                color: white;
                                border-radius: 50px;
                                ''')

next_button = QToolButton()
next_button.clicked.connect(exit)
next_button.setIcon(QIcon('UI/MainMenu/elements/arrow.png'))
next_button.setIconSize(QSize(95, 95))
next_button.setFixedSize(95, 95)
next_button.setStyleSheet('''color:white;
                            border-radius:47%;
                            background:#000000;
                            font-size:96px;''')
main_layout.addWidget(play_button, 1, 1)
main_layout.addWidget(about_game_button, 2, 2)
main_layout.addWidget(next_button, 3, 3)


def send_change_signal(widget):
    core.GLOBAL.CURRENT_WINDOW.setText(widget)
