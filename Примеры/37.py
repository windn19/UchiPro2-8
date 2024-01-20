import sys

from PyQt6.QtWidgets import (QWidget, QApplication, QPushButton, QHBoxLayout,
                             QMessageBox)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        button = QPushButton('Кнопка', self)
        button.clicked.connect(self.closeWindow)
        layout.addWidget(button)
        self.setLayout(layout)

    def closeWindow(self):
        result = QMessageBox().critical(self, 'Закрыть', 'Закрыть окно?')
        if result == QMessageBox.StandardButton.Ok:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
