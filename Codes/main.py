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
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QAbstractItemView
from PyQt5 import QtWidgets, uic
from PyQt5 import QtWidgets, QtGui
class mainWindowUI(QDialog):

    def __init__(self):
        super().__init__()
        ui_file_path = os.path.join(os.getcwd(), "front", "Mainwindow2.ui")
        loadUi(ui_file_path, self)
        self.REGISTER.clicked.connect(self.checklogin)
        self.show()

    def checklogin(self):
        #self.close()
        #self.window = 
        #result, cus_tmp = customer.login(self.USERNAMEINPUT.text(),self.PASSWORDINPUT.text())
        if(True):
            print("Welcome!")
            self.close()
            self.window = LoginwindowUI2()
            self.window.show()


class LoginwindowUI2(QDialog):
    def __init__(self):
        super().__init__()
        ui_file_path = os.path.join(os.getcwd(), "front", "Login.ui")
        loadUi(ui_file_path, self)
        self.login_btn.clicked.connect(self.checklogin)
        self.ADMIN.clicked.connect(self.loginAdmin)

    def checklogin(self):
        result, cus_tmp = customer.login(self.email_input.text(), self.pass_input.text())
        if(result == True):
            print("Welcome!")
            self.close()
            self.window = AfterLogin(cus_tmp)
            self.window.show()
        else:
            print("Bad login!")

    def loginAdmin(self):
       self.close()
       self.window =  LoginAdmin()
       self.window.show()
# ----| AfterLogin |----
class AfterLogin(QDialog):
    def __init__(self, customer):
        super().__init__()
        self.customer = customer
        ui_file_path = os.path.join(os.getcwd(), "front", "Afterlogin.ui")
        loadUi(ui_file_path, self)
        self.setWindowTitle("Customer Page")
        
        self.OPENSTORE.clicked.connect(self.Openstore)
        self.CHANGEINFO.clicked.connect(self.pageChangeInfo)
        self.BACKTOLOGIN.clicked.connect(self.BackToLogin)
        self.COMPLETEBUY.clicked.connect(self.CompleteBuy)
        self.WELCOME.setText(self.customer.firstName + "Welcome")
        
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

    def CompleteBuy(self):
        self.close()
        self.window = ShowFactor(self.customer)
        self.window.show()
# ----| ChangeInfo |----
class ChangeInfo(QDialog):
    def __init__(self, customer):
        super().__init__()
        self.customer = customer
        ui_file_path = os.path.join(os.getcwd(), "front", "Changeinfo.ui")
        loadUi(ui_file_path, self)
        self.setWindowTitle("Change Information")
        self.setGeometry(100, 100, 889, 673)
        self.CHANGEINFO.clicked.connect(self.Changeinfo)
        self.customer.ChangeCustom(self.Cname, self.Clastname, self.Cage, self.Cpassword)

    def Changeinfo(self):

        self.customer.change(self.Cname.text(), self.Clastname.text(), self.Cage.text(), self.Cpassword.text())
        self.close()
        self.window = AfterLogin(self.customer)
        self.window.show()

