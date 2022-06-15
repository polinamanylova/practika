from PyQt5.QtWidgets import QLabel, QWidget, QHBoxLayout
import core.GLOBAL

# Индикатор уровня. Описание и применение аналогично индикатору сложности. За исключением лишь того, что номер уровня
# берется из ядра
class LevelIndicator:
    def __init__(self):
        self.main_widget = QWidget()
        self.main_widget.setFixedSize(504, 163)
        self.main_widget.setStyleSheet('background: rgba(6, 6, 6, 0.08);\
                                        border-radius: 60px;')
        self.elements_layout = QHBoxLayout()
        self.ellipse = QLabel()
        self.ellipse.setFixedSize(111, 111)
        self.ellipse.setStyleSheet('background:rgba(6, 6, 6, 0.76);\
                                    border-radius: 55%;')
        self.rectangle_with_level_number = QLabel()
        self.rectangle_with_level_number.setText(f'УРОВЕНЬ {core.GLOBAL.CURRENT_LEVEL_NUMBER.text}')
        self.rectangle_with_level_number.setStyleSheet("background: rgba(6, 6, 6, 0.76);\
                                                        font-size:36px;\
                                                        color:white;\
                                                        border-radius: 50px;")

        self.rectangle_with_level_number.setFixedSize(309, 111)
        self.elements_layout.addWidget(self.ellipse)
        self.elements_layout.addWidget(self.rectangle_with_level_number)
        self.main_widget.setLayout(self.elements_layout)
