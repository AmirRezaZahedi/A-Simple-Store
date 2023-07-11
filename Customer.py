import csv
from Human import human

class customer(human):
    all = []
    
    def __init__(self, firstName, lastName, age, walletzBalance, email):
        try:
            existing_email = set()
            with open('Customer.csv', 'r+', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    existing_email.add(row[0])

                if email in existing_email:
                    print("email exists!")
                else:
                    print(f"dear {self.name} welcome!")
                    super().__init__(firstName, lastName, age)
                    self.walletzBalance = walletzBalance
                    self.email = email
                    # Save information in file (csv)
                    data = [[firstName, lastName, age, walletzBalance, email]]
                    writer = csv.writer(file)
                    writer.writerows(data)
                    # Action to execute
                    customer.all.append(self)
        except FileNotFoundError:
            with open('Customer.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                print("The file doesn't exists!")

    def changeFirstName(self,value)
