from PyQt5.QtWidgets import QLabel, QWidget, QHBoxLayout
from UI.common.ellipse import Ellipse
import core.GLOBAL

# Класс индикатора сложности. Встраивается в LevelSwitcher
class DifficultyIndicator:
    def __init__(self):
        # Объявление главного (центрального виджета)
        self.main_widget = QWidget()
        self.main_widget.setFixedSize(504, 163)
        self.main_widget.setStyleSheet('background: rgba(1, 1, 1, 0.06);\
                                        border-radius: 60px;')
        # Объявление элементов индикатора
        self.elements_layout = QHBoxLayout()
        self.ellipse = QLabel()
        self.ellipse.setFixedSize(84, 84)
        self.ellipse.setStyleSheet('background: rgba(1, 1, 1, 0.94);\
                                    border-radius: 42px;')
        self.rectangle_with_difficulty = QLabel()
        self.rectangle_with_difficulty\
            .setText(f'СЛОЖНОСТЬ\n           {core.GLOBAL.difficulty_translator[core.GLOBAL.DIFFICULTY.text]}')
        core.GLOBAL.DIFFICULTY.valueChanged.connect(lambda: self.rectangle_with_difficulty.setText(
            f'СЛОЖНОСТЬ\n           {core.GLOBAL.difficulty_translator[core.GLOBAL.DIFFICULTY.text]}'))
        self.rectangle_with_difficulty.setStyleSheet("background: rgba(0, 0, 0, 0.84);\
                                                        font-size:36px;\
                                                        color:white;\
                                                        padding: 5px;\
                                                        border-radius: 30px;")

        self.rectangle_with_difficulty.setFixedSize(309, 111)
        self.elements_layout.addWidget(self.ellipse)
        self.elements_layout.addWidget(self.rectangle_with_difficulty)
        self.main_widget.setLayout(self.elements_layout)
        # Создание некоторых беллых эллипсов возле текста индикатора
        self.white_ellipse_1 = Ellipse((255, 255, 255, 1), 27)
        self.white_ellipse_1.correctStyleSheet(f'''background: rgba{self.white_ellipse_1.color};
                               border-radius: 12px; ''')
        self.white_ellipse_1.setParent(self.main_widget)
        self.white_ellipse_2 = Ellipse((255, 255, 255, 1), 27)
        self.white_ellipse_2.correctStyleSheet(f'''background: rgba{self.white_ellipse_1.color};
                               border-radius: 12px; ''')
        self.white_ellipse_2.setParent(self.main_widget)
        self.white_ellipse_1.move(193, 105)
        self.white_ellipse_2.move(434, 45)
