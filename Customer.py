import csv
from Human import human
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

    def __init__(self, firstName, lastName, age, walletzBalance:float, email, password):
        try:
            existing_email = set()
            with open('Customer.csv', 'r+', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    existing_email.add(row[4])

                if email in existing_email:
                    print("email exists!")
                else:
                    print(f"dear {firstName} welcome!")
                    super().__init__(firstName, lastName, age)
                    self.walletzBalance = walletzBalance
                    self.email = email
                    self.password = password
                    # Save information in file (csv)
                    data = [[firstName, lastName, age, walletzBalance, email, password]]
                    writer = csv.writer(file)
                    writer.writerows(data)

        except FileNotFoundError:
            with open('Customer.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                print("The file doesn't exists!")
    @staticmethod
    def changeFirstName(email,value):
        data = []
        with open('Customer.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)

        for row in data:
            if row[4] == email:
                row[0] = value
                break

        with open('Customer.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    @staticmethod
    def changeLastName(email,value):
        data = []
        with open('Customer.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)

        for row in data:
            if row[4] == email:
                row[1] = value
                break

        with open('Customer.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    @staticmethod
    def changewalletzBalance(email,value):
        data = []
        with open('Customer.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)

        for row in data:
            if row[4] == email:
                row[3] = value
                break

        with open('Customer.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    @staticmethod
    def changePassword(email,value):
        data = []
        with open('Customer.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)

        for row in data:
            if row[4] == email:
                row[5] = value
                break

        with open('Customer.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    
    @classmethod
    def showinformation(email, cls):
        data = []
        try:
            with open('Human.csv', 'r+', newline='') as file:
                reader = csv.reader(file)
                data = list(reader)
                cls.all = data
                for human in cls.all:
                    if(human[4] == email):
                        data.append([human[0], human[1], human[2], human[3], human[4], human[5]])
                headers = ["Name", "Last Name", "Age", "Wallet Balance", "Email", "Password"]
                table = tabulate(data, headers=headers, tablefmt="grid")
                print(table)
        except FileNotFoundError:
            with open('Customer.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                print("The file doesn't exists!")


if __name__ == "__main__":
    # Create instances of customer
    item1 = customer("amir","zahedi",20,500,"amir@gmail.com","1234")
    item2 = customer("mehdi","zahedi",20,500,"f@gmail.com","1234")
    item3 = customer("reza","zahedi",20,500,"g@gmail.com","1234")
    customer.changeFirstName("amir@gmail.com","lashi")
    '''
    # Access and modify attributes
    print(item1.name)  # Output: Product A
    print(item1.price)  # Output: 10.99
    print(item1.quantity)  # Output: 5

    item2.changePrice(955)
    # Print all goods
    print(Goods.all[0].name)  # Output: [Item('Product A',10.99,5), Item('Product B',5.99,0)]
    '''