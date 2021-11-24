import random
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 700, 700, 700)
        self.pushButton = QPushButton('Push', self)
        self.pushButton.move(300, 500)
        self.pushButton.clicked.connect(self.nazh)
        self.proverka = False

    def paintEvent(self, event):
        if self.proverka is True:
            qp = QPainter()
            qp.begin(self)
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            qp.setBrush(QColor(r, g, b))
            a = random.randint(40, 200)
            qp.drawEllipse(280, 180, a, a)
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            qp.setBrush(QColor(r, g, b))
            a = random.randint(40, 200)
            qp.drawEllipse(150, 80, a, a)
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            qp.setBrush(QColor(r, g, b))
            a = random.randint(40, 200)
            qp.drawEllipse(220, 400, a, a)
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            qp.setBrush(QColor(r, g, b))
            a = random.randint(40, 200)
            qp.drawEllipse(500, 20, a, a)
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            qp.setBrush(QColor(r, g, b))
            a = random.randint(40, 200)
            qp.drawEllipse(445, 390, a, a)
            qp.end()

    def nazh(self):
        self.proverka = True
        self.repaint()