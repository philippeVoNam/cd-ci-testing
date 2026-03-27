import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class CounterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.layout = QVBoxLayout(self)
        self.label = QLabel("0")
        self.button = QPushButton("Click It")
        self.button.clicked.connect(self.increment)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

    def increment(self):
        self.count += 1
        self.label.seText(str(self.count))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CounterApp()
    window.show()
    sys.exit(app.exec())
