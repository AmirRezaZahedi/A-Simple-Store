from goods import Goods
from Customer import customer

print("Dear admin welcome.")
print("It's your page to controll Goods, ...!")
print("1-add Item 2-change customer's information with email 3-change Item")
input("test:")
if(True):
    name = input("name: ")
    price = int(input("price: "))
    quantity = int(input("quantity: "))

    item1 = Goods(name, price, quantity)
