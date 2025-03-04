import os
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic


class BMICalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMI Calculator")

        ui_path = os.path.join(os.path.dirname(__file__), "bmi_design.ui")
        uic.loadUi(ui_path, self)
        self.button1.clicked.connect(self.calculate_bmi)
        self.actionExit.triggered.connect(lambda: self.exit())
        self.actionClear.triggered.connect(lambda: self.clear())
        self.menuHelp.triggered.connect(lambda: self.help_info())


    def calculate_bmi(self):
        try:
            weight = float(self.lineEdit_2.text())
            height = float(self.lineEdit_3.text()) / 100
            bmi = round(weight / height**2, 1)
            self.label_5.setText(str(bmi))

            if 0 <= bmi < 18.5:
                self.label_5.setStyleSheet("background-color: rgb(255, 232, 57)")
            elif 18.5 <= bmi < 25:
                self.label_5.setStyleSheet("background-color: rgb(1, 255, 94)")
            elif 25 <= bmi < 30:
                self.label_5.setStyleSheet("background-color: rgb(255, 115, 21)")
            else:
                self.label_5.setStyleSheet("background-color: rgb(255, 52, 16)")

        except:
            self.label_5.setText("Value Error")

    def exit(self):
        MyWindow.close(self)

    def clear(self):
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.label_5.clear()
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255)")

    def help_info(self):
        msg = QMessageBox()
        msg.setWindowTitle("About the BMI Application")
        msg.setText("The BMI Calculator Application is created to calculate your Body Mass Index"
                    "using your height in cm and weight in kg. To start calculation firstly, "
                    "type your height and weight to the white places near the appropriate labels,"
                    "after that click the 'Calculate My BMI' button and see the result. "
                    "Thank you for using BMI Calculator! ")
        x = msg.exec()
        return x

