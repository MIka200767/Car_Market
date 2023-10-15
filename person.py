class Person:
    def __init__(self, name, surname, city):
        self._name = name
        self._surname = surname
        self._city = city

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

