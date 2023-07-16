from Customer import customer
from goods import Goods
import csv
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
import sqlite3
from datetime import date
from PyQt5.QtPrintSupport import QPrinter


ui, _ = loadUiType('front\Customer.ui')

class MainApp(QMainWindow,obj,ui):
        def __init__(self):
            QMainWindow.__init__(self)
            self.setupUi(self)
            self.name = obj.firstName