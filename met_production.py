import sys
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QTableWidgetItem, QDateTimeEdit, QFileDialog
from PyQt6.QtCore import QDateTime, Qt
from metproduction import Ui_Form
import pandas as pd
import numpy as np
import csv
import datetime
import re
import math 
import random

csv_path = "D:\\DIKSHA\\B.Tech\\IIITD Internship\\aaizel_POC\\RadioSonde_GUI\\gps_data.csv"
output_csv_path = "D:\\DIKSHA\\B.Tech\\IIITD Internship\\aaizel_POC\\RadioSonde_GUI\\values.csv"

class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.save_to_csv()
        self.ui.pushButton.clicked.connect(self.handle_button)
        self.ui.pushButton_2.clicked.connect(self.handle_button_1)
        self.ui.pushButton_3.clicked.connect(self.handle_button_2)
        self.ui.pushButton_4.clicked.connect(self.handle_button_3)
        self.ui.pushButton_5.clicked.connect(self.handle_button_4)
        self.ui.pushButton_6.clicked.connect(self.handle_button_5)
        self.ui.pushButton_8.clicked.connect(self.handle_button6)
        self.ui.pushButton_9.clicked.connect(self.handle_button6)
        self.ui.pushButton_11.clicked.connect(self.handle_button6)
        self.ui.pushButton_10.clicked.connect(self.handle_button6)
        self.ui.pushButton_15.clicked.connect(self.handle_button6)
        self.ui.pushButton_14.clicked.connect(self.handle_button6)
        self.ui.pushButton_13.clicked.connect(self.handle_button6)
        self.ui.pushButton_12.clicked.connect(self.handle_button6)
        self.ui.pushButton_16.clicked.connect(self.handle_button7)

    def process_data(self):
        data_processor = DataProcessor(csv_path)
        data_processor.calculate_variables()
        data_processor.save_to_csv(output_csv_path)
        print("Calculated values saved to CSV successfully.")

    def save_to_csv(self):
        # Specify the output CSV file path

        data = [
            b'B73,42.0H,32.0C,14.0P,174349.00T,1907.897N,07255.014E,\r\n',
            b'B75,42.0H,32.0C,14.0P,174350.00T,1907.897N,07255.014E,\r\n',
            b'B77,42.0H,32.0C,14.0P,174351.00T,1907.897N,07255.014E,\r\n',
            b'B79,42.0H,32.0C,14.0P,174352.00T,1907.897N,07255.015E,\r\n',
            b'B82,42.0H,32.0C,14.0P,174353.00T,1907.897N,07255.015E,\r\n',
            b'B88,42.0H,32.0C,14.0P,174355.00T,1907.897N,07255.016E,\r\n',
            # b'B94,42.0H,32.0C,14.0P,17B01,42.0H,32.0C,14.0P,174359.00T,190P,17\r\n',
            b'B07,42.0H,32.0C,14.0P,174401.00T,1907.897N,07255.017E,\r\n',
            # b'B13,42.0H,32.0C,14.0P,174403.00T,1907.897NB15,42.0H,32B18,425,42\r\n',
            b'B24,42.0H,32.0C,14.0P,174407.00T,1907.897N,07255.017E,\r\n',
            b'B30,42.0H,32.0C,14.0P,174409.00T,1907.898N,07255.017E,\r\n',
            b'B42,42.0H,32.0C,14.0P,174413.00T,1907.898N,07255.017E,\r\n',
            b'B48,42.0H,32.0C,14.0P,174415.00T,1907.898N,07255.017E,\r\n',
            # b'B54,42.0H,32.0C,14B60,42.0H,32.0C,14.0P,174419.00T,1907.898N19.0\r\n',
            b'B66,42.0H,32.0C,14.0P,174421.00T,1907.898N,07255.016E,\r\n',
            # b'B72,42.0H,32.0C,14.0P,174423.0B78,42.0H,32.0C,14.0P,174425.0C,14\r\n',
            b'B84,42.0H,32.0C,14.0P,174427.00T,1907.898N,07255.017E,\r\n',
            # b'B90,41.0H,32.0C,14.0P,174429.00T,1907.898N,07255B96,41.0H,327255\r\n',
            b'B03,41.0H,32.0C,14.0P,174433.00T,1907.898N,07255.017E,\r\n',
            b'B09,41.0H,32.0C,14.0P,174435.00T,1907.898N,07255.017E,\r\n',
            b'B21,41.0H,32.0C,14.0P,174439.00T,1907.899N,07255.018E,\r\n',
            b'B27,41.0H,32.0C,14.0P,174441.00T,1907.899N,07255.018E,\r\n',
            # b'B33,41.0H,32B39,41.0H,32.0C,14.0P,174445.00T,1907.899N,07255,190\r\n',
            b'B45,41.0H,32.0C,14.0P,174447.00T,1907.899N,07255.018E,\r\n',
            # b'B51,41.0H,32B57,41.0H,32.0C,14.0P,174451.00T,1907.900N,07255,190\r\n',
            b'B63,41.0H,32.0C,14.0P,174453.00T,1907.901N,07255.016E,\r\n',
            # b'B69,41.0H,32.0C,14.0P,17B75,41.0H,32.0C,14.0P,174457.00T,190P,17\r\n',
            # b'B83,41.0H,32.0C,14.0P,174500.00T,1907.902N,07255B89,41.0H,327255\r\n',
            b'B95,41.0H,32.0C,14.0P,174504.00T,1907.904N,07255.012E,\r\n',
            b'B02,41.0H,32.0C,14.0P,174506.00T,1907.904N,07255.012E,\r\n',
            b'B14,41.0H,32.0C,14.0P,174510.00T,1907.905N,07255.012E,\r\n',
            b'B20,41.0H,32.0C,14.0P,174512.00T,1907.905N,07255.012E,\r\n',
        ]

        with open(csv_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['B', 'Humidity', 'Temperature', 'Pressure', 'Time', 'Latitude', 'Longitude', 'HGHT', 'NORS', 'EORS'])

            for item in data:
                item_str = item.decode('utf-8')
                values = item_str.strip().split(',')

                b_value = values[0][1:]
                humidity_value = values[1].rstrip('H')
                temperature_value = values[2].rstrip('C')
                pressure_value = values[3].rstrip('P')
                time_value = values[4].rstrip('T')
                latitude_longitude_value = values[5:7]
                hght = 41

                # Extract latitude direction
                latitude_direction = re.findall(r'[NS]', values[5])[0]
                # Strip the latitude value
                latitude_value = re.sub(r'[NS]', '', values[5])

                # Extract longitude direction
                longitude_direction = re.findall(r'[EW]', values[6])[0]
                # Strip the longitude value
                longitude_value = re.sub(r'[EW]', '', values[6])

                writer.writerow([b_value, humidity_value, temperature_value, pressure_value, time_value,
                                 latitude_value, longitude_value, hght, latitude_direction, longitude_direction])

        self.process_data()
        print("Data saved to CSV successfully.")

    def handle_button(self):
        csv_file_path = "D:\\DIKSHA\\B.Tech\\IIITD Internship\\aaizel_POC\\RadioSonde_GUI\\values.csv"
        typeOfFormat = 0
        for_met_instance = ForMet()
        met_data = for_met_instance.getMet(csv_file_path,typeOfFormat)
        self.ui.textEdit_2.setText(met_data)

    def handle_button_1(self):
        csv_file_path = "D:\\DIKSHA\\B.Tech\\IIITD Internship\\aaizel_POC\\RadioSonde_GUI\\values.csv"
        typeOfFormat = 1
        for_met_instance = ForMet()
        met_data = for_met_instance.getMet(csv_file_path,typeOfFormat)
        self.ui.textEdit_2.setText(met_data)

    def handle_button_2(self):
        csv_file_path = "D:\\DIKSHA\\B.Tech\\IIITD Internship\\aaizel_POC\\RadioSonde_GUI\\values.csv"
        typeOfFormat = 2
        for_met_instance = ForMet()
        met_data = for_met_instance.getMet(csv_file_path,typeOfFormat)
        self.ui.textEdit_2.setText(met_data)

    def handle_button_3(self):
        csv_file_path = "D:\\DIKSHA\\B.Tech\\IIITD Internship\\aaizel_POC\\RadioSonde_GUI\\values.csv"
        typeOfFormat = 4
        for_met_instance = ForMet()
        met_data = for_met_instance.getMet(csv_file_path,typeOfFormat)
        self.ui.textEdit_2.setText(met_data)

    def handle_button_4(self):
        csv_file_path = "D:\\DIKSHA\\B.Tech\\IIITD Internship\\aaizel_POC\\RadioSonde_GUI\\values.csv"
        typeOfFormat = 5
        for_met_instance = ForMet()
        met_data = for_met_instance.getMet(csv_file_path,typeOfFormat)
        self.ui.textEdit_2.setText(met_data)

    def handle_button_5(self):
        csv_file_path = "D:\\DIKSHA\\B.Tech\\IIITD Internship\\aaizel_POC\\RadioSonde_GUI\\values.csv"
        typeOfFormat = 6
        for_met_instance = ForMet()
        met_data = for_met_instance.getMet(csv_file_path,typeOfFormat)
        self.ui.textEdit_2.setText(met_data)

    def handle_button6(self):
        sender = self.sender()
        button_text = sender.text()
        
        report_section = ""
        report_type = ""

        if button_text == "AATT":
            report_section = "AA"
            report_type = "TT"
        elif button_text == "BBTT":
            report_section = "BB"
            report_type = "TT"
        elif button_text == "CCTT":
            report_section = "CC"
            report_type = "TT"
        elif button_text == "DDTT":
            report_section = "DD"
            report_type = "TT"
        elif button_text == "AAPP":
            report_section = "AA"
            report_type = "PP"
        elif button_text == "BBPP":
            report_section = "BB"
            report_type = "PP"
        elif button_text == "CCPP":
            report_section = "CC"
            report_type = "PP"
        elif button_text == "DDPP":
            report_section = "DD"
            report_type = "PP"

        for_temp_instance = ForTemp()
        temp_data = for_temp_instance.TEMP_report(report_section, report_type)
        self.ui.textEdit_3.setText(temp_data)

    def handle_button7(self):
        aircraft_id = 'AB123'
        location = '12345'
        observation_time = datetime.datetime.now()
        
        wind_data = [
            {'pressure_level': 1000, 'wind_direction': 270, 'wind_speed': 5},
            {'pressure_level': 925, 'wind_direction': 275, 'wind_speed': 10},
            {'pressure_level': 850, 'wind_direction': 280, 'wind_speed': 15},
            # ... additional wind data points
            ]  
        #metData = reportTab.generate_fm36_v_report(aircraft_id, location, observation_time)
        pilot_instance = ForTemp()
        pilot_data = pilot_instance.generate_fm36_v_report(aircraft_id, location, observation_time)
        self.ui.textEdit_3.setText(pilot_data)

