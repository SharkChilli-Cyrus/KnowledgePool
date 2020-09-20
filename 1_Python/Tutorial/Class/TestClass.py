class Dog():
    def __init__(self, name, age):
        self.name = name.title()
        self.age = age
    
    def sit(self):
        print("{0} is now sitting".format(self.name.title()))
    
    def roll_over(self):
        print("{0} rolled over".format(self.name.title()))

# my_dog = Dog('willie', 6)
# print("My dog's name is {0}.\nMy dog is {1} years old.".format(my_dog.name, my_dog.age)) 


class Car():
    """Class Description"""

    def __init__(self, make, model, year):
        """Function Description"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Function Description"""
        long_name = "{0} {1} {2}".format(self.year, self.make, self.model)
        return long_name.title()
    
    def update_odometer(self, mileage):
        """Function Description"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can not roll back an odometer")
    
    def increment_odometer(self, miles):
        """Function Description"""
        self.odometer_reading += miles

    def read_odometer(self):
        """Function Description"""
        print("This car has {0} miles on it".format(self.odometer_reading))
    
    def fill_gas_tank(self):
        pass
    
# my_new_car = Car('BMW', '730', 2022)
# print(my_new_car.get_descriptive_name())

# my_new_car.odometer_reading = 23
# my_new_car.update_odometer(10)
# my_new_car.increment_odometer(100)
# my_new_car.read_odometer()


class Battery():
    """Class Description"""

    def __init__(self, battery_size=80):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print("This car has a {0}-kwh battery".format(self.battery_size))

    def get_range(self):
        if self.battery_size == 80:
            range = 240
        elif self.battery_size == 95:
            range = 300
        else:
            range = 'unknown'

        message = "This car can go approximately {0} miles on a full charge".format(range)
        print(message)


class ElectricCar(Car):
    """Class Description"""
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # self.battery_size = 70
        self.battery = Battery()
    
    # def describe_battery(self):
    #     print("This car has a {0}-kwh battery".format(self.battery_size))
    
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank")

my_tesla = ElectricCar('tesla', 'model s', 2022)
print(my_tesla.get_descriptive_name())
my_tesla.fill_gas_tank()

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()