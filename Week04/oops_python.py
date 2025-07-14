# create Car class and create objects
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.milage = 0

    def drive(self, miles):
        self.milage += miles
        print(f"Driving {miles} miles.")

    def display_info(self):
        print(f"{self.make} {self.year} {self.model} | Milage: {self.milage} miles")
    
    def honk(self):
        print(f"Beep Beep!")

# create car object
car1 = Car("Toyota", "2025", "Crysta")
car2 = Car("Suzuki", "2024", "Dzire")

car1.drive(20)
car1.display_info()
car1.honk()

car2.drive(25)
car2.display_info()
car2.honk()

# Inheritance fro Car
class ElecticCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size
        self.charge_level = 100
    
    def charge(self, percentage):
        self.charge_level = min(100, self.charge_level + percentage)
        print(f"Charged to {self.charge_level}%")
    
    def drive(self, miles):
        super().drive(miles)
        self.charge_level -= miles / 5
        print(f"Battery: {self.charge_level}%")

# create electric car
mahindra = ElecticCar("Mahindra", "EVD3", 2025, 75)
mahindra.drive(25)
mahindra.charge(30)
mahindra.display_info()