class AttributeDescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

class human:
    Id_counter = 0
    firstName = AttributeDescriptor('firstName')
    lastName = AttributeDescriptor('lastName')
    age = AttributeDescriptor('age')
    Id = AttributeDescriptor('Id')

    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        human.Id_counter += 1
        self.Id = human.Id_counter