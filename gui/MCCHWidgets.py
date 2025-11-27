from PySide6.QtWidgets import QMainWindow, QPushButton,QApplication
from PySide6.QtGui import QIcon,Qt
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt,Signal,Slot
import mcchres.res_rcc
import ui.start
from ui import (start)

class MCCHWidgetStart(QWidget):
    def __init__(self):
        super(MCCHWidgetStart, self).__init__()
        self.ui = ui.start.Ui_Form()
        self.ui.setupUi(self)