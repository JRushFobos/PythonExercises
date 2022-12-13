class Car:
    wheels = 4

    def __init__(self, name, color, year, is_crashed):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed

    def drive(self, city):
        #city без self
        print(f'{self.name} is driving to {city}')

    def __str__(self):
        return (f'{self.name} {self.color} {self.year} {self.is_crashed}')

mazda = Car('Mazda', 'Black', 2001, True)
print(mazda)
print(Car.wheels)