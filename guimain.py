import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QFileDialog, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtChart import QChart, QChartView, QLineSeries
import csv

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My App')

        self.widget = QWidget()
        self.layout = QVBoxLayout()
        self.b2 = QPushButton('Graph')
        self.b3 = QPushButton('Table')

        self.layout.addWidget(self.b2)
        self.layout.addWidget(self.b3)

        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        self.b2.clicked.connect(self.generate_graph)
        self.b3.clicked.connect(self.display_table)

        self.chart = QChart()
        self.chart_view = QChartView(self.chart)

        self.table_model = QStandardItemModel()
        self.table_view = QTableView()
        self.table_view.setModel(self.table_model)

    def generate_graph(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open CSV File', '', 'CSV Files (*.csv)')
        if filename:
            data = []
            with open(filename, 'r') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)  # Skip header row
                for row in csv_reader:
                    if len(row) > 1:
                        x = int(row[0])
                        y = float(row[1])  # Convert to float instead of int
                        data.append((x, y))

            series = QLineSeries()
            for x, y in data:
                series.append(x, y)

            self.chart.removeAllSeries()
            self.chart.addSeries(series)
            self.chart.createDefaultAxes()

            self.setCentralWidget(self.chart_view)

    def display_table(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open CSV File', '', 'CSV Files (*.csv)')
        if filename:
            with open(filename, 'r') as file:
                csv_reader = csv.reader(file)
                data = list(csv_reader)

            self.table_model.clear()
            self.table_model.setColumnCount(len(data[0]))
            self.table_model.setRowCount(len(data))

            for row_idx, row_data in enumerate(data):
                for col_idx, col_data in enumerate(row_data):
                    item = QStandardItem(str(col_data))
                    self.table_model.setItem(row_idx, col_idx, item)

            self.table_view.setModel(self.table_model)
            self.setCentralWidget(self.table_view)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
