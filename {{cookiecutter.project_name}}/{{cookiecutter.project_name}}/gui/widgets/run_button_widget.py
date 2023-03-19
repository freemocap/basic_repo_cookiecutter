from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton


class RunButtonWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self._layout = QVBoxLayout()
        self.setLayout = self._layout

        self._title = QLabel("The code for this widget is defined in the file: {__file__}")
        self._layout.addWidget(self._title)
        
        self.run_button_widget = QPushButton('Run',self)

        self.run_button_widget.clicked.connect(self.run_script)

    def run_script(self):
        print(f"Running a print statement from - {__file__} - wow!!\n
        "Put your code here, and it will run when that button is pressed :D")     