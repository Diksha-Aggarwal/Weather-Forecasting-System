import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("map.csv")
df
df.head()
df.info
df.describe()
df.isna().sum()
x = df['HGHT']
y1 = df['TEMP']
y2 = df['PRES']
y3 = df['RELH']
y4 = df['DRCT']
y5 = df['SPED']
# Plot the line graph
plt.plot(x, y1)
plt.xlabel('height')
plt.ylabel('temperature')
plt.title('Line Graph')
plt.savefig('graph1.png')

x = df['HGHT']
y1 = df['TEMP']
# Plot the line graph
plt.plot(x, y1, label='temperature')
plt.plot(x, y2, label='pressure')
plt.plot(x, y3, label='RELH')
plt.plot(x, y4, label='DRCT')
plt.plot(x, y5, label='SPED')
plt.xlabel('height')
plt.title('Line Graph')
plt.legend()
plt.savefig('graph2.png')

# importing pyqtgraph as pg
import pyqtgraph as pg

# importing QtCore and QtGui from the pyqtgraph module
from pyqtgraph.Qt import QtCore, QtGui

# importing numpy as np
import numpy as np

# define the data
title = "Line Graph"

# create plot window object
plt = pg.plot()

# showing x and y grids
plt.showGrid(x = True, y = True)

# adding legend
plt.addLegend()

# set properties of the label for y axis
plt.setLabel('left', 'Vertical Values', units ='y')

# set properties of the label for x axis
plt.setLabel('bottom', 'Horizontal Values', units ='s')

# setting horizontal range
plt.setXRange(1000, 20000)

# setting vertical range
plt.setYRange(0, 40)

# setting window title to the plot window
plt.setWindowTitle(title)

# plotting line in green color
# with dot symbol as x, not a mandatory field
line1 = plt.plot(x, y1, pen ='g', symbol ='x', symbolPen ='g',
						symbolBrush = 0.2, name ='green')

# plotting line2 with blue color
# with dot symbol as o
line2 = plt.plot(x, y2, pen ='b', symbol ='o', symbolPen ='b',
							symbolBrush = 0.2, name ='blue')

if __name__ == '__main__':
	
	# importing system
	import sys
	
	# Start Qt event loop unless running in interactive mode or using
	if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
		QtGui.QGuiApplication.instance().exec()

from PyQt6 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
from random import randint

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        self.x = x  # 100 time points
        self.y = y1  # 100 data points

        self.graphWidget.setBackground('w')

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  self.graphWidget.plot(self.x, self.y, pen=pen)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()
        
    def update_plot_data(self):

        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.

        self.y = self.y[1:]  # Remove the first
        self.y.append( randint(0,100))  # Add a new random value.

        self.data_line.setData(self.x, self.y)  # Update the data.

    def plot_zoom(self):
        # Get the Matplotlib axes object
        ax = self.figure.add_subplot(111)

        # Generate your graph using Matplotlib, for example:
        
        ax.plot(x, y1)

        # Enable zooming functionality
        ax.set_title("Zoomable Graph")
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.set_xlim([min(x), max(x)])
        ax.set_ylim([min(y1), max(y1)])
        ax.autoscale(enable=True)
        self.canvas.draw()    

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())

