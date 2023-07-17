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
sys.path.append('../oop-python')

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
        self.customer = customer
        ui_file_path = os.path.join(os.getcwd(), "front", "Customer.ui")
        loadUi(ui_file_path, self)
        self.setWindowTitle("Customer-page")
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
        self.setWindowTitle("Change information")
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
        self.setWindowTitle("Product Window")
        self.setGeometry(100, 100, 889, 673)
        ProductDatabase_file_path = os.path.join(os.getcwd(), "Databases", "Product.csv")

        goodsList = Goods.loadGoodsFromcsv(ProductDatabase_file_path)
        if goodsList is not None:
            self.show_goods(goodsList)

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
                    color: #000;
                    font-size: 16px;
                    width: 300px;
                    height: 300px;
                    padding: 30px;
                    text-align: center;
                }
            """)

            details_button = QPushButton("نمایش جزییات")
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
            layout.addWidget(details_button)

            container_widget = QWidget()
            container_widget.setLayout(layout)

            main_layout.addWidget(container_widget)

    def openDetailsWindow(self, goods: Goods):
        details_window = ShowDetailsProduct(goods)
        details_window.setWindowModality(Qt.ApplicationModal)
        details_window.show()
        details_window.exec_()

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
    