from PyQt5.QtWidgets import QStackedWidget
import core.GLOBAL
from UI.MainMenu.main_menu import MainMenu
from UI.LevelWindow.level_window import LevelWindow
from UI.LevelSwitcher.level_switcher import LevelSwitcher
from UI.RulesWindow.rules_window import RulesWindow

# Главный класс Ui, отвечающий за плавные переходы между экранными формами
class WindowSwitcher(QStackedWidget):
    # Инициализация основных экранных форм
    def __init__(self):
        super(WindowSwitcher, self).__init__()
        self.main_menu = MainMenu().main_window
        self.level_switcher = LevelSwitcher()
        self.level_window = None
        self.rules_window = RulesWindow()

        self.addWidget(self.main_menu)
        self.addWidget(self.level_switcher)
        self.addWidget(self.rules_window)
        core.GLOBAL.CURRENT_WINDOW.valueChanged.connect(self.switch_window_to)

    # Функция смены текущего виджета
    def switch_window_to(self, widget):
        if self.level_window is not None: self.removeWidget(self.level_window) # Проверка на наличие окна уровня (требуется для корректной перезаписи)
        if widget == 'MainMenu':
            self.setCurrentIndex(0)
        elif widget == 'LevelSwitcher':
            self.setCurrentIndex(1)
        elif widget == 'RulesWindow':
            self.setCurrentIndex(2)
        elif widget == 'LevelWindow':
            self.level_window = LevelWindow()
            self.addWidget(self.level_window)
            self.setCurrentIndex(3)
        self.update()
