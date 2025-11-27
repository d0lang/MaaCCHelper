import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
import sys
from gui import (MCCHWindows,MCCHWidgets)
from PySide6.QtGui import QIcon
import mcchres.res_rcc
from works.link import Linker
def main():
    app = QApplication(sys.argv)
    mainW = MCCHWindows.MCCHFrameLessWindow()
    mainW.setWindowTitle("交错战线小助手")
    mainW.setStatusBar(None)
    startW = MCCHWidgets.MCCHWidgetStart()
    linker = Linker()
    adb_devices = linker.adb_devices
    for device in adb_devices:
        startW.ui.adb_devices.addItem(device.name)
    mainW.centralWidget().layout().addWidget(startW)
    mainW.show()
    app.exec()
if __name__ == "__main__":
    main()