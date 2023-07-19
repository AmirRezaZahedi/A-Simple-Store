import csv
import os

class MyCart:
    def __init__(self, cart):
        self.cart = cart
    
    def addProduct(self, ProductDict):
        ProductDatabase = os.path.join(os.getcwd(), "Databases", "Product.csv")
        CustomerDatabase = os.path.join(os.getcwd(), "Databases", "Customer.csv")
        flagCheck = True
        CartProduct = {}
        
        # Check product availability and update CartProduct
        try:
            with open(ProductDatabase, 'r+',newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if (row[0] in ProductDict):
                        if (ProductDict.get(row[0]) > int(row[2])):
                            flagCheck = False
                            return flagCheck
                        else:
                            CartProduct.update({row[0] : ProductDict.get(row[0])})

                tmp = eval(self.cart)#list of customer's cart
                for i in range(1,len(tmp)):
                    SplitItem = tmp[i].split(":")
                    key = SplitItem[0]
                    value = SplitItem[1]
                    if(key in CartProduct):
                        tmp[i] = f"{key}:{int(CartProduct[key])}"
                        del CartProduct[key]
                        print(tmp[i])
                
                for key, value in CartProduct.items():
                    tmp.append(f"{key}:{value}")
                with open(CustomerDatabase, 'r+', newline='') as file:
                    reader = csv.reader(file)
                    data = list(reader)
                    self.cart = tmp
                    for row in data:
                        if row[4] == self.email:
                            row[6] = self.cart
                            break

                with open(CustomerDatabase, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(data)

                return flagCheck
        except FileNotFoundError:
            with open('Product.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                print("The file doesn't exists!")
        
        # Update existing products in cart
        for i in range(1, len(self.cart)):
            key, value = self.cart[i].split(":")
            if key in CartProduct:
                quantity = min(int(CartProduct[key]), int(value))
                self.cart[i] = f"{key}:{quantity}"
                del CartProduct[key]
        
        # Add new products to cart
        for key, value in CartProduct.items():
            self.cart.append(f"{key}:{value}")
        
        # Update cart in the Customer database
        with open(CustomerDatabase, 'r+', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)
            for row in data:
                if row[4] == self.email:
                    row[6] = self.cart
                    break
        
        with open(CustomerDatabase, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        
        return flagCheck