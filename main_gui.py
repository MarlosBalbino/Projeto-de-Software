from PySide6 import QtCore
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow
from gui.window.ui_main import Ui_MainWindow
import sys
# import gui.icons.icons_rc


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Projeto de Software - 2021.1")
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)

        # TOGGLE BUTTON
        self.btn_toggle.clicked.connect(self.leftMenu)

        # PÁGINAS DO SISTEMA
        self.btn_home.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_home))
        self.btn_add.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_add))
        self.btn_contacts.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_contats))
        self.btn_about.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_about))

    def leftMenu(self):
        width = self.left_menu.width()  # obtém a máxima largura padrão do menu esquerdo

        if width == 9:
            newWidth = 200
        else:
            newWidth = 9

        # ANIMAÇÃO MENU ESQUERDO
        self.animation = QtCore.QPropertyAnimation(self.left_menu, b"maximumWidth")
        self.animation.setDuration(300)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
        # self.animation.setEasingCurve(QtCore.QEasingCurve.InQuart)
        self.animation.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
