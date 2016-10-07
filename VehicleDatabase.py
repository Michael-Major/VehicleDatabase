#HW10: Inheritance
#Author: Michael Major

class Vehicle():
    def __init__(self, make=None, model=None, year=None, mileage=None, price=None):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.price = price
        
    def Display(self):
        print("Make:",self.make,"\nModel:",self.model,"\nYear:",self.year,"\nMileage:",self.mileage,"\nPrice:",self.price)

    def getMake(self):
        return self.make
    def getModel(self):
        return self.model
    def getYear(self):
        return self.year
    def getMileage(self):
        return self.mileage
    def getPrice(self):
        return self.price

    def setMake(self,make):
        self.make = make
    def setModel(self, model):
        self.model = model
    def setYear(self, year):
        self.year = year
    def setMileage(self, mileage):
        self.mileage = mileage
    def setPrice(self, price):
        self.price = price

class Truck(Vehicle):
    def __init__(self, make=None, model=None, year=None, mileage=None, price=None,driveType=None):
        super().__init__(make,model,year,mileage,price)
        self.driveType = driveType
        
    def getDriveType(self):
        return self.driveType
    def setDriveType(self,driveType):
        self.driveType = driveType

    def Display(self):
        print("Invenotry Unit: Truck")
        super().Display()
        print("Drive Type:",self.driveType)
        
class SUV(Vehicle):
    def __init__(self, make=None, model=None, year=None, mileage=None, price=None,capacity=None):
        super().__init__(make,model,year,mileage,price)
        self.capacity = capacity
        
    def getCapacity(self):
        return self.capacity
    def setCapacity(self,capacity):
        self.capacity = capacity

    def Display(self):
        print("Inventory Unit: SUV")
        super().Display()
        print("Passenger Capacity:",self.capacity)

class Car(Vehicle):
    def __init__(self, make=None, model=None, year=None, mileage=None, price=None,numDoors=None):
        super().__init__(make,model,year,mileage,price)
        self.numDoors = numDoors
        
    def getNumDoors(self):
        return self.numDoors
    def setNumDoors(self,numDoors):
        self.numDoors = numDoors

    def Display(self):
        print("Inventory Unit: Car")
        super().Display()
        print("Number of Doors:",self.numDoors)

class Inventory():
    def __init__(self):
        self.vlist = []
    def addVehicle(self,vehicle):
        self.vlist.append(vehicle)
    def Display(self):
        for vehicle in self.vlist:
            vehicle.Display()
            print("\n")
def main():
    done = False
    vehicles = Inventory()

    while done == False:
        
        vehicleType = str(input("Enter vehicle type: "))
        make = str(input("Enter vehicle make: "))
        model = str(input("Enter vehicle model: "))
        year = eval(input("Enter vehicle year: "))
        mileage = eval(input("Enter vehicle mileage: "))
        price = eval(input("Enter vehicle price: "))

        if vehicleType.lower() == "suv":
            lastItem = eval(input("Enter passenger capacity: "))
            vehicles.addVehicle(SUV(make,model,year,mileage,price,lastItem))
        elif vehicleType.lower() == "car":
            lastItem = eval(input("Enter number of doors: "))
            vehicles.addVehicle(Car(make,model,year,mileage,price,lastItem))
        else:
            lastItem = str(input("Enter drive type: "))
            vehicles.addVehicle(Truck(make,model,year,mileage,price,lastItem))

        response = str(input("Would you like to add another vehicle? (y/n): "))
        if response.lower() == 'n':
            done = True
            print()

    vehicles.Display()

main()
