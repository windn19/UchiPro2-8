import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        fileToolbar = self.addToolBar('Файл')
        editToolbar = self.addToolBar('Правка')
        fileToolbar.addAction(QIcon('icons/new.png'), 'Новый', self.test)
        fileToolbar.addAction(QIcon('icons/close.png'), 'Закрыть', self.close)
        editToolbar.addAction('Копировать')
        editToolbar.addAction('Вставить')

    def test(self):
        print('test')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
