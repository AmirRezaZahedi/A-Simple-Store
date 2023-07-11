class AttributeDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

class human:
    Id_counter = 0
    firstName = AttributeDescriptor()
    lastName = AttributeDescriptor()
    age = AttributeDescriptor()
    Id = AttributeDescriptor()

    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        human.Id_counter += 1
        self.Id = human.Id_counter