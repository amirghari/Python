# Part 1
class Publication:
    def __init__(self, book_count: int, author: str):
        self.book_count = book_count
        self.author = author

    def magazine(self, editor: str):
        self.editor = editor


class Book(Publication):
    def __init__(self, book_count: int, author: str):
        self.book_count = book_count
        self.author = author
        super(Book, self).__init__(book_count, author)

    def __str__(self):
        return f"The number of book pages is {self.book_count} and the author is {self.author}."


class Magazine(Publication):
    def __init__(self, chief_editor: str):
        self.chief_editor = chief_editor
        super(Magazine, self).magazine(chief_editor)

    def __str__(self):
        return f"The chief editor of the magazine is {self.chief_editor}."


Donald_Duck = Magazine("Aki Hyyppä")
Compartment_No_6 = Book(192, "author Rosa Liksom")
print(Donald_Duck)
print(Compartment_No_6)

# Part 2

class car:
    def __init__(self, regNumber, maxSpeed):
        self.regNum = regNumber
        self.maxSpeed = maxSpeed
        self.curSpeed = 0
        self.travelledDistance = 0

    def accelerate(self, speed):
        self.curSpeed += speed
        if self.curSpeed < 0:
            self.curSpeed = 0
        elif self.curSpeed > self.maxSpeed:
            self.curSpeed = self.maxSpeed
        return self.curSpeed

    def drive(self, hours):
        self.travelledDistance += self.curSpeed * hours
        return self.travelledDistance


class ElectricCar(car):
    def __init__(self, regNumber, maxSpeed, battCap):
        super().__init__(regNumber, maxSpeed)
        self.battCap = battCap


class GasolineCar(car):
    def __init__(self, regNumber, maxSpeed, tankVol):
        super().__init__(regNumber, maxSpeed)
        self.tankVol = tankVol


new_ecar = ElectricCar("ABC-15", 180, 52.5)
new_ecar.accelerate(80)
new_ecar.drive(3)
print(f"Electric car travelled: {new_ecar.travelledDistance} km")
new_gcar = GasolineCar("ACD-123", 165, 32.3)
new_gcar.accelerate(120)
new_gcar.drive(3)
print(f"Gasoline car travelled: {new_gcar.travelledDistance} km")
