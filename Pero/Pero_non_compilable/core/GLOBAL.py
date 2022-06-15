from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal


# Класс переменной с сигналом. Базируется на QWidget, поскольку по-другому QT сигналы работают через раз.
# Нужен [сигнал] для плавных двусторонних бесшовных переходов между экранными формами
class VariableWithSignal(QWidget):
    valueChanged = pyqtSignal(object)

    def __init__(self):
        super(VariableWithSignal, self).__init__()
        self.text = ''

    def setText(self, str):
        self.text = str
    # Объявление своего метода "геттера" свойства text
    @property
    def text(self):
        return self._text
    # Объявление своего метода "сеттера" свойства text (нужно для отслеживания и активации сигнала)
    @text.setter
    def text(self, value):
        self._text = value
        self.valueChanged.emit(value)


DIFFICULTY = VariableWithSignal()
DIFFICULTY.text = 'EASY'
CURRENT_LEVEL_NUMBER = VariableWithSignal()
CURRENT_LEVEL_NUMBER.text = 1
CURRENT_WINDOW = VariableWithSignal()
CURRENT_WINDOW.text = 'MainMenu'
# Гениальный костыль для интерфейса во многом. Словарь подошел как нельзя кстати
difficulty_translator = {'EASY': 'ПРОСТАЯ', 'MEDIUM': 'СРЕДНЯЯ', 'HARD': 'ВЫСОКАЯ'}
