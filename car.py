import uuid


class Car:
    def __init__(self, mark, model, color, price, year):
        if isinstance(mark, str) and isinstance(model, str) and isinstance(color, str) and isinstance(price, int) and \
                isinstance(year, int):
            self._uuid = str(uuid.uuid4())
            self._mark = mark
            self._model = model
            self._color = color
            self._price = price
            self._year = year
        else:
            raise TypeError

    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        self._uuid = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def mark(self):
        return self._mark

    @mark.setter
    def mark(self, value):
        self._mark = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

