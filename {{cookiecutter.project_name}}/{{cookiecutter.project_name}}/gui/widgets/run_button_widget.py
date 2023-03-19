import logging

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

from {{cookiecutter.project_name}}.{{cookiecutter.project_name}}_run_me import run_me


logger = logging.getLogger(__name__)
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
        logger.info(f"Clicked on the run button, running {run_me} (this is being generated from the file at: {__file__}")
        run_me()