# This is a sample Python script.
from PyQt6.QtWidgets import QMainWindow
import sys



# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # set window title
        self.setWindowTitle("Pictionary Game - A2 Template")

        # set the windows dimensions
        top = 400
        left = 400
        width = 800
        height = 600
        self.setGeometry(top, left, width, height)
        self.setGeometry(top, left, width, height)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
