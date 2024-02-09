#OOP task:

#Class car

class Car:
    car_name = 'Polo'
    car_model = 1.0
    color = 'red'


a1 = Car()
print(a1.car_name)

gsk = Car()

gsk.car_name = 'Veerna'
gsk.car_model = 5.0
gsk.color = 'Black'
gsk.company = "Tata"

print("GSK car name:",gsk.car_name)
print("Car model: ",gsk.car_model)
print("Car color= ",gsk.color)
print(gsk.company)


#Class laptop:

class Laptop:
    name = 'lenovo'
    model = 10
    ram = 8
    processor = 'i5'
    storage = 1000

L1 = Laptop()
L1.name= 'Dell'
L1.model = 1.11
L1.RAM = 8
L1.processor = 'i7'
L1.storage = 512

print("L1.name",L1.name)
print("L1.model",L1.model)
print("L1.RAM",L1.ram)
print("L1.processor",L1.processor)
print("L1.storage",L1.storage)


class Employee():
    emp_name = 'Defalt'
    emp_id = 0000
    salary = 1000

e1 = Employee()
e1.emp_name = 'john'
e1.emp_id = 1213
e1.salary = 8000

print("emp name= ",e1.emp_name)
print("emp_id= ",e1.emp_id)
print("salary= ",e1.salary)
    
class Bank():
    acc_number = 0000
    balance = 1000

c1 = Bank()
c1.acc_number = 1020
c1.balance = 5500

print("c1.acc_number",c1.acc_number)
print("c1.balance",c1.balance)

print()

class Bike():
    bike_name = 'KTM'
    milage = 15
    engine = 'petrol'

b1 = Bike()
b1.bike_name = 'Shine125'
b1.milage = 60
b1.engine = 'petrol'

print(b1.bike_name)
print(b1.milage)
print(b1.engine)

print()
b2 = Bike()

b2.bike_name = 'OLA S1'
b2.milage = 60
b2.engine = 'electric'

print("b2.bike_name=",b2.bike_name)
print("b2.milage=",b2.milage)
print("b2.engine=",b2.engine)