class LoginAdmin(QDialog):
    def __init__(self):
        super().__init__()
        ui_file_path = os.path.join(os.getcwd(), "front", "Login_Admin.ui")
        loadUi(ui_file_path, self)
        self.login_btn.clicked.connect(self.logIn)
        self.name = "admin"

    def logIn(self):
        if(self.email_input.text() == 'admin' and self.pass_input.text() == 'admin'):
            self.close()
            self.window = AdminPage()
            self.window.show()
        else:
            print("Bad")
    
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
        self.setFixedSize(1024, 900)
        ProductDatabase_file_path = os.path.join(os.getcwd(), "Databases", "Product.csv")

        self.goodsList = Goods.loadGoodsFromcsv(ProductDatabase_file_path)
        if self.goodsList is not None:
            self.show_goods(self.goodsList)

    

    def show_goods(self, goods_list: List['Goods']):
        main_layout = QGridLayout(self.scrollAreaWidgetContents)
        main_layout.setAlignment(Qt.AlignTop)
        main_layout.setHorizontalSpacing(20)
        main_layout.setVerticalSpacing(20)

        # Set the background color of the button
        button_background_color = "#df2569"

        for index, goods in enumerate(goods_list):
            product_widget = QLabel(self.scrollAreaWidgetContents)
            product_widget.setObjectName(f"productLabel_{index}")
            product_widget.setText(f"Name: {goods.name}\nPrice: {goods.price}")
            product_widget.setAlignment(Qt.AlignCenter)
            product_widget.setStyleSheet(f"""
                QLabel {{
                    background-color: #73628a;
                    border-radius: 50%;
                    color: #fff;
                    font-size: 16px;
                    width: 300px;
                    height: 300px;
                    padding: 30px;
                    text-align: center;
                }}
            """)

            spinbox = QSpinBox()
            spinbox.setObjectName("spinBox_" + str(goods.name))  # Use a unique name for each spinbox
            spinbox.setMinimum(0)
            spinbox.setValue(0)
            spinbox.setMaximum(100)

            details_button = QPushButton("Show Details")
            details_button.setObjectName(f"detailsButton_{index}")
            details_button.setStyleSheet(f"""
                QPushButton {{
                    font-size: 11.5px;
                    width: 118px;
                    height: 28px;
                    border-radius: 10%;
                    background-color: {button_background_color};
                    color: #fff;
                    font: 15pt "IRANSans";
                }}
            """)
            details_button.clicked.connect(lambda checked, goods=goods: self.openDetailsWindow(goods))

            container_widget = QWidget()
            layout = QVBoxLayout()
            layout.addWidget(product_widget)
            layout.addWidget(spinbox)
            layout.addWidget(details_button)
            container_widget.setLayout(layout)

            # Calculate the row and column based on the index to create the horizontal layout
            row = index // 3
            column = index % 3
            main_layout.addWidget(container_widget, row, column)

        self.scrollAreaWidgetContents.setLayout(main_layout)

    def openDetailsWindow(self, goods: Goods):
        details_window = ShowDetailsProduct(goods)
        details_window.setWindowModality(Qt.ApplicationModal)
        details_window.show()
        details_window.exec()
        
    def exitWindow(self):
        self.window = AfterLogin(self.customer)
        self.window.show()
        self.close()
    
    def AddToCart(self):
        quantities = {} 

        for goods in self.goodsList:
            spinbox = self.findChild(QSpinBox, "spinBox_" + str(goods.name))
            if spinbox and spinbox.value() > 0:
                quantity = spinbox.value()
                quantities[goods.name] = quantity
        
        if not quantities:
            print("No products selected!")
            return
        check = self.customer.addProduct(quantities)
        
        if(check):

            msgBox = CustomMessageBox()
            msgBox.exec_()


            

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


class ShowFactor(QDialog):
    def __init__(self, customer):
        super().__init__()
        ui_file_path = os.path.join(os.getcwd(), "front", "Completebuy.ui")
        loadUi(ui_file_path, self)
        self.customer = customer
        Factor = eval(self.customer.cart)

        # Create a table with three columns (product name, quantity, and price)        
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["نام محصول", "تعداد", "قیمت"])
        self.DELETEALL.clicked.connect(self.DeleteCart)
        # Adjust the width of the columns
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)

        # Choose colors
        color1 = QColor(230, 255, 255)  # آبی روشن
        color2 = QColor(255, 245, 230)  # نارنجی روشن
        brush1 = QBrush(color1)
        brush2 = QBrush(color2)
        total = 0

        for i in range(1, len(Factor)):
            product_name, quantity = Factor[i].split(':')
            price = Goods.getPrice(product_name)
            total = total + float(price) * int(quantity)
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)

            # Add information to the table
            self.tableWidget.setItem(row_position, 0, QTableWidgetItem(product_name))
            self.tableWidget.setItem(row_position, 1, QTableWidgetItem(quantity))
            self.tableWidget.setItem(row_position, 2, QTableWidgetItem(str(price)))

            # Set background color for rows
            if i % 2 == 0:
                for j in range(3):
                    self.tableWidget.item(row_position, j).setBackground(brush1)
            else:
                for j in range(3):
                    self.tableWidget.item(row_position, j).setBackground(brush2)

            # Set color for cells
            for j in range(3):
                self.tableWidget.item(row_position, j).setTextAlignment(Qt.AlignCenter)
                font = self.tableWidget.item(row_position, j).font()
                font.setBold(True)
                self.tableWidget.item(row_position, j).setFont(font)
        # Create and set the label for total
        total_label = QLabel(f"مجموع: {total}")
        total_label.setStyleSheet("""
            font-size: 16px;
            color: #333333;
            font-weight: bold;
        """)

        # Add total label to the layout
        layout = self.verticalLayout
        layout.addWidget(total_label)
        

    def DeleteCart(self):
            if(len(eval(self.customer.cart)) != 1):
                self.customer.deletecart()
                self.close()
                self.window = ShowFactor(self.customer)
                self.window.show()
            else:
                print("Empty")

    