class ForMet():
    def __init__(self):
        pass

    def get_validity(self, hours):
        if (0 <= hours <= 4) or (12 <= hours <= 16):
            return "4"
        return "2"

    def get_octane(self, longitude_oct, eorw_oct, nors_oct):
        temp_oct = float(float(longitude_oct) / 100.0)
        longitude_oct = temp_oct + float(longitude_oct) % 100.0 / 60.0
        if 0.0 <= longitude_oct <= 90.0:
            if eorw_oct == 'W' and nors_oct == 'N':
                return "0"
            if eorw_oct == 'W' and nors_oct == 'S':
                return "5"
            if eorw_oct == 'E' and nors_oct == 'N':
                return "3"
            if eorw_oct == 'E' and nors_oct == 'S':
                return "8"
        elif 90.0 <= longitude_oct <= 180.0:
            if eorw_oct == 'W' and nors_oct == 'N':
                return "1"
            if eorw_oct == 'W' and nors_oct == 'S':
                return "6"
            if eorw_oct == 'E' and nors_oct == 'N':
                return "2"
            if eorw_oct == 'E' and nors_oct == 'S':
                return "7"
        return "9"

    def getMet(self, csv_file_path, typemap):

        standardTemperatureK = [287.5, 287.5, 285.88, 283.28, 280.03, 276.78, 271.9, 265.4, 258.9, 252.4, 242.65, 229.65, 218.28, 216.65, 216.65, 216.65]
        lineNo = [ "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]#, "24", "25", "26" ]
        standardDensity = [1.2133, 1.2133, 1.1844, 1.1392, 1.0846, 1.032, 0.9569, 0.8632, 0.7768, 0.6971, 0.5895, 0.4664, 0.3612, 0.2655, 0.1937, 0.1413]


        heightMtrs = [
            [0.0, 200.0, 500.0, 1000.0, 1500.0, 2000.0, 2500.0, 3000.0, 3500.0, 4000.0, 4500.0, 5000.0, 6000.0, 7000.0, 8000.0, 9000.0, 10000.0, 11000.0, 12000.0, 13000.0, 14000.0, 15000.0, 16000.0, 17000.0, 18000.0, 19000.0, 20000.0],
            [0.0, 200.0, 500.0, 1000.0, 1500.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 8000.0, 10000.0, 12000.0, 14000.0, 16000.0, 18000.0],
            [0.0, 200.0, 500.0, 1000.0, 1500.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 8000.0, 10000.0, 12000.0, 14000.0, 16000.0, 18000.0],
            [0.0, 50.0, 100.0, 200.0, 300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0, 1100.0, 1200.0, 1300.0, 1400.0, 1500.0, 1600.0],
            [0.0, 2000.0, 4000.0, 6000.0, 8000.0, 10000.0, 12000.0, 14000.0, 16000.0, 18000.0, 20000.0, 22000.0, 24000.0, 26000.0, 28000.0, 30000.0],
            [0.0, 500.0, 700.0, 1400.0, 2100.0, 28000.0]
        ]

        meanWindWeightingFactorsMETB2 = [
            [1.0, 0.5, 0.29, 0.18, 0.13, 0.08, 0.07, 0.04, 0.04, 0.03, 0.02, 0.03, 0.02, 0.02, 0.01],
            [0.5, 0.33, 0.23, 0.18, 0.12, 0.08, 0.08, 0.06, 0.04, 0.04, 0.04, 0.04, 0.04, 0.03],
            [0.38, 0.39, 0.31, 0.22, 0.16, 0.13, 0.11, 0.08, 0.06, 0.07, 0.05, 0.05, 0.05],
            [0.2, 0.27, 0.2, 0.15, 0.12, 0.1, 0.08, 0.07, 0.07, 0.06, 0.06, 0.04],
            [0.11, 0.19, 0.16, 0.13, 0.1, 0.08, 0.06, 0.07, 0.06, 0.04, 0.05],
            [0.19, 0.27, 0.24, 0.21, 0.16, 0.13, 0.11, 0.11, 0.09, 0.09],
            [0.11, 0.18, 0.2, 0.15, 0.13, 0.11, 0.1, 0.1, 0.1],
            [0.12, 0.18, 0.16, 0.15, 0.13, 0.12, 0.11, 0.11],
            [0.09, 0.16, 0.15, 0.14, 0.12, 0.12, 0.11],
            [0.07, 0.14, 0.14, 0.12, 0.12, 0.11],
            [0.11, 0.17, 0.18, 0.16, 0.15],
            [0.08, 0.15, 0.15, 0.14],
            [0.07, 0.13, 0.14],
            [0.06, 0.11],
            [0.05]
        ]

        meanTempWeightingFactorsMETB2 = [
            [1.0, 0.63, 0.37, 0.25, 0.2, 0.13, 0.1, 0.09, 0.07, 0.05, 0.05, 0.04, 0.05, 0.05, 0.05],
            [0.37, 0.37, 0.3, 0.24, 0.19, 0.14, 0.1, 0.09, 0.08, 0.06, 0.06, 0.06, 0.06, 0.06],
            [0.26, 0.35, 0.3, 0.24, 0.2, 0.17, 0.14, 0.12, 0.1, 0.1, 0.11, 0.11, 0.11],
            [0.1, 0.18, 0.18, 0.16, 0.15, 0.13, 0.1, 0.09, 0.08, 0.09, 0.09, 0.09],
            [0.08, 0.14, 0.14, 0.14, 0.12, 0.1, 0.08, 0.08, 0.08, 0.08, 0.08],
            [0.12, 0.19, 0.2, 0.19, 0.17, 0.15, 0.14, 0.16, 0.16, 0.16],
            [0.07, 0.12, 0.15, 0.14, 0.13, 0.13, 0.12, 0.12, 0.12],
            [0.04, 0.08, 0.1, 0.12, 0.11, 0.13, 0.13, 0.13],
            [0.03, 0.08, 0.1, 0.1, 0.11, 0.11, 0.11],
            [0.06, 0.12, 0.16, 0.1, 0.1, 0.1],
            [0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0],
            [0.0, 0.0],
            [0.0]
        ]

        meanWindWeightingFactorsMETB3 = [
            [1.0, 0.2, 0.09, 0.06, 0.04, 0.03, 0.02, 0.02, 0.02, 0.01, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.8, 0.19, 0.12, 0.08, 0.05, 0.03, 0.02, 0.02, 0.02, 0.0, 0.01, 0.01, 0.01, 0.01],
            [0.72, 0.26, 0.15, 0.08, 0.07, 0.06, 0.05, 0.02, 0.01, 0.01, 0.01, 0.01, 0.01],
            [0.56, 0.2, 0.09, 0.07, 0.06, 0.05, 0.04, 0.04, 0.02, 0.01, 0.01, 0.01],
            [0.53, 0.12, 0.08, 0.06, 0.05, 0.03, 0.03, 0.04, 0.03, 0.02, 0.02],
            [0.63, 0.2, 0.14, 0.12, 0.07, 0.08, 0.07, 0.07, 0.07, 0.07],
            [0.53, 0.19, 0.13, 0.08, 0.08, 0.07, 0.07, 0.07, 0.07],
            [0.45, 0.2, 0.09, 0.09, 0.07, 0.07, 0.07, 0.07],
            [0.36, 0.09, 0.09, 0.08, 0.07, 0.07, 0.07],
            [0.55, 0.2, 0.17, 0.15, 0.13, 0.12],
            [0.38, 0.16, 0.16, 0.13, 0.12],
            [0.3, 0.13, 0.13, 0.11],
            [0.24, 0.1, 0.1],
            [0.18, 0.08],
            [0.14]
        ]

        meanWindWeightingFactorsMETB3 = [ [ 1.0, 0.2, 0.09, 0.06, 0.04, 0.03, 0.02, 0.02, 0.02, 0.01, 0.0, 0.0, 0.0, 0.0, 0.0 ], [ 0.8, 0.19, 0.12, 0.08, 0.05, 0.03, 0.02, 0.02, 0.02, 0.0, 0.01, 0.01, 0.01, 0.01 ], [ 0.72, 0.26, 0.15, 0.08, 0.07, 0.06, 0.05, 0.02, 0.01, 0.01, 0.01, 0.01, 0.01 ], [ 0.56, 0.2, 0.09, 0.07, 0.06, 0.05, 0.04, 0.04, 0.02, 0.01, 0.01, 0.01 ], [ 0.53, 0.12, 0.08, 0.06, 0.05, 0.03, 0.03, 0.04, 0.03, 0.02, 0.02 ], [ 0.63, 0.2, 0.14, 0.12, 0.07, 0.08, 0.07, 0.07, 0.07, 0.07 ], [ 0.53, 0.19, 0.13, 0.08, 0.08, 0.07, 0.07, 0.07, 0.07 ], [ 0.45, 0.2, 0.09, 0.09, 0.07, 0.07, 0.07, 0.07 ], [ 0.36, 0.09, 0.09, 0.08, 0.07, 0.07, 0.07 ], [ 0.55, 0.2, 0.17, 0.15, 0.13, 0.12 ], [ 0.38, 0.16, 0.16, 0.13, 0.12 ], [ 0.3, 0.13, 0.13, 0.11 ], [ 0.24, 0.1, 0.1 ], [ 0.18, 0.08 ], [ 0.14 ] ]
        meanTempWeightingFactorsMETB3 = [ [ 1.0, 0.27, 0.13, 0.08, 0.05, 0.04, 0.02, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01 ], [ 0.73, 0.2, 0.12, 0.1, 0.04, 0.04, 0.03, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01 ], [ 0.67, 0.25, 0.2, 0.09, 0.07, 0.05, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02 ], [ 0.55, 0.21, 0.11, 0.09, 0.04, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03 ], [ 0.44, 0.13, 0.11, 0.1, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03 ], [ 0.59, 0.26, 0.19, 0.09, 0.09, 0.09, 0.09, 0.09, 0.09, 0.09 ], [ 0.41, 0.23, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13 ], [ 0.35, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24 ], [ 0.44, 0.44, 0.44, 0.44, 0.44, 0.44, 0.44 ], [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ], [ 0.0, 0.0, 0.0, 0.0, 0.0 ], [ 0.0, 0.0, 0.0, 0.0 ], [ 0.0, 0.0, 0.0 ], [ 0.0, 0.0 ], [ 0.0 ] ]
        weightingFactorsWindCalculationsMETSR =  [ [ 0.2, 0.4, 0.0, 0.0 ], [ 0.5, 0.0, 1.0, 0.0 ], [ 0.15, 0.3, 0.0, 1.0 ], [ 0.075, 0.15, 0.0, 0.0 ], [ 0.075, 0.15, 0.0, 0.0 ] ]

        geographicDataFiltered = []
        filename = output_csv_path
        with open(filename, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            samples = []
            for row in reader:
                sample = {
                    "Latitude": row["Latitude"],
                    "Longitude": row["Longitude"],
                    "Altitude": row["HGHT"],
                    "eOrw": row["EORS"],
                    "nOrs": row["NORS"],
                    "Date": datetime.datetime.strftime(datetime.datetime.now(), "%d/%H/%M"),
                    "Course": row["DRCT"],
                    "Speed": row["SPED"],
                    "BrdTemp": row["Temperature"],
                    "Pressure": row["Pressure"]
                }
                samples.append(sample)

        geographicDataFiltered.append(samples)
        new_line = "\n"
        format = ""
        Lat = 0.0
        Long = 0.0
        altitude = 0.0
        eorw = ""
        nors = ""
        octant = ""
        validity = ""
        windDrn = 0.0
        windSpeed = 0.0
        tempKelvin = 0.0
        pressure = 0.0
        LatDD = 0.0
        LatMM = 0.0
        LongDD = 0.0
        LongMM = 0.0
        LatStr = ""
        LongStr = ""
        altitudeStr = ""
        header = ""
        body = ""
        # space = " "
        type = typemap
        if type == 0:
            format = "METCM"
            # print(">>> GEWO  DATA>>>>> ", geographicDataFiltered[0][0])
            Lat = geographicDataFiltered[0][0]['Latitude']
            Long = geographicDataFiltered[0][0]['Longitude']
            altitude = geographicDataFiltered[0][0]['Altitude']
            pressureMdp = geographicDataFiltered[0][0]['Pressure']
            eorw = geographicDataFiltered[0][0]['eOrw']
            nors = geographicDataFiltered[0][0]['nOrs']
            octant = self.get_octane(Long, eorw, nors)
            date = geographicDataFiltered[0][0]['Date']
            today = date
            day, time, minutes = today.split("/")
            beginMM = int(minutes)
            beginMM /= 6
            minutes = str(beginMM)
            time = str(time)
            begining = time + minutes
            validity = self.get_validity(float(time))
            windDrn = geographicDataFiltered[0][0]['Course']
            windSpeed = geographicDataFiltered[0][0]['Speed']
            tempKelvin = geographicDataFiltered[0][0]['BrdTemp']
            pressure = geographicDataFiltered[0][0]['Pressure']
            Lat = float(Lat)
            Long = float(Long)
            altitude = float(altitude)
            LatDD = float(Lat / 100)
            LatMM = round(Lat % 100.0 / 6.0)
            Lat = float(LatDD * 10 + LatMM)
            LongDD = float(Long / 100)
            LongMM = round(Long % 100.0 / 6.0)
            Long = LongDD * 10.0 + LongMM
            LatStr = str(int(Lat))
            LongStr = str(int(Long))
            altMts = float(altitude)
            altMts = round(altitude) / 10
            presMb = float(pressureMdp)
            presMb = round(presMb) / 10
            pressureMdpStr = "{:.3f}".format(presMb)
            altitudeStr = "{:.3f}".format(altMts)
            header = format + octant + LatStr + LongStr + new_line + day + begining + validity + altitudeStr + pressureMdpStr
            body = header + new_line
            for k in range(len(heightMtrs[0])):
                try:
                    windDrn = geographicDataFiltered[0][k]['Course']
                    windSpeed = geographicDataFiltered[0][k]['Speed']
                    tempKelvin = geographicDataFiltered[0][k]['BrdTemp']
                    pressure = geographicDataFiltered[0][k]['Pressure']
                except Exception as e:
                    continue
                windDrn = float(windDrn) * 17.777777778
                windDrn = float(windDrn) / 10.0
                windSpeed = round(float(windSpeed))
                tempKelvin = float(tempKelvin) + 273.15
                tempKelvin = float(tempKelvin * 10.0)
                presZoneMb = float(pressure)
                presZoneMb = round(presZoneMb)
                body += lineNo[k] + "{:.3f}".format(windDrn) + "{:.3f}".format(windSpeed) + str(tempKelvin) + "{:.4f}".format(presZoneMb) + new_line
            return body

        elif type == 1:
            format = "METB2"
            try:
                # print(">>>GEWO  DATA>>>>> ", geographicDataFiltered[0][0])
                try:
                    Lat = geographicDataFiltered[0][0]['Latitude']
                    Long = geographicDataFiltered[0][0]['Longitude']
                except:
                    Lat = 0
                    Long = 0
                try:
                    altitude = geographicDataFiltered[0][0]['Altitude']
                except:
                    altitude = 100
                pressureMdp = geographicDataFiltered[0][0]['Pressure']
                eorw = geographicDataFiltered[0][0]['eOrw']
                nors = geographicDataFiltered[0][0]['nOrs']
                octant = self.get_octane(Long, eorw, nors)
                date = geographicDataFiltered[0][0]['Date']
                today = date
                day, time, minutes = today.split("/")
                beginMM = float(minutes)
                begining = time + minutes
                beginMM /= 6
                minutes = str(minutes)
                time = str(time)
                begining = time + minutes
                # print("--------------latdd ", today)
                validity = self.get_validity(float(time))
                try:
                    windDrn = geographicDataFiltered[0][0]['Course']
                except:
                    windDrn = 0
                try:
                    windSpeed = geographicDataFiltered[0][0]['Speed']
                    tempKelvin = geographicDataFiltered[0][0]['BrdTemp']
                    pressure = geographicDataFiltered[0][0]['Pressure']
                except:
                    windSpeed = 0
                    tempKelvin = 0
                    pressure = 0
                # print(">>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<< all     good")
                # print("CHECK ERROR ", float(float(Lat) / 100))
                Lat = float(Lat)
                Long = float(Long)
                altitude = float(altitude)
                LatDD = float(Lat / 100)
                LatMM = round(Lat % 100.0 / 6.0)
                Lat = float(LatDD * 10 + LatMM)
                LongDD = float(Long / 100)
                LongMM = round(Long % 100.0 / 6.0)
                Long = float(LongDD * 10.0 + LongMM)
                altMts = float(altitude)
                altMts = round(altMts) / 10
                LatStr = str(float(Lat))
                LongStr = str(float(Long))
                pressureMdp = float(pressureMdp)
                presMb = float(pressureMdp / 1013.25 * 100.0)
                if presMb > 100.0:
                    presMb %= 100.0
                presMb = round(presMb)
                altMts = float(altMts)
                presMb = float(presMb)
                altitudeStr = "{:.3f}".format(altMts)
                pressureMdpStr = "{:.3f}".format(presMb)
                header = format + octant + LatStr + LongStr + new_line + day + begining + validity + altitudeStr + pressureMdpStr
                body = header + new_line
                for k in range(15): # only works with 15 as values are 15 in the meanWindWeightingFactorsMETB2
                    try:
                        pressure = geographicDataFiltered[0][k]['Pressure']
                    except Exception as e:
                        continue
                    tempKelvinWeighted = 0.0
                    windSpeedWeighted = 0.0
                    windDrnWeighted = 0.0
                    zNo = k - 1
                    lNo = 0
                    l = 0
                    if k <= 1:
                        tempKelvin = geographicDataFiltered[0][k]['BrdTemp']
                        tempKelvin = float(tempKelvin)
                        tempKelvin += 273.15
                        tempKelvin /= standardTemperatureK[k]
                        if tempKelvin >= 100.0:
                            tempKelvin %= 100.0
                        tempKelvin = round(tempKelvin * 10.0)
                        windSpeed = geographicDataFiltered[0][k]['Speed']
                        windSpeed = float(windSpeed)
                        windSpeed = round(windSpeed)
                        if windSpeed >= 100.0:
                            windSpeed = 99.0
                        windDrn = geographicDataFiltered[0][k]['Course']
                        windDrn = float(windDrn) * 17.777777778
                        windDrn /= 100.0
                        windDrn = round(windDrn)
                    else:
                        for l in range(k, 0, -1):
                            try:
                                tempKelvin = geographicDataFiltered[0][k]['BrdTemp']
                                tempKelvin = float(tempKelvin)
                                windSpeed = geographicDataFiltered[0][k]['Speed']
                                windDrn = geographicDataFiltered[0][k]['Course']
                                windSpeed = float(windSpeed)
                                windDrn = float(windDrn)
                            except Exception as e:
                                print("Error message:", str(e))
                                print("METB2 previous data fetch error")
                            try:
                                tempKelvin *= meanTempWeightingFactorsMETB2[zNo][lNo]
                                windSpeed *= meanWindWeightingFactorsMETB2[zNo][lNo]
                                windDrn *= meanWindWeightingFactorsMETB2[zNo][lNo]
                                zNo -= 1
                                lNo += 1
                            except Exception as e:
                                print(e)
                                print("Error message:", str(e))
                                print("METB2 Error in fetching weights")
                            tempKelvinWeighted += tempKelvin
                            windSpeedWeighted += windSpeed
                            windDrnWeighted += windDrn
                        tempKelvin = tempKelvinWeighted
                        windSpeed = windSpeedWeighted
                        windDrn = windDrnWeighted
                        tempKelvin = float(tempKelvin)
                        tempKelvin += 273.15
                        tempKelvin *= 100.0
                        tempKelvin /= standardTemperatureK[zNo + 1]
                        if tempKelvin >= 100.0:
                            tempKelvin %= 100.0
                        tempKelvin = round(tempKelvin * 10.0)
                        windSpeed = float(windSpeed)
                        windSpeed = round(windSpeed)
                        if windSpeed >= 100.0:
                            windSpeed = 99.0
                        windDrn = float(windDrn) * 17.777777778
                        windDrn /= 100.0
                        windDrn = round(windDrn)
                    pressure = geographicDataFiltered[0][k]['Pressure']
                    presZoneMb = float(pressure)
                    presZoneMb = round(presZoneMb)
                    pressureStr = "{:.4f}".format(presZoneMb)
                    conversionFactor = [1.0, 0.99, 0.98, 0.96, 0.94, 0.92, 0.88, 0.83, 0.79, 0.75, 0.67, 0.59, 0.52, 0.43, 0.36, 0.3]
                    ballisticDensity = float(presMb - (tempKelvin - 1000.0) * conversionFactor[k])
                    ballisticDensity *= 100.0
                    ballisticDensity /= standardDensity[k]
                    if ballisticDensity > 100.0:
                        ballisticDensity %= 100.0
                    ballisticDensity = round(ballisticDensity * 10.0)
                    ballisticDensity = str(ballisticDensity)
                    body += lineNo[k] + "{:.3f}".format(float(windDrn)) + "{:.3f}".format(float(windSpeed)) + "{:.3f}".format(
                        float(tempKelvin)) + "{:.3f}".format(float(ballisticDensity)) + new_line
                return body
            except Exception as e:
                print(e)
                print("Please select a different date and time. Data not found. 1")

        elif type == 2:
            format = "METB3"
            # print(geographicDataFiltered[0][0])
            try:
                try:
                    Lat = geographicDataFiltered[0][0]['Latitude']
                    Long = geographicDataFiltered[0][0]['Longitude']
                except:
                    Lat = 0
                    Long = 0
                try:
                    altitude = geographicDataFiltered[0][0]['Altitude']
                except:
                    altitude = 100
                pressureMdp = geographicDataFiltered[0][0]['Pressure']
                eorw = geographicDataFiltered[0][0]['eOrw']
                nors = geographicDataFiltered[0][0]['nOrs']
                octant = self.get_octane(Long, eorw, nors)
                date = geographicDataFiltered[0][0]['Date']
                today = date
                day, time, minutes = today.split("/")
                beginMM = float(minutes)
                begining = time + minutes
                beginMM /= 6
                minutes = str(minutes)
                time = str(time)
                begining = time + minutes
                validity = self.get_validity(float(time[0]))
                try:
                    windDrn = geographicDataFiltered[0][0]['Course']
                except:
                    windDrn = 0
                try:
                    windSpeed = geographicDataFiltered[0][0]['Speed']
                    tempKelvin = geographicDataFiltered[0][0]['BrdTemp']
                    pressure = geographicDataFiltered[0][0]['Pressure']
                except:
                    windSpeed = 0
                    tempKelvin = 0
                    pressure = 0
                Lat = float(Lat)
                Long = float(Long)
                altitude = float(altitude)
                pressureMdp = float(pressureMdp)
                LatDD = Lat
                LatDD = float(LatDD / 100)
                LatMM = round(Lat % 100.0 / 6.0)
                Lat = float(LatDD * 10 + LatMM)
                LongDD = Long
                LongDD = float(LongDD / 100)
                LongMM = round(Long % 100.0 / 6.0)
                Long = LongDD * 10.0 + LongMM
                altMts = altitude
                altMts = float(altitude) / 10
                presMb = pressureMdp / 1013.25 * 100.0
                if presMb > 100.0:
                    presMb %= 100.0
                presMb = round(presMb)
                LatStr = str(float(Lat))
                LongStr = str(float(Long))
                altitudeStr = "{:.3f}".format(altMts)
                pressureMdpStr = "{:.3f}".format(presMb)
                header = format + octant + LatStr + LongStr + new_line + day + begining + validity + altitudeStr + pressureMdpStr
                body = header + new_line
                for k in range(15):
                    try:
                        pressure = geographicDataFiltered[0][k]['Pressure']
                    except Exception as e5:
                        print("Exception: ", str(e5))
                    # print("B# HERE")
                    tempKelvinWeighted = 0.0
                    windSpeedWeighted = 0.0
                    windDrnWeighted = 0.0
                    zNo = k - 1
                    lNo = 0
                    l = 0
                    if k<= 1:
                        tempKelvin = geographicDataFiltered[0][k]['BrdTemp']
                        tempKelvin = float(tempKelvin)
                        tempKelvin += 273.15
                        tempKelvin *= 100.0
                        tempKelvin = standardTemperatureK[k]
                        if tempKelvin > 100.0:
                            tempKelvin %= 100.0
                        # print("B# HERE", "44")
                        tempKelvin = round(tempKelvin * 10.0)
                        windSpeed = geographicDataFiltered[0][k]['Speed']
                        windSpeed = float(windSpeed)
                        if windSpeed >= 100.0:
                            windSpeed = 99.0
                        windDrn = geographicDataFiltered[0][k]['Course']
                        windDrn = float(windDrn)
                        windDrn *= 17.777777778
                        windDrn /= 100.0
                        windDrn = round(windDrn)
                        # print("HERE 3")
                    else:
                        for l in range(k, 0, -1):
                            try:
                                tempKelvin = geographicDataFiltered[0][k]['BrdTemp']
                                tempKelvin = float(tempKelvin)
                                windSpeed = geographicDataFiltered[0][k]['Speed']
                                windDrn = geographicDataFiltered[0][k]['Course']
                                windSpeed = float(windSpeed)
                                windDrn = float(windDrn)
                            except Exception as e2:
                                print("METB3 previous data fetch error",str(e2))
                            try:
                                tempKelvin *= meanTempWeightingFactorsMETB3[zNo][lNo]
                                windSpeed *= meanWindWeightingFactorsMETB3[zNo][lNo]
                                windDrn *= meanWindWeightingFactorsMETB3[zNo][lNo]
                                zNo -= 1
                                lNo += 1
                            except Exception as e2:
                                print("METB3 Error in fetching weights:", e2)
                            tempKelvinWeighted += tempKelvin
                            windSpeedWeighted += windSpeed
                            windDrnWeighted += windDrn
                        # print("B# HERE", "33")
                        tempKelvin = tempKelvinWeighted
                        windSpeed = windSpeedWeighted
                        windDrn = windDrnWeighted
                        tempKelvin += 273.15
                        tempKelvin *= 100.0
                        tempKelvin /= standardTemperatureK[zNo + 1]
                        if tempKelvin >= 100.0:
                            tempKelvin %= 100.0
                        tempKelvin = float(tempKelvin * 10.0)
                        windSpeed = float(windSpeed)
                        if windSpeed >= 100.0:
                            windSpeed = 99.0
                        windDrn *= 17.777777778
                        windDrn /= 100.0
                        windDrn = float(windDrn)
                    presZoneMb = float(pressure)
                    presZoneMb = round(presZoneMb)
                    windDrnStr = "{:.2f}".format(windDrn)
                    windSpeedStr = "{:.2f}".format(windSpeed)
                    tempKelvinStr = "{:.3f}".format(tempKelvin)
                    pressureStr = "{:.4f}".format(presZoneMb)
                    conversionFactor = [1.0, 0.99, 0.98, 0.96, 0.94, 0.92, 0.88, 0.83, 0.79, 0.75, 0.67, 0.59, 0.52, 0.43, 0.36, 0.3]
                    ballisticDensity = float(presMb - (tempKelvin - 1000.0) * conversionFactor[k])
                    ballisticDensity *= 100.0
                    ballisticDensity /= standardDensity[k]
                    if ballisticDensity > 100.0:
                        ballisticDensity %= 100.0
                    ballisticDensity = round(ballisticDensity * 10.0)
                    ballisticDensity = str(ballisticDensity)
                    # print("HERE 2")
                    body += lineNo[k] + "{:.3f}".format(float(windDrn)) + "{:.3f}".format(float(windSpeed)) + "{:.3f}".format(
                        float(tempKelvin)) + "{:.3f}".format(float(ballisticDensity)) + new_line
                # print(body)
                return body
            except Exception as e:
                print(str(e))

        elif type == 4:
            format = "METFM"
            # print(geographicDataFiltered[0][0])
            try:
                try:
                    Lat = geographicDataFiltered[0][0]['Latitude']
                    Long = geographicDataFiltered[0][0]['Longitude']
                except:
                    Lat = 0
                    Long = 0
                try:
                    altitude = geographicDataFiltered[0][0]['Altitude']
                except:
                    altitude = 100
                pressureMdp = geographicDataFiltered[0][0]['Pressure']
                eorw = geographicDataFiltered[0][0]['eOrw']
                nors = geographicDataFiltered[0][0]['nOrs']
                octant = self.get_octane(Long, eorw, nors)
                date = geographicDataFiltered[0][0]['Date']
                today = date
                day, time, minutes = today.split("/")
                beginMM = float(minutes)
                begining = time + minutes
                beginMM /= 6
                minutes = str(minutes)
                time = str(time)
                begining = time + minutes
                validity = self.get_validity(float(time[0]))
                Lat = float(Lat)
                Long = float(Long)
                altitude = float(altitude)
                # pressureMdp = float(pressureMdp)
                LatDD = Lat
                LatDD = float(LatDD / 100)
                LatMM = round(Lat % 100.0 / 6.0)
                Lat = float(LatDD * 10 + LatMM)
                LongDD = Long
                LongDD = float(LongDD / 100)
                LongMM = round(Long % 100.0 / 6.0)
                Long = LongDD * 10.0 + LongMM
                altMts = altitude
                altMts = round(float(altitude) / 10)
                LatStr = str(float(Lat))
                LongStr = str(float(Long))
                altitudeStr = "{:.3f}".format(altMts)
                header = format + octant + new_line + LatStr + LongStr + new_line + day + begining + validity + new_line + altitudeStr
                body = header + new_line
                # print("BODYYYY  ", body)
                for k in range(len(heightMtrs[4])):
                    try:
                        windDrn = float(geographicDataFiltered[0][k]['Course'])
                        windDrn = float(windDrn)
                        windSpeed = float(geographicDataFiltered[0][k]['Speed'])
                        windSpeed = float(windSpeed)
                    except Exception as e5:
                        #print("exception ", e5)
                        continue
                    windDrn *= 17.777777778
                    windDrn /= 10.0
                    windSpeed = round(windSpeed)
                    windDrnStr = "{:.3f}".format(windDrn)
                    windSpeedStr = "{:.3f}".format(windSpeed)
                    body += lineNo[k] + windDrnStr + windSpeedStr + new_line
                # print(body)
                return body
            except Exception as e:
                print(e)
                print("Please select different date and time.", "Data not found ", 1)

        elif type == 5:
            format = "METSR"
            try:
                try:
                    Lat = geographicDataFiltered[0][0]['Latitude']
                    Long = geographicDataFiltered[0][0]['Longitude']
                except:
                    Lat = 0
                    Long = 0
                try:
                    altitude = geographicDataFiltered[0][0]['Altitude']
                except:
                    altitude = 100

                pressureMdp = float(geographicDataFiltered[0][0]['Pressure'])
                eorw = geographicDataFiltered[0][0]['eOrw']
                nors = geographicDataFiltered[0][0]['nOrs']
                octant = self.get_octane(Long, eorw, nors)
                date = geographicDataFiltered[0][0]['Date']


                today = date


                day, time, _ = today.split("/")
                beginMM = float(time)
                day = day

                begining = str(float(time)) # + str(float(time[1]))
                beginMM /= 6
                time = str(float(beginMM))
                day = day
                begining = str(float(time))  #+ str(float(time[1]))
                validity = self.get_validity(float(time))
                try:
                    windDrn = float(geographicDataFiltered[0][0]['Course'])
                except:
                    windDrn

                try:
                    windSpeed = float(geographicDataFiltered[0][0]['Speed'])
                    tempKelvin =float( geographicDataFiltered[0][0]['BrdTemp'])
                    pressure = float(geographicDataFiltered[0][0]['Pressure'])
                except:
                    windSpeed = 0
                    tempKelvin = 0
                    pressure = 0

                Lat = float(Lat)
                Long = float(Long)
                altitude = float(altitude)

                LatDD = Lat
                LatDD = float(LatDD / 100)
                LatMM = round(Lat % 100.0 / 6.0)
                Lat = float(LatDD * 10 + LatMM)
                LongDD = Long
                LongDD = float(LongDD / 100)
                LongMM = round(Long % 100.0 / 6.0)
                Long = LongDD * 10.0 + LongMM
                LatStr = str(float(Lat))
                LongStr = str(float(Long))
                windSpeedL0 = float(geographicDataFiltered[0][0]['Speed'])
                windSpeedL2 = float(geographicDataFiltered[0][0]['Speed'])
                windSpeedL3 = float(geographicDataFiltered[0][0]['Speed'])
                setNo = 0

                if windSpeedL3 >= windSpeedL2 and windSpeedL3 <= 2.0 * windSpeedL2:
                    setNo = 0
                elif windSpeedL3 > 2.0 * windSpeedL2:
                    setNo = 1
                elif windSpeedL3 < windSpeedL2 and math.fabs((windSpeedL3 - windSpeedL0) * 3.28084) < 3.0:
                    setNo = 2
                else:
                    setNo = 3
                numOfReadings = 5.0

                for j in range(6):
                    print("ALLLLLLLLLLLLLLLLLLLLLLLLLLL GOOODDDD  ")
                    try:
                        if j != 1:
                            windDrn += geographicDataFiltered[0][j]['Course'] * weightingFactorsWindCalculationsMETSR[j][setNo]
                        windSpeed += geographicDataFiltered[0][j]['Speed'] * weightingFactorsWindCalculationsMETSR[j][setNo]
                    except Exception as e2:
                        numOfReadings -= 1
                        if numOfReadings == 0.0:
                            print( "0000 reading", e2)
                    if windDrn > 360.0:
                        windDrn -= 360.0
                meanWindDrn = "{:.3f}".format(windDrn / numOfReadings)
                tempKelvin =  float(geographicDataFiltered[0][0]['BrdTemp'])
                virtualTemp = tempKelvin * 9.0 / 5.0 + 32.0
                if virtualTemp < 0.0:
                    virtualTemp += 500.0
                virtualTempStr = "{:.3f}".format(virtualTemp)
                weightedWindSpeed = "{:.3f}".format(windSpeed)
                header = format + octant + " " + LatStr + LongStr + " " + day + begining + validity + " " + meanWindDrn + " " + weightedWindSpeed + " " + virtualTempStr
                body = header + new_line
                # print(body)
                return body
            except Exception as e:
                print( "Please select different date and time.", "Data not found", e)

        elif type == 6:
            format = "METTA"

            try:
                try:
                    Lat = geographicDataFiltered[0][0]['Latitude']
                    Long = geographicDataFiltered[0][0]['Longitude']
                except:
                    Lat = 0
                    Long = 0
                try:
                    altitude = geographicDataFiltered[0][0]['Altitude']
                except:
                    altitude = 100

                pressureMdp = geographicDataFiltered[0][0]['Pressure']
                eorw = geographicDataFiltered[0][0]['eOrw']
                nors = geographicDataFiltered[0][0]['nOrs']
                octant = self.get_octane(Long, eorw, nors)
                date = geographicDataFiltered[0][0]['Date']

                # date = datetime.now()
                today = date
                day, time, _ = today.split("/")
                beginMM = float(time)
                day = day
                begining = str(float(time[0])) #+ str(float(time[1]))
                beginMM /= 6
                time = str(float(beginMM))
                day = day
                begining = str(float(time[0])) #+ str(float(time[1]))
                validity = self.get_validity(float(time[0]))
                try:
                    windDrn = geographicDataFiltered[0][0]['Course']
                except:
                    windDrn

                try:
                    windSpeed = geographicDataFiltered[0][0]['Speed']
                    tempKelvin = geographicDataFiltered[0][0]['BrdTemp']
                    pressure = geographicDataFiltered[0][0]['Pressure']
                except:
                    windSpeed = 0
                    tempKelvin = 0
                    pressure = 0

                Lat = float(Lat)
                Long = float(Long)
                altitude = float(altitude)

                LatDD = float(Lat)
                LatDD = float(LatDD / 100)
                LatMM = round(Lat % 100.0 / 6.0)
                Lat = float(LatDD * 10 + LatMM)
                LongDD = float(Long)
                LongDD = float(LongDD / 100)
                LongMM = round(Long % 100.0 / 6.0)
                Long = LongDD * 10.0 + LongMM
                altMts = float(altitude)
                altMts = float(altitude) / 10
                presMb = float(pressureMdp)
                presMb = float(round(presMb))
                LatStr = str(float(Lat))
                LongStr = str(float(Long))
                altitudeStr = "{:.3f}".format(altMts)
                pressureMdpStr = "{:.3f}".format(presMb)

                #original><<<<<<<<<<<<<<

                heightAboveMdp = ""
                refractiveIndex = ""
                buttonGroupSelection = ""

                # modified<<<<<<<<<<<<<<<<<<<<<<<
                heightAboveMdp = 100
                refractiveIndex = 5
                buttonGroupSelection = 1

                if buttonGroupSelection == 1:
                    # heightAboveMdp = "{:.3f}".format(comboBoxHeightForMetTA.getSelectedItem())
                    # print(comboBoxHeightForMetTA.getSelectedItem())
                    heightAboveMdp = "{:.3f}".format(111.33)
                    print(heightAboveMdp)
                elif buttonGroupSelection == 2:
                    heightAboveMdp = "166"
                elif buttonGroupSelection == 3:
                    heightAboveMdp = "199"
                else:
                    heightAboveMdp = "199"

                refractiveIndex = "22"

                if refractiveIndex == "":
                    refractiveIndex = " / / / "
                header = format + octant + LatStr + LongStr + new_line + day + begining + validity + " " + altitudeStr + pressureMdpStr + new_line + heightAboveMdp + refractiveIndex
                body = header + new_line
                for k in range(len(heightMtrs[0])):
                    try:
                        windDrn = geographicDataFiltered[0][k]['Course']
                        windSpeed = geographicDataFiltered[0][k]['Speed']
                        tempKelvin = geographicDataFiltered[0][k]['BrdTemp']
                        relHumidity = geographicDataFiltered[0][k]['relHumidity']
                    except Exception as e6:
                        #print(e6)
                        continue
                    windDrn *= 17.777777778
                    windDrn /= 10.0
                    windSpeed = round(windSpeed)
                    tempKelvin = round(tempKelvin)
                    relHumidity = round(relHumidity)
                    if relHumidity == 100.0:
                        relHumidity = 0.0
                    body += lineNo[k] + "{:.3f}".format(windDrn) + "{:.3f}".format(windSpeed) + " " + str(tempKelvin) + "{:.2f}".format(relHumidity) + new_line
                # print(body)
                return body
            except Exception as e:
                print(e)
                print( "Please select different date and time.", "Data not found ", 1)

class ForTemp():
    def __init__(self):
        pass
  
    def format_temp_report(self, section_data, section_type, report_type, station_id, date_time):
        formatted = f"{report_type}{section_type} {station_id} {date_time}"
        for level_data in section_data:
            pressure = f"{float(level_data['pressure']):03}"
            height = f"{float(level_data['geopotential_height'] / 10):03}"
            temp = f"{float(round((level_data['temperature'] + 50) * 10)):03}"
            wind_dir = f"{float(round(level_data['wind_direction'] / 10)):02}"
            wind_speed = f"{float(round(level_data['wind_speed'])):02}"
            formatted += f" {pressure}{height}{temp}{wind_dir}{wind_speed}"
        return formatted + " 51515"

    def TEMP_report(self, report_section, report_type):
        samples = []
        csvFileName ="dataset/MET/full_data_test.csv"
        with open(csvFileName, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            samples = []
            for row in reader:
                sample = {
                    "Latitude": row["LAT"],
                    "Longitude": row["LON"],
                    "geopotential_height": float(row["HGHT"]),
                    "eOrw": 'W',
                    "nOrs": 'N',
                    "Date": datetime.datetime.strftime(datetime.datetime.now(), "%d/%H/%M"),
                    "wind_direction": float(row["DRCT"]),
                    "wind_speed":float( row["SPED"]),
                    "temperature": float(row["TEMP"]),
                    "Pressure": float(row["PRES"])
                }             
                samples.append(sample)

        raw_data_string = {
            "station_id": "12345",
            "date_time": "2023-06-24 00:00",
            "mandatory_levels": [
                {"pressure": 200, "geopotential_height": 11000, "temperature": -50.5, "wind_direction": 180, "wind_speed": 20},
                {"pressure": 500, "geopotential_height": 6000, "temperature": -20.2, "wind_direction": 270, "wind_speed": 10},
                {"pressure": 800, "geopotential_height": 2000, "temperature": 15.3, "wind_direction": 90, "wind_speed": 5}
            ],
            "significant_levels": [
                {"pressure": 250, "geopotential_height": 9000, "temperature": -40.1, "wind_direction": 200, "wind_speed": 15},
                {"pressure": 550, "geopotential_height": 5000, "temperature": -10.7, "wind_direction": 280, "wind_speed": 8},
                {"pressure": 850, "geopotential_height": 1500, "temperature": 10.8, "wind_direction": 100, "wind_speed": 3}
            ]
        }
        
        raw_data_string = {
            "station_id": "12345",
            "date_time": "2023-06-24 00:00",
            "mandatory_levels": 
            samples ,
            "significant_levels": 
                samples
        }

        print(raw_data_string)

        raw_data = raw_data_string
        station_id = raw_data['station_id']
        date_time = raw_data['date_time']
        
        # Separate mandatory and significant levels into sections based on pressure ranges
        mandatory_sections = [
            [level for level in raw_data["mandatory_levels"] if 100 <= level["Pressure"] < 400],
            [level for level in raw_data["mandatory_levels"] if 400 <= level["Pressure"] < 700],
            [level for level in raw_data["mandatory_levels"] if 700 <= level["Pressure"]],
        ]

        significant_sections = [
            [level for level in raw_data["significant_levels"] if 100 <= level["Pressure"] < 400],
            [level for level in raw_data["significant_levels"] if 400 <= level["Pressure"] < 700],
            [level for level in raw_data["significant_levels"] if 700 <= level["Pressure"]],
        ]

        # Format TEMP sections
        
        if report_section == 'AA' and report_type == 'TT':
            mapped_section = ['AA']
            mapped_report = ['TT']
        elif report_section == 'BB' and report_type == 'TT':
            mapped_section = ['BB']
            mapped_report = ['TT']
        elif report_section == 'CC' and report_type == 'TT':
            mapped_section = ['CC']
            mapped_report = ['TT']
        elif report_section == 'DD' and report_type == 'TT':
            mapped_section = ['DD']
            mapped_report = ['TT']
        elif report_section == 'AA' and report_type == 'PP':
            mapped_section = ['AA']
            mapped_report = ['PP']
        elif report_section == 'BB' and report_type == 'PP':
            mapped_section = ['BB']
            mapped_report = ['PP']
        elif report_section == 'CC' and report_type == 'PP':
            mapped_section = ['CC']
            mapped_report = ['PP']
        elif report_section == 'DD' and report_type == 'PP':
            mapped_section = ['DD']
            mapped_report = ['PP']
 
        sections = mapped_section
        report_types = mapped_report
        formatted_sections = {}

        for report_type in report_types:
            for i, section_data in enumerate(mandatory_sections + significant_sections):
                # print( i, section_data, sections)
                section_type = sections
                formatted_sections[f"{report_type}{section_type}"] = self.format_temp_report(
                    section_data, section_type, report_type, station_id, date_time
                )

        # Print the formatted sections
        data = ""
        for section_key in formatted_sections:
            print(f"{section_key}: {formatted_sections[section_key]}")
            data += f"{section_key}: {formatted_sections[section_key]}"
        
        return data

    def generate_fm36_v_report(self, aircraft_id, location, observation_time):
        samples = []
        csvFileName ="dataset/MET/full_data_test.csv"
        with open(csvFileName, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            samples = []
            for row in reader:
                sample = {
                    "Latitude": row["LAT"],
                    "Longitude": row["LON"],
                    "geopotential_height": float(row["HGHT"]),
                    "eOrw": 'W',
                    "nOrs": 'N',
                    "Date": datetime.datetime.strftime(datetime.datetime.now(), "%d/%H/%M"),
                    "wind_direction": float(row["DRCT"]),
                    "wind_speed":float( row["SPED"]),
                    "temperature": float(row["TEMP"]),
                    "pressure_level": float(row["PRES"])
                }             
                samples.append(sample)

        wind_data = samples

        message_header = f'FM36-V {observation_time.strftime("%Y%m%d%H%M")}\n{aircraft_id} {location}\n'

        wind_groups = ''
        for wind_point in wind_data:
            pressure_level = wind_point['pressure_level']
            wind_direction = wind_point['wind_direction']
            wind_speed = wind_point['wind_speed']

            wind_group = f'{pressure_level:05} {wind_direction:03} {wind_speed:03}\n'
            wind_groups += wind_group

        message_termination = 'NNNN\n'

        return message_header + wind_groups + message_termination

class DataProcessor:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.data_frame = None

    def calculate_variables(self):
        self.data_frame = pd.read_csv(self.csv_path)
        self.rad()
        self.time()
        self.calculate_geopotential_height()
        self.calculate_dew_point()
        self.calculate_ascent_rate()
        self.calculate_wind_speed()
        self.calculate_wind_direction()
        self.calculate_virtual_temperature()
        # self.SPEED()
        # self.Direction()

    def time(self):
        start_date = datetime.datetime(2023, 7, 1, 5, 15, 10)
        end_date = datetime.datetime(2023, 7, 1, 7, 15, 8)
        self.data_frame['timestamp'] = [start_date + datetime.timedelta(seconds=random.randint(0, (end_date - start_date).total_seconds())) for _ in range(23)]
        self.data_frame['timestamp'] = pd.to_datetime(self.data_frame['timestamp'])

    def rad(self):
        lat_deg = self.data_frame['Latitude'].astype(int)
        lat_min = ((self.data_frame['Latitude'] - lat_deg) * 60.0).astype(int)
        self.data_frame['Latitude_R'] = (self.data_frame['Latitude'] - lat_deg - lat_min / 60.0) * 3600.0
        lon_deg = self.data_frame['Longitude'].astype(int)
        lon_min = ((self.data_frame['Longitude'] - lon_deg) * 60.0).astype(int)
        self.data_frame['Longitude_R'] = (self.data_frame['Longitude'] - lon_deg - lon_min / 60.0) * 3600.0

    def calculate_wind_speed(self):
        self.data_frame['SPED'] = np.random.rand(23)
        #self.data_frame['SPED'] = self.data_frame['distance_2d'] / (self.data_frame['time_diff'] / 3600)

    def calculate_wind_direction(self):
        # self.data_frame['DRCT'] = np.random.rand(23)
        # self.data_frame['DRCT'] = np.random.rand(23)
        self.data_frame['time_diff'] = self.data_frame['timestamp'].diff().dt.total_seconds().shift(-1)
        R = 6371

        self.data_frame['latitude_rad_diff'] = self.data_frame['Latitude_R'].diff().shift(-1)
        self.data_frame['longitude_rad_diff'] = self.data_frame['Longitude_R'].diff().shift(-1)
        self.data_frame['distance_2d'] = R * np.arccos(
            np.sin(self.data_frame['Latitude_R']) * np.sin(self.data_frame['Latitude_R'] + self.data_frame['latitude_rad_diff']) +
            np.cos(self.data_frame['Latitude_R']) * np.cos(self.data_frame['Latitude_R'] + self.data_frame['latitude_rad_diff']) *
            np.cos(self.data_frame['longitude_rad_diff'])
        )

        self.data_frame['DRCT'] = (np.degrees(np.arctan2(self.data_frame['longitude_rad_diff'], self.data_frame['latitude_rad_diff'])) + 360) % 360

    def calculate_geopotential_height(self):
        # Implement the calculation logic for geopotential height based on the row values
        pass

    def calculate_dew_point(self):
        # Implement the calculation logic for dew point based on the row values
        # dewpt = ['Temperature']-((100-['Humidity'])/5)
        self.data_frame['Dew Point'] = self.data_frame['Temperature'] - ((100 - self.data_frame['Humidity']) / 5)
        # return dewpt

    def calculate_ascent_rate(self):
        # Implement the calculation logic for ascent rate based on the row values
        self.data_frame['AscentRate'] = self.data_frame['HGHT']/self.data_frame['Time']
        pass

    # def calculate_wind_speed(self):
    #     # Implement the calculation logic for wind speed based on the row values
    #     pass

    # def calculate_wind_direction(self):
    #     # Implement the calculation logic for wind direction based on the row values
    #     pass

    def calculate_virtual_temperature(self):
        # Implement the calculation logic for virtual temperature based on the row values
        pass

    def save_to_csv(self, output_csv_path):
        self.data_frame.to_csv(output_csv_path, index=False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    app.exec()