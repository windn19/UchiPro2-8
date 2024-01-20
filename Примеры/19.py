import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        menu = self.menuBar()
        fileMenu = menu.addMenu('Файл')
        editMenu = menu.addMenu('Правка')
        fileMenu.addAction(QIcon('icons/new.png'), 'Новый', self.test)
        fileMenu.addAction(QIcon('icons/close.png'), 'Закрыть', self.close)
        editMenu.addAction('Копировать')
        editMenu.addAction('Вставить')

    def test(self):
        print('test')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
