class AttributeDescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

class human:
    firstName = AttributeDescriptor('firstName')
    lastName = AttributeDescriptor('lastName')
    age = AttributeDescriptor('age')
    Id = AttributeDescriptor('Id')

    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age