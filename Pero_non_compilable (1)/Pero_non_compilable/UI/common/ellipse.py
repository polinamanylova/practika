from PyQt5.QtWidgets import QLabel


# В игре много эллипсов. Решил запилить класс, отвечающий за создание такой красоты
# Название аргументов буквально отражает их суть
class Ellipse(QLabel):
    def __init__(self, color, radius, border_radius=50):
        super(Ellipse, self).__init__()
        self.setStyleSheet(f'''background: rgba{color};
                               border-radius: {border_radius}%;    
                                ''')
        self.color = color
        self.radius = radius
        self.setFixedSize(radius, radius)

    def correctStyleSheet(self, newStyleSheet):
        self.setStyleSheet(newStyleSheet)
