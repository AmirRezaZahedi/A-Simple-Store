import os
import csv
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sqlite3
from datetime import date
from Customer import customer
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QWidget, QApplication
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
import csv

class mainWindowUI(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_file_path = os.path.join(os.getcwd(), "front", "Login.ui")
        loadUi(ui_file_path, self)
        self.show()
        self.LOGINBUTTONCUS.clicked.connect(self.checklogin)
        

    def checklogin(self):
        result, cus_tmp = customer.login(self.USERNAMEINPUT.text(),self.PASSWORDINPUT.text())
        if(result == True):
            print("welcome!")
            self.close()
            self.window = LoginWindowUI(cus_tmp)
            self.window.show()
        else:
            print("Bad!")


       
# ----| LoginWindowUI |----
class LoginWindowUI(QMainWindow):
    def __init__(self, customer):
        super().__init__()
        ui_file_path = os.path.join(os.getcwd(), "front", "Customer.ui")
        loadUi(ui_file_path, self)
        self.setWindowTitle("Customer-page")
        self.Name.setText(customer.firstName)
        self.Lastname.setText(customer.lastName)
        self.Age.setText(customer.age)
        self.Gmail.setText(customer.email)
        self.OPENSTORE.clicked.connect(lambda: self.Openstore(customer))
        self.CHANGEINFO.clicked.connect(lambda: self.pageChangeInfo(customer))

    def Openstore(self, customer):
        self.close()
        self.window = ProductWindow(customer)
        self.window.show()

    def pageChangeInfo(self, customer):
        self.close()
        self.window = ChangeInfo(customer)
        self.window.show()





class ChangeInfo(QDialog):
    def __init__(self, customer):
        super().__init__()
        ui_file_path = os.path.join(os.getcwd(), "front", "Changeinfo.ui")
        loadUi(ui_file_path, self)
        self.setWindowTitle("Change information")
        self.setGeometry(100, 100, 889, 673)
        self.changeinfo.clicked.connect(lambda: self.Changeinfo(customer))
    
    def Changeinfo(self, customer):
        password = self.Cpassword.text()
        customer.change(self.Cname.text(), self.Clastname.text(), self.Cage.text(), password)
        self.close()
        self.window = LoginWindowUI(customer)
        self.window.show()

class ProductWindow(QDialog):
    def __init__(self, customer):
        super().__init__()
        loadUi("C:\\Users\\10\\Desktop\\oop-python\\front\\Showproduct.ui", self)
        self.setWindowTitle("Product Window")
        self.setGeometry(100, 100, 889, 673)
        #self.setStyleSheet("background-color: rgba(41, 5, 5, 253);")
        products = self.load_products_from_csv("C:\\Users\\10\\Desktop\\oop-python\\Databases\\Product.csv")

        main_layout = QVBoxLayout(self.scrollAreaWidgetContents)
        main_layout.setAlignment(Qt.AlignTop)
        main_layout.setSpacing(10)

        row_layout = None
        for index, product in enumerate(products):
            if index % 2 == 0:
                row_layout = QHBoxLayout()
                main_layout.addLayout(row_layout)

            row_layout.addWidget(product)

    def load_products_from_csv(self, filename):
        products = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:
                    product_widget = QLabel(self.scrollAreaWidgetContents)
                    product_widget.setObjectName("productLabel")
                    product_widget.setText(f"Name: {row[0]}\nPrice: {row[1]}")
                    product_widget.setAlignment(Qt.AlignCenter)
                    product_widget.setStyleSheet("""
                        QLabel#productLabel {
                            background-color: #7D0F0F;
                            border-radius: 50%;
                            color: #000;
                            font-size: 16px;
                            width: 300px;
                            height: 300px;
                            padding: 30px;
                            text-align: center;
                        }
                    """)
                    products.append(product_widget)

        return products







def main():
    import sys
    app = QApplication(sys.argv)
    mainUI = mainWindowUI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()    
    