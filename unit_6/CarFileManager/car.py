class Car:

    def __init__(self, type):
        self.__type = type

    def display_type(self):
        print("This car type is:", self.__type)
