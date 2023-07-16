

ui, _ = loadUiType('front\Login.ui')

class MainApp(QMainWindow,ui):
        def __init__(self):
            QMainWindow.__init__(self)
            self.setupUi(self)
            self.tabWidget.setCurrentIndex(0)
            self.LOGINBUTTONCUS.clicked.connect(self.login)



'''def customer_handler(cus_tmp):
    while(1):
        print("1-show goods 2-show information 3-complete buy")
        choose = int(input())
        if(choose == 1 and len(cus_tmp.cart) == 1):
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
                for key,value in productDict.items():
                    cus_tmp.addProduct(key,value)

            else:
                print("Not ok")
        
        elif(choose == 2):
            cus_tmp.showinformation()

        elif(choose == 3):
            with open('Customer.csv', 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if(row[0] == cus_tmp.firstName and len(eval(row[6]))):
                        pass'''








def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()    

        


