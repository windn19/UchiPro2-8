import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QDockWidget, QWidget,
                             QVBoxLayout, QLabel, QLineEdit, QPushButton,
                             QTextEdit)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Текстовый редактор')
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.setMenu()
        self.setDock()
        self.setToolBar()
        self.statusbar = self.statusBar()

    def setMenu(self):
        menu = self.menuBar()
        fileMenu = menu.addMenu('Файл')
        fileMenu.addAction('Новый', self.textEdit.clear)
        fileMenu.addAction('Закрыть', self.close)

    def setDock(self):
        self.dock = QDockWidget('Поиск')
        widget = QWidget()
        layout = QVBoxLayout()
        self.findText = QLineEdit()
        self.findButton = QPushButton('Искать')
        layout.addWidget(QLabel('Введите текст'))
        layout.addWidget(self.findText)
        layout.addWidget(self.findButton)
        layout.addStretch()
        widget.setLayout(layout)
        self.dock.setWidget(widget)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dock)
        self.findButton.clicked.connect(self.find)

    def setToolBar(self):
        toolbar = self.addToolBar('Правка')
        toolbar.addAction('UPPER', self.changeText)
        toolbar.addAction('lower', self.changeText)

    def find(self):
        findtext = self.findText.text()
        text = self.textEdit.toPlainText()
        result = text.count(findtext)
        self.statusbar.showMessage(f'Найдено {result} совпадений')

    def changeText(self):
        text = self.textEdit.toPlainText()
        if self.sender().text() == 'UPPER':
            self.textEdit.setText(text.upper())
        else:
            self.textEdit.setText(text.lower())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
