import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import csv

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("Airline.ui", self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #add close btn
        self.CrossButton.clicked.connect(lambda: self.close())
        
        self.load_table()
        
        # Button Functions
        self.AddButton.clicked.connect(self.add_flight)
        self.DeleteButton.clicked.connect(self.delete_flight)
        self.EditButton.clicked.connect(self.edit_flight)
        self.StuInfoTable.clicked.connect(self.fill_values)
    
    # This function allows the user to select the value from the table to edit or delete
    def fill_values(self):
        row = self.StuInfoTable.currentRow()
        self.NameEdit.setText(self.StuInfoTable.item(row, 0).text())
        self.RegEdit.setText(self.StuInfoTable.item(row, 1).text())
        self.gpaEdit.setText(self.StuInfoTable.item(row, 2).text())
        self.uniEdit.setText(self.StuInfoTable.item(row, 3).text())
    
    # This is a helper function to reset the text fields after adding or editing a flight.
    def reset_values(self):
        self.NameEdit.setText("Flight Name")
        self.RegEdit.setText("Time")
        self.gpaEdit.setText("Price")
        self.uniEdit.setText("Destination")

    def check_flight_name(self, name): 
        with open('Airline.csv', 'r', encoding="utf-8", newline="") as fileInput:
            data = list(csv.reader(fileInput))
            for row in data:
                if name == row[0]:
                    return False
        return True

    # Add flight to CSV file if the flight name is not already added.
    def add_flight(self):
        name = self.NameEdit.text()
        time = self.RegEdit.text()
        price = self.gpaEdit.text()
        destination = self.uniEdit.text()

        if not price.isdigit():
            self.show_error_message("Price must be an integer.")
            return

        if name != "Flight Name" and self.check_flight_name(name):
            flight_data = [name, time, price, destination]

            with open('Airline.csv', 'a+', encoding="utf-8", newline="") as fileInput:
                writer = csv.writer(fileInput)
                writer.writerows([flight_data])
            self.reset_values()
        else:
            self.show_error_message("Flight is already added.")
        
        # Reload the table to show the recently added data
        self.load_table()
        
    # Edit flight details in the CSV file
    def edit_flight(self):
        row = self.StuInfoTable.currentRow()
        original_name = self.StuInfoTable.item(row, 0).text()
        name = self.NameEdit.text()
        time = self.RegEdit.text()
        price = self.gpaEdit.text()
        destination = self.uniEdit.text()
        updated_data = []
        flight_found = False

        if not price.isdigit():
            self.show_error_message("Price must be an integer.")
            return

        with open('Airline.csv', "r", encoding="utf-8") as fileInput:
            reader = csv.reader(fileInput)
            for row in reader:
                if len(row) > 0:
                    if original_name == row[0]:
                        flight_found = True
                        updated_data.append([name, time, price, destination])
                    else:
                        updated_data.append(row)
                    
        if flight_found:
            with open('Airline.csv', "w", encoding="utf-8", newline="") as fileOutput:
                writer = csv.writer(fileOutput)
                writer.writerows(updated_data)
            self.load_table()
            self.reset_values()
        
    # Delete flight from the CSV file
    def delete_flight(self):
        name = self.NameEdit.text()
        flight_found = False
        updated_data = []

        with open('Airline.csv', "r", encoding="utf-8") as fileInput:
            reader = csv.reader(fileInput)
            for row in reader:
                if len(row) > 0:
                    if name != row[0]:
                        updated_data.append(row)
                    else:
                        flight_found = True

        if flight_found:
            with open('Airline.csv', "w", encoding="utf-8", newline="") as fileOutput:
                writer = csv.writer(fileOutput)
                writer.writerows(updated_data)
            self.load_table()
            self.reset_values()
        else:
            self.show_error_message("Flight not found.")
      
    # Helper function to load the content of the table after every event
    def load_table(self):
        with open('Airline.csv', "r", encoding="utf-8") as fileInput:
            data = list(csv.reader(fileInput))
            self.StuInfoTable.setRowCount(len(data))
            for row_index, row in enumerate(data):
                self.StuInfoTable.setItem(row_index, 0, QtWidgets.QTableWidgetItem(row[0]))
                self.StuInfoTable.setItem(row_index, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.StuInfoTable.setItem(row_index, 2, QtWidgets.QTableWidgetItem(row[2]))
                self.StuInfoTable.setItem(row_index, 3, QtWidgets.QTableWidgetItem(row[3]))

    # Helper function to show error messages
    def show_error_message(self, message):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText(message)
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        msg.setFont(font)
        msg.exec()
                
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
