from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import QPoint, Qt

from core.levels import *
import core.GLOBAL


# Класс отрсиовщика уровня. Используется для первоначальной (фоновой) отросвки графа-уровня
class LevelPainter(QMainWindow):
    def __init__(self, number):
        super().__init__()
        self.setContentsMargins(66, 0, 66, 0)
        self.level_number = number
        self.dot_radius = 11 # радиус отрисовываемых точек
        self.line_width = 1  # ширина длинны
        self.horizontal_margin = 300
        self.vertical_margin = 56

        self.level = None  # Placeholder
        self.level_content_holder = QLabel()

        self.level_content_holder.setStyleSheet('background: rgba(0, 0, 0, 0.05);border-radius: 92px;\
        OneMorePoint{background:rgba(6, 6, 6, 0.76);\
                                    border-radius: 55%};')
        self.setCentralWidget(self.level_content_holder)
        self.get_and_set_level()

    # Вызов операции получения уровня
    def get_and_set_level(self):
        self.level = self.get_level_content()

    # Запуск отрисовки фона (графа). Выполняет каждый раз при вызове self.update()
    def paintEvent(self, event):
        content_painter = QPainter(self)  # Создание экземпляра "отрисовщика"
        # Antialiasing on
        content_painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        # Установка цвета для отрисовки линий и вершин
        color = QColor(3, 3, 3)
        color.setAlpha(200)
        pen = QPen(Qt.PenStyle.SolidLine)
        pen.setColor(color)
        content_painter.setPen(pen)
        content_painter.setBrush(color)
        vertices_list = self.level.vertices_positions
        edges_list = self.level.edges_positions_list
        bypassed_edges_list = self.level.bypassed_edges
        for vertex in vertices_list:
            content_painter.drawEllipse(QPoint(vertex[0] + self.horizontal_margin, vertex[1] + self.vertical_margin),
                                        self.dot_radius, self.dot_radius)
        pen.setWidth(self.line_width)
        content_painter.setPen(pen)
        for edge in edges_list:
            content_painter.drawLine(edge[0] + self.horizontal_margin, edge[1] + self.vertical_margin, edge[2]
                                     + self.horizontal_margin, edge[3] + self.vertical_margin)
        # Установка красного цвета для отрисовки пройденных ребер графа
        color.setRgb(255, 0, 0)
        pen.setColor(color)
        content_painter.setPen(pen)
        for edge in bypassed_edges_list:
            content_painter.drawLine(edge[0] + self.horizontal_margin, edge[1] + self.vertical_margin, edge[2]
                                     + self.horizontal_margin, edge[3] + self.vertical_margin)

        content_painter.end()  # Обязательное заверещение цикла отрисовки

    def get_level_content(self):
        needed_level_name = f'{core.GLOBAL.DIFFICULTY.text}_{self.level_number}'
        match needed_level_name:
            case 'EASY_1':
                needed_level = EASY_1
            case 'EASY_2':
                needed_level = EASY_2
            case 'EASY_3':
                needed_level = EASY_3
            case 'EASY_4':
                needed_level = EASY_4
            case 'EASY_5':
                needed_level = EASY_5
        return needed_level
