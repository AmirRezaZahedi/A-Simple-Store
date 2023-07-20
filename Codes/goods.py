from prettytable import PrettyTable
from colorama import Fore, Style
from termcolor import colored
import csv
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QWidget, QApplication
from PyQt5.QtCore import Qt
from typing import List, Optional


class AttributeDescriptor:
    def __init__(self, name):
        self.private_attr = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.private_attr)

    def __set__(self, instance, value):
        # Run validations on the received value
        if self.validate_value(value):
            setattr(instance, self.private_attr, value)
        else:
            raise ValueError(f"Invalid value for {self.private_attr}")

    def validate_value(self, value):
        if isinstance(value, str):
            return bool(value.strip())  # Check if the stripped string is non-empty
        elif isinstance(value, (int, float)):
            return value >= 0  # Check if the numeric value is greater than or equal to zero
        else:
            return False  # Invalid type

class Goods:
    def __init__(self, name: str, price: float, path,  quantity=0):
        assert int(price) > 0, f"{price} is negative"
        assert len(name) > 2, f"len of {name} is smaller than 2"
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.path = path

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value

    @property
    def path(self):
        return self.__path
    @path.setter
    def path(self, value):
        self.__path = value

    @staticmethod
    def CreateProduct(Name, Price, Count, path):
        product = Goods(Name, Price, path, Count)
        ui_file_path = os.path.join(os.getcwd(), "Databases", "Product.csv")
        
        with open(ui_file_path, 'r+', newline='') as file:
                reader = csv.reader(file)
                existing_names = set(row[0] for row in reader)

                if Name in existing_names:
                    print("Product exists with this name!")
                else:
                    print(f"The product created\nname is: {Name}.")
                    data = [[product.name, str(product.price), str(product.quantity), product.path]]
                    writer = csv.writer(file)
                    writer.writerows(data)


    def changePath(self, value):
        DatabasePath = os.path.join(os.getcwd(), "Databases", "Product.csv")
        data = []
        with open(DatabasePath, 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)
            
        for row in data:
            if row[0] == self.name:
                row[3] = str(value)
                break

        with open(DatabasePath, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    def changeName(self, value):
        DatabasePath = os.path.join(os.getcwd(), "Databases", "Product.csv")
        data_list = []
        with open(DatabasePath, 'r', newline='') as file:
            reader = csv.reader(file)
            existing_names = set(row[0] for row in reader)
            file.seek(0)  # برگرداندن مکان نما به ابتدای فایل
            for row in reader:
                data_list.append(row)

        if value in existing_names:
            print("Product exists with this name!")
        else:
            print(f"The product's name changed\nname is: {self.name}.")
            for row in data_list:
                if row[0] == self.name:
                    row[0] = str(value)
                    break

            with open(DatabasePath, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data_list)
                
    def changePrice(self, value):#function to change price
        DatabasePath = os.path.join(os.getcwd(), "Databases", "Product.csv")
        data = []
        with open(DatabasePath, 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)

        for row in data:
            if row[0] == self.name:
                row[1] = str(value)
                break

        with open(DatabasePath, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)


    def changeQuantity(self, quantity):#function to change quantity
        DatabasePath = os.path.join(os.getcwd(), "Databases", "Product.csv")
        data = []
        with open(DatabasePath, 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)

        for row in data:
            if row[0] == self.name:
                row[2] = str(quantity)
                break

        with open(DatabasePath, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)


    def __str__(self) -> str:
        return f"Name: {self.name}\nPrice: {self.price}"

    @staticmethod
    def loadGoodsFromcsv(filename: str) -> Optional[List['Goods']]:
        goods_list = []
        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 4:
                        name, price, quantity, path = row
                        goods = Goods(name, float(price), path, int(quantity))
                        goods_list.append(goods)
        except FileNotFoundError:
            print("The file doesn't exist!")
            return None
        return goods_list
    
    def showDetails(self, page):
        page.Name.setText(str(self.name))
        page.Price.setText(str(self.price))
        page.Quantity.setText(str(self.quantity))

    @staticmethod
    def getPrice(name):
        
        filePath = os.path.join(os.getcwd(), "Databases", "Product.csv")
        try:
            with open(filePath, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if name == row[0]:
                        return row[1]
        except FileNotFoundError:
            print("The file doesn't exist!")
            return None

    def __str__(self) -> str:
        return f"Name: {self.name}\nPrice: {self.price}"



if __name__ == "__main__":
    # Create instances of Goods
    item1 = Goods("Lap top ideapad320", 1000, 5)
    item2 = Goods("galaxy s21", 1500, 55)
    '''
    # Access and modify attributes
    print(item1.name)  # Output: Product A
    print(item1.price)  # Output: 10.99
    print(item1.quantity)  # Output: 5

    item2.changePrice(955)
    # Print all goods
    print(Goods.all[0].name)  # Output: [Item('Product A',10.99,5), Item('Product B',5.99,0)]
    '''
