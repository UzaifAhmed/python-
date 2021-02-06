class Car(): 
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def fill_gas_tank(self):        
        print("This car is filling gas tank!")
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class battery():
    def __init__(self,amp,plates,manuf):
        self.amp = amp
        self.plates = plates
        self.manuf = manuf
    
    def get_amp(self):
        return self.amp
    
        
class  Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def open_restaurant(self):
        return f"{self.restaurant_name} is open, Enjoy the {self.cuisine_type}"

def addisional_fun():
    print('I am additional function')