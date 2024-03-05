# assignment on method overriding:
#Create a base class called “Vehicle” with method called “Drive”. Implement 2 subclasses,
#“Bike” and “Car” that inherit from “Vehicle” and override the “Drive” method with their own
#implementation

class Vehicle:
    def drive(self):
        print('drive method from Vehicle class')

class Bike(Vehicle):
    def drive(self):
        print("drive method from Bike class")

class Car(Vehicle):
    def drive(self):
        print("drive method from Car class")

bikobj = Bike()
carobj = Car()

bikobj.drive()
carobj.drive()

    
