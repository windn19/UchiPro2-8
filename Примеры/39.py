import sys

from PyQt6.QtWidgets import (QWidget, QApplication, QPushButton, QHBoxLayout,
                             QInputDialog)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        button = QPushButton('Кнопка', self)
        button.clicked.connect(self.closeWindow)
        layout.addWidget(button)
        self.setLayout(layout)

    def closeWindow(self):
        result, ok = QInputDialog().getDouble(self, 'Имя', "Введите значение")
        if ok:
            print(result)
        else:
            print('Пользователь закрыл окно')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
