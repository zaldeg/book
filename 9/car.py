"""Class for describing any car"""


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('Whattafuck?')

    def increment_odometer(self, miles):
        self.odometer_reading += miles


'''Simple model of Battery'''


class Battery:
    def __init__(self, battery_size=60):
        self.battery_size = battery_size

    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + 'kW/h battery.')

    def get_range(self):
        print('Range which can go this car is', self.battery_size * 3, 'miles')


"""Subclass ElectricCar for class Car"""


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
