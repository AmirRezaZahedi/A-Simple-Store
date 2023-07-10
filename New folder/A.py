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
        print("Good created.")
        # Run validations on the received arguments
        assert Price >= 0, f"{Price} is wrong"
        assert Quantity >= 0, f"{Quantity} is wrong"

        # Assign to self objects
        self.name = Name
        self.price = Price
        self.quantity = Quantity

        # Action to execute
        Goods.all.append(self)
    
    def changePrice(self):
    # Python code to illustrate split() function
        with open("Product.txt", "a") as file:
            data = file.readlines()
            for line in data:
                word = line.split()
                print (word)


        



if __name__ == "__main__":
    # Create instances of Goods
    item1 = Goods("Product A", 10.99, 5)
    item2 = Goods("Product B", 5.99)

    # Access and modify attributes
    print(item1.name)  # Output: Product A
    print(item1.price)  # Output: 10.99
    print(item1.quantity)  # Output: 5

    item1.name = "Updated Product A"
    item1.price = 15.99
    item1.quantity = 1

    print(item1.name)  # Output: Updated Product A
    print(item1.price)  # Output: 15.99
    print(item1.quantity)  # Output: 10

    # Print all goods
    print(Goods.all)  # Output: [Item('Product A',10.99,5), Item('Product B',5.99,0)]
