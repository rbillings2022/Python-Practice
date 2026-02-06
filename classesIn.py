# Classes are blueprints for objects
# Attributes are data the object has - Noun
#    - A variable attached to an object - self.color
# Methods are data the object can do - Verb

# Class: Car
# Attributes (What it has): color, speed, fuel
# Methods (what it does): accelerate(), brake(), refuel()

class Car:
    def __init__(self, color, fuel):
        self.color = color     # attribute
        self.fuel = fuel       # attribute
        self.speed = 0         # attribute

    def accelerate(self):      # method
        self.speed += 10

    def brake(self):           # method
        self.speed -= 5

# Using attributes
car = Car("red", 50)

print(car.color)   # "red"
print(car.speed)   # 0
