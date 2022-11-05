import random
from prettytable import PrettyTable


class Car:
    def __init__(self, reg_num, max_speed, current_speed=0, travelled_distance=0):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def Acceleration(self, acceleration):
        self.acceleration = acceleration
        self.max_speed += self.acceleration
        # print(f"The speed is {self.max_speed}")
        if self.max_speed < 0:
            self.max_speed = 0
            # print(f"The speed is {self.max_speed}")

    def drive(self, hours):
        self.hours = hours
        self.travelled_distance += self.hours * self.max_speed
        # print(f"The Travelled distance is {self.travelled_distance}")


new_car = Car("ABC-123", 142)
print(f"New car's properties are as follows:")
print(f"registration Number: {new_car.reg_num}")
print(f"Maximum speed: {new_car.max_speed}")
print(f"Current Speed: {new_car.current_speed}")
print(f"Travelled Distance: {new_car.travelled_distance}")

new_car.Acceleration(30)
new_car.Acceleration(70)
new_car.Acceleration(-200)
new_car.Acceleration(18)
new_car.drive(1.5)

cars_list = []
overall_distance = 0

for i in range(10):
    car_name = "ABC-" + str(i + 1)
    car_list = []
    car_list.append(car_name)
    max_speed = random.randrange(100, 200)
    car = Car(car_name, max_speed)
    changed_speed = random.randint(-10, 15)
    car.Acceleration(changed_speed)
    car_list.append(car.max_speed)
    car.drive(1)
    distance = car.travelled_distance
    car_list.append(distance)
    cars_list.append(car_list)
# print(cars_list)
while overall_distance < 10000:
    for i in range(10):
        max_speed = random.randrange(100, 200)
        changed_speed = random.randint(-10, 15)
        car = Car(car_name, max_speed)
        car.Acceleration(changed_speed)
        cars_list[i][1] = car.max_speed
        car.drive(1)
        cars_list[i][2] += car.travelled_distance
        overall_distance = cars_list[i][2]
        if overall_distance > 10000:
            break

table = PrettyTable(["Car Name", "Speed", "Travelled Distance"])
for i in cars_list:
    car_name = i[0]
    max_speed = i[1]
    travelled_distance = i[2]
    table.add_row([car_name, max_speed, travelled_distance])
print(table.get_string(sortby="Travelled Distance", reversesort=True))
