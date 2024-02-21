# Duck Typing:

class Honda:
    def max_speed(self):
        print('max speed of Honda is 220 KMPH')

    def fuel_type(self):
        print('fuel_type of Honda is Diesel')

    def transmission(self):
        print('transmission of Honda is Manual')

class Skoda:
    def max_speed(self):
        print('max speed of Skoda is 280 KMPH')

    def fuel_type(self):
        print('fuel_type of Skoda is Petrol')

city = Honda()
slavia = Skoda()

def get_car_info(obj):
    obj.max_speed()
    obj.fuel_type()

get_car_info(city)
    
