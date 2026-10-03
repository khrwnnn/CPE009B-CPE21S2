import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Special Midterm Exam in OOP")
        self.setGeometry(100, 100, 400, 300)

        self.btn = QPushButton("Click to Change Color", self)
        self.btn.resize(150, 30)
        self.btn.move(125, 135)
        self.btn.clicked.connect(self.change_color)

    def change_color(self):
        self.btn.setStyleSheet("background-color: yellow;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())