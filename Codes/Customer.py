import csv
from goods import Goods
import os
from Cart import MyCart
class AttributeDescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("walletzBalance cannot be negative")
        instance.__dict__[self.name] = value


class customer(MyCart):

    all = []
    walletzBalance = AttributeDescriptor('walletzBalance')

    def __init__(self, firstName, lastName, age, walletzBalance: float, email, password, cart):
        super().__init__(cart)
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.walletzBalance = walletzBalance
        self.email = email
        self.password = password
        
    
    def showCustomerPage(self,Name,Lastname,Age,Gmail):
        #show information in Customer.ui page
        Name.setText(self.firstName)
        Lastname.setText(self.lastName)
        Age.setText(self.age)
        Gmail.setText(self.email)

    @staticmethod
    def login(username, password):
        with open('C:\\Users\\10\\Desktop\\oop-python\\Databases\\Customer.csv', 'r+', newline='') as file:
            reader = csv.reader(file) 
            for row in reader:
                if row[4] == username and row[5] == password:
                    print("successfull . . .")
                    return True, customer(row[0],row[1],(row[2]),float(row[3]),row[4],row[5],row[6])
                else:
                    print("Bad . . .")
                    return False, None
                
    def ChangeCustom(self, Cname, Clastname, Cage,Cpassword):

        Cname.setText(self.firstName)
        Clastname.setText(self.lastName)
        Cage.setText(self.age)
        Cpassword.setText(self.password)

    def change(self,firstName, lastName, age, password):
        data = []
        current_directory = os.getcwd()
        filename = "Databases\Customer.csv"
        file_path = os.path.join(current_directory, filename)
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.password = password
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)

        for row in data:
            if row[4] == self.email:
                row[0] = firstName
                row[1] = lastName
                row[2] = (age)
                row[5] = password
                break

        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
            return self

    @staticmethod
    def register(firstName, lastName, age, walletzBalance: float, email, password):
        tmp = 0
        with open('Customer.csv', 'r+', newline='') as file:
            reader = csv.reader(file) 
            for row in reader:
                if(row[4] == email):
                    print("duplicate!")
                    tmp = 1
                    break
            
            if(tmp == 0):
                cus_tmp = customer(firstName, lastName, age, float(walletzBalance), email, password,"['None']")
                data = [[firstName, lastName, age, float(walletzBalance), email, password,cus_tmp.cart]]
                writer = csv.writer(file)
                writer.writerows(data)

    @staticmethod
    def changewalletzBalance(self,value):
        data = []
        with open('Customer.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)

        for row in data:
            if row[4] == self.email:
                row[3] = value
                break

        with open('Customer.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
