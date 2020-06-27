class Empresa:
    def __init__(self, lenguages):
        self.lenguages = lenguages
    def getInformation(self):
        return {
            self.lenguages
        }
class Coche(Empresa):
## when a property has __ it means that is private
    __color = "red"
    __brand = "Mazda"
    __speed = 0
    def __init__(self, color, brand, speed):
        self.color = color
        self.brand = brand
        self.speed = speed
    def accelaterate(self):
        self.speed += 1
    def down_speed(self):
        self.speed -= 1
    def getSpeed(self):
        return self.speed
    def setColor(self, color):
        self.color = color
    def getColor(self):
        return self.color
    def getInfo(self):
        return {
            "Color": self.color,
            "Marca": self.brand,
            "Velocidad": self.speed
        }
class Garage(Coche):
    def __init__(self, color, brand, speed):
        super().__init__(color, brand, speed)
        self.audite = True
    def geAudite(self):
        return self.audite
    
