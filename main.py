import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
import sys
import pyui.MCCHWindows
from PySide6.QtGui import QIcon
import mcchres.res_rcc
def main():
    app = QApplication(sys.argv)
    mainW = pyui.MCCHWindows.MCCHFrameLessWindow()
    # mainW.setWindowTitle("交错战线小助手")
    mainW.show()
    app.exec()
if __name__ == "__main__":
    main()