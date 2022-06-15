
if __name__ == '__main__':
    from PyQt5 import QtWidgets
    import sys
    app = QtWidgets.QApplication(sys.argv)  # Конструтирование QApp
    from UI.window_switcher import WindowSwitcher
    window_switcher = WindowSwitcher()
    window_switcher.showFullScreen()  # Создание и показ основного окна на полный экран
    sys.exit(app.exec_())  # Запуск QApp