class AdminPage(QDialog):
    def __init__(self):
        super().__init__()
        ui_file_path = os.path.join(os.getcwd(), "front", "AdminPage.ui")
        loadUi(ui_file_path, self)
        self.ADDPRODUCT.mousePressEvent = self.AddProduct
        self.edit.mousePressEvent = self.EditProduct
        #self.SelectImageButton.clicked.connect(self.open_image_dialog)
    def AddProduct(self, event):
        print("Add product clicked!")
        self.close()
        self.window = AddProductByAdmin()
        self.window.show()

    def EditProduct(self, event):
        print("Edit clicked")
        self.close()
        self.window = EditProductByAdmin()
        self.window.show()

class AddProductByAdmin(QDialog):
    def __init__(self):
        super().__init__()
        ui_file_path = os.path.join(os.getcwd(), "front", "AddProduct.ui")
        loadUi(ui_file_path, self)

        self.ADD.clicked.connect(self.AddButtom)
        self.SelectImageButton.clicked.connect(self.OpenImageDialog)

    def OpenImageDialog(self):
        options = QFileDialog.Options()
        FilePath, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", 
                                                   "Image Files (*.png *.jpg *.bmp *.jpeg);;All Files (*)", 
                                                   options=options)
        
        if FilePath:
            self.selected_image_label.setText(FilePath)

    def AddButtom(self):
        print("clicked add...!")
        print(self.Name.text(), self.Price.text(), self.Count.text())
        if (self.Name.text() == "") or (self.Price.text() == "") or (self.Count.text() == "") or (self.selected_image_label.text()==""):
            print("Bad..!")

        else:
            Goods.CreateProduct(self.Name.text(), self.Price.text(), self.Count.text(), self.selected_image_label.text())
        
