class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")


class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        print("Sail!")


class Plane(Vehicle):
    def move(self):
        print("Fly!")


car1 = Car("Ford", "Mustang")
boat1 = Boat("Ford", "Mustang")
plane1 = Plane("Ford", "Mustang")

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()
