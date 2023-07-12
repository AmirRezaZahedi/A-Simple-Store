import csv
from Human import human
from goods import Goods
from tabulate import tabulate

class AttributeDescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("walletzBalance cannot be negative")
        instance.__dict__[self.name] = value


class customer(human):

    all = []
    walletzBalance = AttributeDescriptor('walletzBalance')

    def __init__(self, firstName, lastName, age, walletzBalance: float, email, password):
        super().__init__(firstName, lastName, age)
        self.walletzBalance = walletzBalance
        self.email = email
        self.password = password

    @staticmethod
    def login(username, password):
        with open('Customer.csv', 'r+', newline='') as file:
            reader = csv.reader(file)
        for row in reader:
            if row[4] == username and row[5] == password:
                print("successfull . . .")
                return customer(row[0],row[1],row[2],float(row[3]),row[4],row[5])
            else:
                print("Bad . . .")

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
            
            if(tmp != 1):
                data = [[firstName, lastName, age, walletzBalance, email, password]]
                writer = csv.writer(file)
                writer.writerows(data)

    def addProduct(self, name):
        data = []
        try:
            with open('Product.csv', 'r+', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if(row[0] == name and row[2] != '0' and int(self.walletzBalance) >= int(row[1])):
                        self.cart.append(row)
                        
                        with open('Customer.csv', 'r', newline='') as file:
                            reader = csv.reader(file)
                            data = list(reader)

                        for row in data:
                            if row[4] == self.email:
                                row[6] = self.cart
                                break

                        with open('Customer.csv', 'w', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerows(data)
                            
        except FileNotFoundError:
                with open('Product.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    print("The file doesn't exists!")

    @staticmethod
    def changeFirstName(self,value):
        data = []
        with open('Customer.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)

        for row in data:
            if row[4] == self.email:
                row[0] = value
                break

        with open('Customer.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    @staticmethod
    def changeLastName(self,value):
        data = []
        with open('Customer.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)

        for row in data:
            if row[4] == self.email:
                row[1] = value
                break

        with open('Customer.csv', 'w', newline='') as file:
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

    @staticmethod
    def changePassword(self,value):
        data = []
        with open('Customer.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)

        for row in data:
            if row[4] == self.email:
                row[5] = value
                break

        with open('Customer.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    @staticmethod
    def login(email, password):
        data = []
        with open('Customer.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)

        for row in data:
            if row[4] == email and row[5] == password:
                return customer(row[0],row[1],row[2],float(row[3]),row[4],row[5])

    def showinformation(self):
        data = []
        try:
            with open('Human.csv', 'r+', newline='') as file:
                reader = csv.reader(file)

                for row in reader:
                    if(row[4] == self.email):
                        data.append([row[0], row[1], row[2], row[3], row[4], row[5]])
                headers = ["Name", "Last Name", "Age", "Wallet Balance", "Email", "Password"]
                table = tabulate(data, headers=headers, tablefmt="grid")
                print(table)
        except FileNotFoundError:
            with open('Customer.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                print("The file doesn't exists!")