class EditProductByAdmin(QDialog):
    def __init__(self):
        super().__init__()
        ui_file_path = os.path.join(os.getcwd(), "front", "Editproduct.ui")
        Database_file_path = os.path.join(os.getcwd(), "Databases", "Product.csv")
        uic.loadUi(ui_file_path, self)

        self.goods_widgets = {}  # Dictionary to store references to QLineEdit widgets for each Goods object
        self.goodsList = Goods.loadGoodsFromcsv(Database_file_path)
        if self.goodsList is not None:
            self.show_goods(self.goodsList)

    def show_goods(self, goods_list: List['Goods']):
        scroll_layout = QtWidgets.QVBoxLayout()
        for goods in goods_list:
            product_widget = QtWidgets.QWidget()
            product_layout = QtWidgets.QGridLayout()

            # برچسب‌ها
            name_label = QtWidgets.QLabel("Name:")
            price_label = QtWidgets.QLabel("Price:")
            quantity_label = QtWidgets.QLabel("Quantity:")

            # فونت‌ها
            font = QFont()
            font.setPointSize(12)  # اندازه فونت را افزایش می‌دهیم
            font.setBold(True)    # فونت را برجسته می‌کنیم
            name_label.setFont(font)
            price_label.setFont(font)
            quantity_label.setFont(font)

            # ویرایش فونت دکمه ویرایش
            edit_button = QtWidgets.QPushButton("Edit")
            edit_button.setStyleSheet("background-color: #4CAF50; color: white; border: 2px solid #4CAF50; border-radius: 8px;")
            edit_button.setFont(font)

            edit_button.clicked.connect(lambda checked, goods=goods: self.edit_product(goods))

            # ویرایش فونت دکمه "ویرایش عکس"
            choose_image_button = QtWidgets.QPushButton("Choose Image")
            choose_image_button.setFont(font)
            choose_image_button.clicked.connect(lambda checked, goods=goods: self.choose_image(goods))

            # ایجاد ویرایش‌گرها
            product_name_edit = QtWidgets.QLineEdit(goods.name)
            product_price_edit = QtWidgets.QLineEdit(str(goods.price))
            product_quantity_edit = QtWidgets.QLineEdit(str(goods.quantity))
            previous_image_path_edit = QtWidgets.QLineEdit(goods.path)
            previous_image_path_edit.setReadOnly(True)

            # اضافه کردن ویرایش‌گرها به دیکشنری با استفاده از نام محصول به عنوان کلید
            self.goods_widgets[goods.name] = {
                'product_name_edit': product_name_edit,
                'product_price_edit': product_price_edit,
                'product_quantity_edit': product_quantity_edit,
                'previous_image_path_edit': previous_image_path_edit
            }

            # چینش ویجت‌ها و برچسب‌ها در قالب
            product_layout.addWidget(name_label, 0, 0)
            product_layout.addWidget(product_name_edit, 0, 1)
            product_layout.addWidget(price_label, 1, 0)
            product_layout.addWidget(product_price_edit, 1, 1)
            product_layout.addWidget(quantity_label, 2, 0)
            product_layout.addWidget(product_quantity_edit, 2, 1)
            product_layout.addWidget(previous_image_path_edit, 3, 0, 1, 2)  # دکمه از سطر 3، ستون 0 شروع شود و به اندازه 1 سطر و 2 ستون ادامه یابد
            # دکمه از سطر 4، ستون 0 شروع شود و به اندازه 1 سطر و 2 ستون ادامه یابد
            product_layout.addWidget(choose_image_button, 4, 0, 1, 2)  # دکمه از سطر 5، ستون 0 شروع شود و به اندازه 1 سطر و 2 ستون ادامه یابد
            product_layout.addWidget(edit_button, 5, 0, 1, 2)

            product_widget.setLayout(product_layout)
            scroll_layout.addWidget(product_widget)

        self.scrollAreaWidgetContents.setLayout(scroll_layout)



    def choose_image(self, goods: Goods):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly  # انتخاب فایل به صورت تنها خواندنی (readonly)
        file_name, _ = QFileDialog.getOpenFileName(self, "Choose Image", "", "Image Files (*.png *.jpg *.bmp);;All Files (*)", options=options)
        if file_name:
            goods.changePath(file_name)
            previous_image_path_edit = self.findChild(QtWidgets.QLineEdit, "previous_image_path_edit_{}".format(goods.name))
            if previous_image_path_edit:
                self.close()
                self.close()
                self.window = EditProductByAdmin()
                self.window.show()

    def edit_product(self, goods: Goods):
        # Get the edited values from the QLineEdit widgets using the dictionary
        
        edited_name = self.goods_widgets[goods.name]['product_name_edit'].text()
        edited_price = float(self.goods_widgets[goods.name]['product_price_edit'].text())
        edited_quantity = int(self.goods_widgets[goods.name]['product_quantity_edit'].text())

        # Update the Goods object with the edited values
        
        goods.changeName(edited_name)
        goods.name = edited_name

        
        goods.changePrice(edited_price)
        goods.price = edited_price

        
        goods.changeQuantity(edited_quantity)

        goods.quantity = edited_quantity

        self.close()
        self.window = EditProductByAdmin()
        self.window.show()
        
def main():
    import sys
    app = QApplication(sys.argv)
    mainUI = mainWindowUI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
