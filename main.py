import random
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor
from window import Main


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myW = Main()
    myW.show()

    sys.exit(app.exec())