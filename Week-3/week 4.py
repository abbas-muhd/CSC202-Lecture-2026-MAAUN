from abc import ABC, abstractmethod
#ABBAS MUHAMMAD YUSUF
#MAAUN/24/CSC/0052

# Abstract Base Class
class StationAsset(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_revenue(self):
        pass


# Fuel Dispenser Class
class FuelDispenser(StationAsset):

    def __init__(self, name, price_per_liter, liters_sold):
        super().__init__(name)
        self.price_per_liter = price_per_liter
        self.liters_sold = liters_sold

    def calculate_revenue(self):
        return self.price_per_liter * self.liters_sold


# Car Wash Class
class CarWash(StationAsset):

    def __init__(self, name, price_per_wash, cars_washed):
        super().__init__(name)
        self.price_per_wash = price_per_wash
        self.cars_washed = cars_washed

    def calculate_revenue(self):
        return self.price_per_wash * self.cars_washed


# MAIN PROGRAM

# Create assets
dispenser1 = FuelDispenser("Pump 1", 650, 120)
dispenser2 = FuelDispenser("Pump 2", 650, 90)
carwash1 = CarWash("Main Wash", 2000, 15)

# Store assets in a list
station_assets = [dispenser1, dispenser2, carwash1]

total_revenue = 0

# Loop through assets
for asset in station_assets:
    revenue = asset.calculate_revenue()
    print(asset.name, "Revenue:", revenue)
    total_revenue += revenue

print("\nTotal Station Revenue:", total_revenue)