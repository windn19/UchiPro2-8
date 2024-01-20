import sys

from PyQt6.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        menu = self.menuBar()
        menu = menu.addMenu('Файл')
        menu.addAction('Новый', self.test)
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Готов к работе')

    def test(self):
        self.statusbar.showMessage('Новый')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
