

class Car:
    def __init__(self, color, brand):
        self.color = color  # Атрибут: цвет машины
        self.brand = brand  # Атрибут: марка машины
        self.mileage = 0
    
    def drive(self, distance=0):
        self.mileage += distance
        print(f"Машина {self.brand} цвета {self.color} проехала {distance} км. Общий пробег: {self.mileage} км.")
    
    def honk(self):
        print("Бип-бип!")

my_car = Car("красный", "Toyota")
friend_car = Car("синий", "BMW")

my_car.drive(15)
friend_car.honk()