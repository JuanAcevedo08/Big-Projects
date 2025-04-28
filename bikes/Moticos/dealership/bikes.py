import time
import random

class Bike:
    def __init__(self, bike_id: int, brand: str, model: str, price: float):
        self.brand = brand
        self.model = model
        self.price = price
        self.bike_id = bike_id
        self.availability = True     

class BikeDealership:
    def __init__(self):
        self.bikes = {}

    def add_bike(self, bike: object):
        self.bikes[bike.bike_id] = bike
        print("Adding bike...")
        time.sleep(random.randint(1,3))
        print(f"Bike {bike.model} added to the dealership")

    def remove_bike(self, bike: object):
        if bike.bike_id in self.bikes:
            del self.bikes[bike.bike_id]
            print("Removing bike...")
            time.sleep(random.randint(1,3))
            print(f"Bike {bike.brand} {bike.model} removed successfully")
            return 
        print("Bike not found")

    def show_bikes(self):
        for bike in self.bikes.values():
            print(f"Bikes: - Brand: {bike.brand}  Model: {bike.model} Price: {bike.price}")
    
    def check_availability(self, bike_id: int) -> bool:
        print("Searching for bike...")
        time.sleep(1.5)
        for i in self.bikes.keys():
            if i == bike_id:
                print(f"Bike available. Retrieving information...")
                return True
            else:
                print("Bike not available")
                return False
    
    def show_bike(self, bike_id: object):
        print("Showing bike...")
        time.sleep(2)
        for k, v in self.bikes.items():
            if k == bike_id:
                print(f"Brand: {v.brand} Model: {v.model} Price: {v.price}")
            

            

bike1 = Bike(1, "Suzuki", "GSXR-R 1000R", 40_000)
#bike2 = Bike(2, "Kawasaki", "Z900", 43_000)
#dealership = Dealership()
#dealership.add_bike(bike1)
#dealership.add_bike(bike2)
#dealership.show_bikes()
#dealership.check_availability(2)
