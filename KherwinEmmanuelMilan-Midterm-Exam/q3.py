import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton,
                             QLabel, QLineEdit)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Midterm in OOP")
        self.setGeometry(100, 100, 600, 300)

        #Red label
        self.label = QLabel("Enter your fullname:", self)
        self.label.setGeometry(40, 95, 230, 32)
        self.label.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
        self.label.setStyleSheet("color: red;")

        #Input box
        self.entry1 = QLineEdit(self)
        self.entry1.setGeometry(300, 95, 250, 32)
        self.entry1.setStyleSheet("font-size: 16px;")

        #Button with red text
        self.button = QPushButton("Click to display your Fullname", self)
        self.button.setGeometry(40, 145, 230, 32)
        self.button.setStyleSheet("color: red;")
        self.button.clicked.connect(self.display_name)

        #Output box
        self.entry2 = QLineEdit(self)
        self.entry2.setGeometry(300, 145, 250, 32)
        self.entry2.setStyleSheet("font-size: 16px;")

    def display_name(self):
        self.entry2.setText(self.entry1.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())