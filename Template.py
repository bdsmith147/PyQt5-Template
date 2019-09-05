import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui, uic


from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas,
                                                NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)

import random

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('Visualizer.ui', self)
        self.left = 10
        self.top = 10
        self.title = 'PyQt5 matplotlib example - pythonspot.com'
        self.width = 640
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.plot_layout = QVBoxLayout()
        
        m = PlotCanvas(self, width=5, height=4)
        m.move(0,300)

#        button = QPushButton('PyQt5 button', self)
#        button.setToolTip('This s an example button')
#        button.move(500,0)
#        button.resize(140,100)
        self.toolbar = NavigationToolbar(m, self)  
        self.plot_layout.addWidget(m)        
        self.plot_layout.addWidget(self.toolbar)        
        self.gridLayout.addLayout(self.plot_layout, 0, 0, 1, 1)
        self.show()


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()


    def plot(self):
        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-')
        ax.set_title('PyQt Matplotlib Example')
        self.draw()

if __name__ == '__main__':
    def run_app():
        app = QApplication(sys.argv)
        ex = App()
        ex.show()
        app.exec_()
    run_app()