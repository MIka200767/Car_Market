from person import Person
from read_file import Data


class Buyer(Person):
    def __init__(self, money,  bought_cars, filename):
        super().__init__(self.name, self.surname, self.city)
        self.money = money
        self.spend_money = 0
        self.bought_cars = bought_cars
        self.filename = filename
        self.data = Data()
        self.balance = self.data.read_file(self.filename)




        




