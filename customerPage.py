from Customer import customer
from goods import Goods
import os
import csv

def check(productDict):# a function to check a valid order

    existing_names = {}

    if os.path.exists('Product.csv'):
        with open('Product.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                existing_names[row[0]] = int(row[2])

        for key in productDict:
            if key not in existing_names or existing_names[key] < productDict[key]:
                print("Bad!")
                return False

        return True

    return False

def check_login(email, password):
    with open('Customer.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[4] == email and row[5] == password:
                tmp_cus = customer(row[0], row[1], row[2], row[3], row[4], row[5])
                return True, tmp_cus
        return False, None

def main():
    email = input('Please enter your email: ')
    password = input('Please enter your password: ')
    
    success, tmp_cus = check_login(email, password)
    
    if success:
        print('Login successful!')
        return True, tmp_cus
    else:
        print('Invalid login credentials!')
        return False, None
accept, cus_tmp = main()  
def customer_handler():
    while(1):
        print("1-show goods 2-show information")
        choose = int(input())
        if(choose == 1):
            Goods.showGoods()
            #Iphone13:5-galaxy s21:1
            print("--------------------------------------------------")
            user_input = input("if you whould to buy something please write this:\nproduct A: 5 - product B: 2\n")
            productDict = {}  # Dictionary for storing products

            items = user_input.split('-')  # Splitting different products

            for item in items:
                name, quantity = item.split(':')
                productDict[name.strip()] = int(quantity)
            


            if(check(productDict)):
                print("Ok!")
                for key in productDict:
                    cus_tmp.addProduct(key)

            else:
                print("Not ok")





while(1):
    if(accept == True):
        print("welcome")
        customer_handler()
    else:
        print(2)

        
    
