class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it')

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Don't try to cheat with me Bitch!!! I'll find you")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


class Battery:
    def __init__(self):
        self.battery_size = 70

    def describe_battery(self):
        print('Battery size is : ', self.battery_size)

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        print("This car can go approximately " + str(range) + " miles on full charge")

    def update_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


tesla = ElectricCar('tesla', 'model S', 2012)
print(tesla.get_descriptive_name())
tesla.battery.describe_battery()
tesla.battery.get_range()
tesla.battery.update_battery()
tesla.battery.get_range()