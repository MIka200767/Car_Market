from person import Person
# from read_file import Data


class Seller(Person):
    def __init__(self, name, surname, city, money, cars, data, filename_balance):
        super().__init__(name, surname, city)
        self._money = money
        self.data = data
        self.cars = data.read_file(cars)
        self.filename_balance = filename_balance

    def sell(self, car_obj):
        print(car_obj.__dict__)
        for i in self.cars.keys():
            if car_obj.uuid in self.cars.keys():
                print("Hello")
            self.change_money(car_obj)
            self. cars.pop(car_obj.model)

    def change_money(self, car_obj):
        self._money += car_obj.price
        balance_data = {
            "seller_money": self._money
        }
        self.data.write_file(self.filename_balance, balance_data)

    def return_car(self, car_obj):
        self.data.write_file(self.cars, car_obj)

        self.data.write_file(self.filename_balance, )

    def get_available_cars(self):
        pass

    def check_discount(self):
        pass

    def add_sold_cars(self):
        pass


