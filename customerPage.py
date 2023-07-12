from Customer import customer
import csv

item1 = customer.register("amir","zahedi",20,500,"amir@gmail.com","1234")
item2 = customer.register("mehdi","zahedi",20,500,"f@gmail.com","1234")
item3 = customer.register("reza","zahedi",20,5000,"g@gmail.com","1234")
item_fake_3 = customer.login("g@gmail.com","1234")
customer.changeFirstName("amir@gmail.com","free")

        
    
