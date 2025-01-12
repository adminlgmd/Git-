import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
from UIproject import Ui_MainWindow
from random import randint
from PyQt6.QtGui import QColor, QPainter


class DrawCircle(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.create_circle.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_circle(self, qp):
        qp.setBrush(QColor(randint(0, 250), randint(0, 250), randint(0, 250)))
        r = randint(0, 250)
        qp.drawEllipse(150, 150, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DrawCircle()
    window.show()
    sys.exit(app.exec())
