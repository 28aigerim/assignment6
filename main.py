import sys
from PyQt6.QtWidgets import QApplication
from mywindow import BMICalculator


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BMICalculator()
    window.show()
    app.exec()