import os
import csv
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Customer import customer
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QWidget, QApplication
from PyQt5.QtCore import Qt
from goods import Goods
import sys
from typing import List
#sys.path.append('../oop-python')

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
            print("Welcome!")
            self.close()
            self.window = LoginWindowUI(cus_tmp)
            self.window.show()
        else:
            print("Bad login!")


       
# ----| LoginWindowUI |----
class LoginWindowUI(QMainWindow):
    def __init__(self, customer):
        super().__init__()
        self.customer = customer
        ui_file_path = os.path.join(os.getcwd(), "front", "Customer.ui")
        loadUi(ui_file_path, self)
        self.setWindowTitle("Customer Page")
        customer.showCustomerPage(self.Name,self.Lastname,self.Age,self.Gmail)
        self.OPENSTORE.clicked.connect(self.Openstore)
        self.CHANGEINFO.clicked.connect(self.pageChangeInfo)
        self.BACKTOLOGIN.clicked.connect(self.BackToLogin)

    def Openstore(self):
        self.close()
        self.window = ProductWindow(self.customer)
        self.window.show()

    def pageChangeInfo(self):
        self.close()
        self.window = ChangeInfo(self.customer)
        self.window.show()

    def BackToLogin(self):
        self.close()
        self.window = mainWindowUI()


# ----| ChangeInfo |----
class ChangeInfo(QDialog):
    def __init__(self, customer):
        super().__init__()
        self.customer = customer
        ui_file_path = os.path.join(os.getcwd(), "front", "Changeinfo.ui")
        loadUi(ui_file_path, self)
        self.setWindowTitle("Change Information")
        self.setGeometry(100, 100, 889, 673)
        self.changeinfo.clicked.connect(self.Changeinfo)
    
    def Changeinfo(self):
        password = self.Cpassword.text()
        customer.change(self.Cname.text(), self.Clastname.text(), self.Cage.text(), password)
        self.close()
        self.window = LoginWindowUI(self.customer)
        self.window.show()

class ProductWindow(QDialog):
    def __init__(self, customer):
        super().__init__()
        self.customer = customer
        ui_file_path = os.path.join(os.getcwd(), "front", "Showproduct.ui")
        loadUi(ui_file_path, self)
        self.goodsList = []  # goods_list attribute
        self.setWindowTitle("Product Window")
        self.setGeometry(100, 100, 889, 673)
        self.exit.clicked.connect(self.exitWindow)
        self.ADDTOCART.clicked.connect(self.AddToCart)
        ProductDatabase_file_path = os.path.join(os.getcwd(), "Databases", "Product.csv")

        self.goodsList = Goods.loadGoodsFromcsv(ProductDatabase_file_path)
        if self.goodsList is not None:
            self.show_goods(self.goodsList)

    def exitWindow(self):
        self.window = LoginWindowUI(self.customer)
        self.window.show()
        self.close()

    def show_goods(self, goods_list: List['Goods']):
        main_layout = QVBoxLayout(self.scrollAreaWidgetContents)
        main_layout.setAlignment(Qt.AlignTop)
        main_layout.setSpacing(10)

        for goods in goods_list:
            product_widget = QLabel(self.scrollAreaWidgetContents)
            product_widget.setObjectName("productLabel")
            product_widget.setText(str(goods))
            product_widget.setAlignment(Qt.AlignCenter)
            product_widget.setStyleSheet("""
                QLabel#productLabel {
                    background-color: #7D0F0F;
                    border-radius: 50%;
                    color: #fff;
                    font-size: 16px;
                    width: 300px;
                    height: 300px;
                    padding: 30px;
                    text-align: center;
                }
            """)
            spinbox = QSpinBox()
            spinbox.setObjectName("spinBox_" + str(goods.name))  # Use a unique name for each spinbox
            spinbox.setMinimum(0)  # Minimum value
            spinbox.setValue(0)  # Set default value
            spinbox.setMaximum(100)  # Maximum value
            details_button = QPushButton("Show Details")
            details_button.setObjectName("detailsButton")
            details_button.setStyleSheet("""
                QPushButton#detailsButton {
                    background-color: #4C9EEF;
                    color: #fff;
                    font-size: 14px;
                    width: 120px;
                    height: 30px;
                    border-radius: 5px;
                }
            """)
            details_button.clicked.connect(lambda checked, goods=goods: self.openDetailsWindow(goods))

            layout = QVBoxLayout()
            layout.addWidget(product_widget)
            layout.addWidget(spinbox)
            layout.addWidget(details_button)

            container_widget = QWidget()
            container_widget.setLayout(layout)

            main_layout.addWidget(container_widget)

    def openDetailsWindow(self, goods: Goods):
        details_window = ShowDetailsProduct(goods)
        details_window.setWindowModality(Qt.ApplicationModal)
        details_window.show()
        details_window.exec()
        

    def AddToCart(self):
        quantities = {} 

        for goods in self.goodsList:
            spinbox = self.findChild(QSpinBox, "spinBox_" + str(goods.name))
            if spinbox and spinbox.value() > 0:
                quantity = spinbox.value()
                quantities[goods.name] = quantity
        
        check = self.customer.addProduct(quantities)
        if(check):

            msgBox = CustomMessageBox()
            msgBox.exec_()

        else:
            print("Bad!")

class CustomMessageBox(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Custom Message Box")
        self.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.7);
            border-radius: 10px;
        """)

        layout = QVBoxLayout(self)
        label = QLabel("محصول با موفقیت به سبد خرید اضافه شد")
        label.setStyleSheet("""
            font-size: 20px;
            font-weight: bold;
            color: #333333;
        """)
        layout.addWidget(label)

        button = QPushButton("باشه")
        button.setStyleSheet("""
            background-color: #4C9EEF;
            color: #FFFFFF;
            font-size: 16px;
            border-radius: 5px;
        """)
        button.clicked.connect(self.accept)
        layout.addWidget(button)

class ShowDetailsProduct(QDialog):
    def __init__(self, goods):
        super().__init__()
        ui_file_path = os.path.join(os.getcwd(), "front", "Showdetailproduct.ui")
        loadUi(ui_file_path, self)

        goods.showDetails(self)


def main():
    import sys
    app = QApplication(sys.argv)
    mainUI = mainWindowUI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
