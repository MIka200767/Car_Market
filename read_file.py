import json


class Data:
    def read_file(self, filename):
        with open(filename, 'r') as file:
            return json.load(file)

    def write_file(self, filename, data):
        with open(filename, 'w') as file:
            return json.dump(data, file, indent=4)

