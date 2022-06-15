from PyQt5.QtWidgets import QGridLayout, QToolButton
import core.GLOBAL


# Класс с кнопками для возвращения в разные менюшки (главное, выбор сложности и к списку уровней вроде)
# Базируется на QGridLayout, поскольку планируется внедрение в другие виджеты
class BackMenu(QGridLayout):
    # full отвечает за наличие/отсутствие кнопки возвращения к списку уровней
    def __init__(self, full: bool = False):
        super(BackMenu, self).__init__()
        # Объявление кнопки
        self.back_to_main_menu_button = QToolButton()
        self.back_to_main_menu_button.setFixedSize(261, 111)
        self.back_to_main_menu_button.setText('В\nГЛАВНОЕ\nМЕНЮ')
        # Установка стиля кнопки (css)
        self.back_to_main_menu_button.setStyleSheet('''background: rgba(0, 0, 0, 0.88);
                                                                border-radius: 50px;
                                                                font-size: 29px;
                                                                color: #FFFFFF;''')
        # Установка функции-ответчика на нажатие на кнопку
        self.back_to_main_menu_button.clicked.connect(lambda: return_to('MainMenu'))
        self.back_to_level_list = QToolButton()
        self.back_to_level_list.setFixedSize(261, 111)
        self.back_to_level_list.setText('НАЗАД К\nСПИСКУ\nУРОВНЕЙ')
        self.back_to_level_list.clicked.connect(lambda: return_to('LevelSwitcher'))
        self.back_to_level_list.setStyleSheet('''background: rgba(0, 0, 0, 0.88);
                                                                                    border-radius: 50px;
                                                                                    font-size: 29px;
                                                                                    color: #FFFFFF;''')
        # Добавление виджетов в список виджетов. Последние две цифры означают координатное положение в сетке
        # (строка, столбец)
        if full:
            self.addWidget(self.back_to_level_list, 0, 2)
            self.addWidget(self.back_to_main_menu_button, 0, 3)
        else:
            self.addWidget(self.back_to_main_menu_button, 0, 3)


# Простая функция перехода к другой экранной форме (указывается в аргументе, позже анализируется в WindowSwitcher)
# Как было описано ранее, аргумент этой функции передается через qtSignal в WindowSwitcher
def return_to(widget):
    core.GLOBAL.CURRENT_WINDOW.text = widget
