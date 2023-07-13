from prettytable import PrettyTable
from colorama import Fore, Style
from termcolor import colored
import csv
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

    all = []
    name = AttributeDescriptor("name")
    price = AttributeDescriptor("price")
    quantity = AttributeDescriptor("quantity")

    def __init__(self, Name: str, Price: float, Quantity=0):
        # Run validations on the received arguments
        assert Price >= 0, f"{Price} is wrong"
        assert Quantity >= 0, f"{Quantity} is wrong"
        try:
            existing_names = set()
            with open('Product.csv', 'r+', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    existing_names.add(row[0])

                if Name in existing_names:
                    print("Product exists with this name!")
                else:
                    print(f"The product created\nname is : {Name}.")
                    self.name = Name
                    self.price = Price
                    self.quantity = Quantity
                    # Save information in file (csv)
                    data = [[self.name, str(self.price), str(self.quantity)]]
                    writer = csv.writer(file)
                    writer.writerows(data)
                    
        except FileNotFoundError:
            with open('Product.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                print("The file doesn't exists!")

    @staticmethod
    def changePrice(name, value):#function to change price
        data = []
        with open('Product.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)

        for row in data:
            if row[0] == name:
                row[1] = str(value)
                break

        with open('Product.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    @staticmethod
    def changeQuantity(name, quantity):#function to change quantity
        data = []
        with open('Product.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)

        for row in data:
            if row[0] == name:
                row[2] = str(quantity)
                break

        with open('Product.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    @classmethod
    def showGoods(cls):
        try:
            with open('Product.csv', 'r+', newline='') as file:
                reader = csv.reader(file)
                data = list(reader)
                cls.all = data
                
                table = PrettyTable()
                table.field_names = [colored("Item", "blue"), colored("Name", "blue"), colored("Price", "blue"), colored("Quality", "blue")]
                table.title = colored("Goods List", "green")
                table.align = "l"
                
                for i in range(len(cls.all)):
                    table.add_row([f"Item {i+1}", cls.all[i][0], cls.all[i][1], cls.all[i][2]])
                
                print(Fore.YELLOW + table.get_string() + Style.RESET_ALL)
                
        except FileNotFoundError:
            with open('Product.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                print("The file doesn't exist!")




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
