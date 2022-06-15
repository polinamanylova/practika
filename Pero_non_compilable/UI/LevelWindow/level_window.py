from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QToolButton
from PyQt5.QtGui import QPainter, QColor, QPen, QIcon
from PyQt5.QtCore import Qt, QSize
import core.GLOBAL
from UI.LevelWindow.elements.level_painter import LevelPainter
from UI.LevelWindow.elements.level_indicator import LevelIndicator
from UI.common.back_menu import BackMenu

# Класс Окна с уровнем
class LevelWindow(QMainWindow):
    def __init__(self):
        super(LevelWindow, self).__init__()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.mouse_pos_start = 0
        self.mouse_pos_end_list = []
        self.clicked = False  # Некоторые переменные для выполнения игровых действий
        self.level_over = False

        self.central_vertical_layout = QVBoxLayout(self.central_widget)
        self.central_vertical_layout.setContentsMargins(100, 0, 100, 100)
        self.level_indicator = LevelIndicator()

        self.back_menu = BackMenu(True)

        # Генерация содержимого окна
        self.level_content = LevelPainter(core.GLOBAL.CURRENT_LEVEL_NUMBER.text)
        core.GLOBAL.CURRENT_LEVEL_NUMBER.valueChanged.connect(self.retake_level)
        self.central_vertical_layout.addWidget(self.level_indicator.main_widget)
        self.central_vertical_layout.addWidget(self.level_content)
        self.central_vertical_layout.addLayout(self.back_menu)

        # Создание кнопки перехода на следующий уровень
        self.next_button = QToolButton(self)
        self.next_button.setIcon(QIcon('UI/MainMenu/elements/arrow.png'))
        self.next_button.setIconSize(QSize(95, 95))
        self.next_button.setFixedSize(95, 95)
        self.next_button.setStyleSheet('''color:white;
                                            border-radius:47%;
                                            background:#000000;
                                            font-size:96px;''')
        self.next_button.clicked.connect(self.play_next_level)
        self.next_button.move(1774, 439)

    # Функция перерисовки и смены уровня + генерация содержимого окна
    def retake_level(self):
        self.central_vertical_layout.removeWidget(self.level_indicator.main_widget)
        self.central_vertical_layout.removeWidget(self.level_content)
        self.central_vertical_layout.removeItem(self.back_menu)
        self.level_indicator = LevelIndicator()
        self.level_content = LevelPainter(core.GLOBAL.CURRENT_LEVEL_NUMBER.text)
        self.central_vertical_layout.addWidget(self.level_indicator.main_widget)
        self.central_vertical_layout.addWidget(self.level_content)
        self.central_vertical_layout.addLayout(self.back_menu)
        self.restart_level()
        self.update()

    def play_next_level(self):
        core.GLOBAL.CURRENT_LEVEL_NUMBER.text = \
            int(core.GLOBAL.CURRENT_LEVEL_NUMBER.text) + 1 if int(core.GLOBAL.CURRENT_LEVEL_NUMBER.text) + 1 < 6 else 1
        self.retake_level()
        self.update()

    # Отслеживание того что мышь зажата
    def mousePressEvent(self, event):
        super(LevelWindow, self).mousePressEvent(event)
        if event.button() == Qt.MouseButton.LeftButton and not self.level_over:
            self.clicked = True
            self.mouse_pos_start = event.pos()
            self.mouse_pos_end_list.append(event.pos())
            self.update()

    # Отслеживание того что ЛКМ отпущена
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked = False
            if not self.level_over: self.restart_level()
            self.update()
        super(LevelWindow, self).mouseReleaseEvent(event)

    # Отслеживание того что мышь передвигается
    def mouseMoveEvent(self, event):
        super(LevelWindow, self).mouseMoveEvent(event)
        if self.clicked:
            self.mouse_pos_end_list.append(event.pos())
            self.do_core_operations()
            if not self.level_over:
                self.update()
            else:
                self.update()
                self.mouse_pos_end_list.clear()

    # Функция отрисовки перемещения мыши
    def paintEvent(self, paint_event):
        super(LevelWindow, self).paintEvent(paint_event)
        if self.clicked:
            content_painter = QPainter(self.level_content)
            # Antialiasing on
            content_painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            color = QColor(255, 0, 0)
            pen = QPen(Qt.PenStyle.SolidLine)
            pen.setColor(color)
            content_painter.setPen(pen)
            if not self.level_over:
                content_painter.drawLine(self.mouse_pos_start, self.mouse_pos_end_list[0])
                for i in range(1, len(self.mouse_pos_end_list) - 1):
                    content_painter.drawLine(self.mouse_pos_end_list[i], self.mouse_pos_end_list[i + 1])
            content_painter.end()

    # Функция нахождения пройденных вершин и ребер графа + передача оных в Level и LevelPainter
    def do_core_operations(self):
        # Try to find vertex in level
        level = self.level_content.level
        index = self.level_content.level.vertex_exists(
            self.mouse_pos_end_list[len(self.mouse_pos_end_list) - 1].x() - 300 - 66 * 3 + 100,
            self.mouse_pos_end_list[len(self.mouse_pos_end_list) - 1].y() - 216)
        if index != -1:
            level.previous_painted_vertex = level.current_painted_vertex
            if index != level.current_painted_vertex:
                level.current_painted_vertex = index
                new_edge = sorted((level.previous_painted_vertex, level.current_painted_vertex))
                if level.edge_exists(new_edge):
                    new_edge = self.level_content.level.vertices_positions[new_edge[0]] \
                               + self.level_content.level.vertices_positions[new_edge[1]]
                    if not (new_edge in level.bypassed_edges):
                        level.bypassed_edges.append(new_edge)
                    else:
                        self.restart_level()

        # Условие окончания уровня
        if len(level.bypassed_edges) == len(level.edges_list):
            self.level_over = True

    # Функция обнуления уровня
    def restart_level(self):
        self.level_over = False
        self.clicked = False
        level = self.level_content.level
        self.mouse_pos_start = 0
        self.mouse_pos_end_list.clear()
        level.previous_painted_vertex = -1
        level.current_painted_vertex = -1
        level.bypassed_edges.clear()

