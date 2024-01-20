import sys

from PyQt6.QtWidgets import QWidget, QApplication, QPushButton


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.button = QPushButton('Кнопка', self)
        self.button.clicked.connect(self.click)

    def click(self):
        self.counter += 1
        self.button.setText(str(self.counter))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
