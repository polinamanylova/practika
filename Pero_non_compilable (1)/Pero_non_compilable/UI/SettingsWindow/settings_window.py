from PyQt5.QtWidgets import QLabel, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QToolButton
from UI.common.ellipse import Ellipse
from UI.common.back_menu import BackMenu


class SettingsWindow(QMainWindow):
    def __init__(self):
        super(SettingsWindow, self).__init__()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.settings_name_widget = QWidget(self.central_widget)
        self.settings_name_layout = QHBoxLayout()
        self.settings_name_layout.setSpacing(10)
        self.settings_name_widget.setLayout(self.settings_name_layout)
        self.ellipse = Ellipse((0, 0, 0, 0.79), 110)
        self.ellipse.correctStyleSheet(f'''background: rgba{self.ellipse.color};
                               border-radius: 50%;    
                                ''')
        self.settings_label = QLabel()
        self.settings_label.setStyleSheet('''
                                            background: rgba(6, 6, 6, 0.81);
                                            border-radius:55px;
                                            color:white;
                                            font-size: 64px;''')
        self.settings_label.setText('   НАСТРОЙКИ')
        self.settings_label.setFixedSize(506, 110)
        self.settings_name_layout.addWidget(self.ellipse)
        self.settings_name_layout.addWidget(self.settings_label)
        self.settings_name_widget.move(303, 68)

        self.music_label = QLabel(self.central_widget)
        self.music_label.setText('\n   МУЗЫКА\n')
        self.music_label.setStyleSheet('''
                                        background: rgba(3, 3, 3, 0.08);
                                        border-radius: 70px;
                                        font-size: 62px;
                                        ''')
        self.music_label.setFixedSize(456, 154)
        self.music_label.move(82, 257)
        self.additional_text = QLabel(self.central_widget)
        self.additional_text.setStyleSheet('''font-family: 'Sansation';
                                        font-style: normal;
                                        font-weight: 400;
                                        font-size: 20px;
                            ''')
        self.additional_text.setText('       КОНТРОЛИРУЕТ ФОНОВУЮ\n       МУЗЫКУ')
        self.additional_text.move(92, 357)

        self.add_or_not_widget = QWidget(parent=self.central_widget)
        self.add_or_not_layout = QVBoxLayout()
        self.add_or_not_layout.setSpacing(30)
        self.add_button = QToolButton()
        self.add_button.setText('ДОБАВИТЬ')
        self.add_button.setFixedSize(294, 54)
        self.add_button.setStyleSheet('''
                                        background: rgba(3, 3, 3, 0.68);
                                        border-radius: 27px;
                                        color:white;
                                        font-weight: 400;
                                        font-size: 33px;
                                    ''')
        self.abstract_button = QToolButton()
        self.abstract_button.setFixedSize(294, 54)
        self.abstract_button.setText('УБРАТЬ')
        self.abstract_button.setStyleSheet('''
                                               background: rgba(3, 3, 3, 0.68);
                                               border-radius: 27px;
                                               color:white;
                                               font-size: 33px;
                                            ''')
        self.add_or_not_layout.addWidget(self.add_button)
        self.add_or_not_layout.addWidget(self.abstract_button)
        self.add_or_not_widget.setLayout(self.add_or_not_layout)
        self.add_or_not_widget.move(814, 257)

        self.back_menu_widget = QWidget(self.central_widget)
        self.back_menu = BackMenu()
        self.back_menu.setSpacing(150)
        self.back_menu.setContentsMargins(300, 0, 0, 0)
        self.back_menu_widget.setLayout(self.back_menu)
        self.back_menu_widget.move(855, 799)
