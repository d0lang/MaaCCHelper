from PySide6.QtWidgets import QMainWindow, QPushButton
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt,Signal,Slot
import mcchres.res_rcc
from ui import (mainwindow,framelesswindow)
class MCCHMainWindow(QMainWindow):
    def __init__(self):
        super(MCCHMainWindow, self).__init__()
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":/images/icons/icon.ico"))
        self.setWindowFlag()

class MCCHFrameLessWindow(QMainWindow):

    def __init__(self):
        super(MCCHFrameLessWindow, self).__init__()
        self.ui = framelesswindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_close.clicked.connect(self.click_close)
        self.ui.btn_min.clicked.connect(self.click_min)
        self.ui.btn_max.clicked.connect(self.click_max)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

    @Slot()
    def click_close(self):
        self.close()
    @Slot()
    def click_min(self):
        self.showMinimized()
    @Slot()
    def click_max(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()