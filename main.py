import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton
from random import randint


class Design(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(650, 420)
        self.btn = QPushButton('Жмякать', self)
        self.btn.move(50, 50)

class Example(Design):
    def __init__(self):
        super().__init__()
        self.flag = False
        self.btn.clicked.connect(self.go_paint)

    def go_paint(self):
        self.qp = QPainter()
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp.begin(self)
            self.draw_flag(self.qp)
            self.qp.end()

    def draw_flag(self, qp):
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        self.qp.setBrush(QColor(r, g, b))
        x, y = randint(0, 650), randint(0, 420)
        d = randint(10, 30)
        self.qp.drawEllipse(x, y, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
