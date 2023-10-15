from read_file import Data
from car import Car
from seller import Seller


class CarMarket:
    def __init__(self, filename):
        self.info = Data()
        self.filename = filename
        self.car_park = self.info.read_file(filename)

    def add_car(self, car_obj, seller_obj):
        new_car = {
            "car mark": car_obj.mark,
            "car model": car_obj.model,
            "car color": car_obj.color,
            "car price": car_obj.price,
            "car year": car_obj.year,
            "Seller": {
                "Seller name": seller_obj.name,
                "Seller surname": seller_obj.surname,
                "Seller city": seller_obj.city,
            }
        }
        self.car_park[car_obj.uuid] = new_car
        self.info.write_file(self.filename, self.car_park)

    def remove_car(self, car_obj):
        print(self.car_park)
        print(car_obj.uuid in self.car_park.keys())
        if car_obj.uuid in self.car_park:
            self.car_park.pop(car_obj.uuid)
            self.info.write_file(self.filename, self.car_park)
            # del self.car_park[car_obj.uuid]
        else:
            print(f"the car with uuid {car_obj.uuid} is not found")


if __name__ == '__main__':
    car_file = "cars.json"
    data = Data()
    balance_seller_file = "balance.json"
    car = Car("mercedes", "E_class", "white", 20000, 2007)
    seller = Seller("mika", "aydinyan", "yerevan", 0, car_file, data, balance_seller_file)

    cm = CarMarket(car_file)
    # cm.add_car(car, seller)
    seller.sell(car)
    # cm.remove_car(car)
