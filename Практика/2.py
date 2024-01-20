import sys

from PyQt6.QtWidgets import (QApplication,
                             QInputDialog,
                             QMessageBox,
                             QHBoxLayout,
                             QPushButton,
                             QWidget)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Админ панель')
        self.resize(300, 200)
        self.layout = QHBoxLayout()
        self.login = QPushButton('Авторизоваться', self)
        self.logout = QPushButton('Выход', self)
        self.logout.setEnabled(False)
        self.login.clicked.connect(self.autorization)
        self.logout.clicked.connect(self.exit)
        self.layout.addWidget(self.login)
        self.layout.addWidget(self.logout)
        self.setLayout(self.layout)

    def autorization(self):
        password, ok = QInputDialog.getText(
            self,
            'Введите пароль',
            'Введите пароль'
        )
        if ok and password == '123456':
            QMessageBox.information(
                self,
                'Авторизация выполнена',
                'Авторизация выполнена'
            )
            self.login.setEnabled(False)
            self.logout.setEnabled(True)
        else:
            QMessageBox.critical(
                self,
                'Авторизация не выполнена',
                'Авторизация не выполнена'
            )

    def exit(self):
        QMessageBox.information(
            self,
            'Вы вышли',
            'Вы вышли'
        )
        self.login.setEnabled(True)
        self.logout.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
