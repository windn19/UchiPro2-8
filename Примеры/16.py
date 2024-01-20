import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QDockWidget, QMainWindow, QTextEdit,
                             QLineEdit, QPushButton, QWidget, QVBoxLayout,
                             QLabel)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dock = QDockWidget('Поиск')
        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Введите текст'))
        layout.addWidget(QLineEdit())
        layout.addWidget(QPushButton('Искать'))
        layout.addStretch()
        widget.setLayout(layout)
        self.dock.setWidget(widget)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dock)
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
