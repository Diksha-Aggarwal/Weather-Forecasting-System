import math,csv, random
import datetime
import sys
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QTableWidgetItem, QDateTimeEdit, QFileDialog
from PyQt6.QtCore import QDateTime, Qt
from temp_ini import Ui_Form
import pandas as pd
import numpy as np
import csv
import datetime
from datetime import timedelta

csv_path = "D:\\DIKSHA\\B.Tech\\IIITD Internship\\aaizel_POC\\RadioSonde_GUI\\temp_data.csv"
output_csv_path = "D:\\DIKSHA\\B.Tech\\IIITD Internship\\aaizel_POC\\RadioSonde_GUI\\temp_values.csv"

class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.save_to_csv()
        self.display_csv()
        self.ui.pushButton_2.clicked.connect(self.handle_button)
        self.ui.pushButton_3.clicked.connect(self.handle_button)
        self.ui.pushButton_4.clicked.connect(self.handle_button)
        self.ui.pushButton_5.clicked.connect(self.handle_button)
        self.ui.pushButton_6.clicked.connect(self.handle_button)
        self.ui.pushButton_7.clicked.connect(self.handle_button)
        self.ui.pushButton_8.clicked.connect(self.handle_button)
        self.ui.pushButton_9.clicked.connect(self.handle_button)
        self.ui.pushButton_10.clicked.connect(self.handle_button1)
        self.process_data()

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
            writer.writerow(['B', 'Humidity', 'Temperature', 'Pressure', 'Time', 'Latitude_N', 'Longitude_E', 'HGHT'])

            for item in data:
                item_str = item.decode('utf-8')
                values = item_str.strip().split(',')

                b_value = values[0][1:]
                humidity_value = values[1].rstrip('H')
                temperature_value = values[2].rstrip('C')
                pressure_value = values[3].rstrip('P')
                time_value = values[4].rstrip('T')
                latitude_value = values[5].rstrip('N')
                longitude_value = values[6].rstrip('E')
                hght = 41
                writer.writerow([b_value, humidity_value, temperature_value, pressure_value, time_value,
                                 latitude_value, longitude_value, hght])

        #self.process_data()
        print("Data saved to CSV successfully.")

    def display_csv(self):
        df = pd.read_csv(output_csv_path)

        # Set the number of rows and columns in the tableWidget
        self.ui.tableWidget.setRowCount(df.shape[0])
        self.ui.tableWidget.setColumnCount(df.shape[1])

        # Set the table headers
        headers = df.columns.tolist()
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)

        # Fill the tableWidget with data
        for i, row in df.iterrows():
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.ui.tableWidget.setItem(i, j, item)

    def handle_button(self):
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
        self.ui.textEdit.setText(temp_data)
    
    def handle_button1(self):
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
        self.ui.textEdit.setText(pilot_data)
       
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
        
        # sections = ['AA', 'BB', 'CC', 'DD']
        # report_types = ['TT', 'PP']
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

        # Perform calculations for each row and add the calculated values as new columns
        self.calculate_geopotential_height()
        self.calculate_dew_point()
        self.calculate_ascent_rate()
        self.calculate_wind_speed()
        self.calculate_wind_direction()
        self.calculate_virtual_temperature()
        self.SPEED()
        self.Direction()

    def SPEED(self):
        self.data_frame['SPED'] = np.random.rand(23)

    def Direction(self):
        self.data_frame['DRCT'] = np.random.rand(23)

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
        pass

    def calculate_wind_speed(self):
        # Implement the calculation logic for wind speed based on the row values
        pass

    def calculate_wind_direction(self):
        # Implement the calculation logic for wind direction based on the row values
        pass

    def calculate_virtual_temperature(self):
        # Implement the calculation logic for virtual temperature based on the row values
        pass

    def save_to_csv(self, output_csv_path):
        self.data_frame.to_csv(output_csv_path, index=False)

    def save_to_csv(self, output_csv_path):
        self.data_frame.to_csv(output_csv_path, index=False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    app.exec()