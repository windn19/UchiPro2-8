import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Админ панель')
        self.imageLabel = QLabel()
        self.setCentralWidget(self.imageLabel)
        menu = self.menuBar()
        fileMenu = menu.addMenu('Файл')
        fileMenu.addAction('Открыть', self.fileOpen)
        fileMenu.addAction('Очистить', self.imageLabel.clear)

    def fileOpen(self):
        result, ok = QFileDialog.getOpenFileName(self)
        print(result)
        if ok:
            pixmap = QPixmap(result)
            self.imageLabel.setPixmap(pixmap)
            self.imageLabel.resize(pixmap.width(), pixmap.height())


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
