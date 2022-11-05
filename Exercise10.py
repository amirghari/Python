import random
from tabulate import tabulate


# Part 1-2-3
class Building:
    def __init__(self, elevators_no, bottom_floor, top_floor):
        self.elevators_no = elevators_no
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []
        for i in range(self.elevators_no):
            elevator = [i + 1, self.bottom_floor, self.top_floor]
            self.elevators.append(elevator)

    def run_elevator(self, elev_num, floor):
        for i in range(self.elevators_no):
            if elev_num == self.elevators[i][0]:
                bottom = self.elevators[i][1]
                top = self.elevators[i][2]
                elev_travel = Elevator(floor, bottom, bottom, top)
                print(f'You are in Elevator number {i + 1}.')
                print(f'The current floor is {elev_travel.current_floor}!')
                return elev_travel.current_floor

    def fire_alarm(self):
        fire_alarm_travel = Elevator(self.bottom_floor, self.bottom_floor, self.bottom_floor, self.top_floor)
        print(f'Due to emergency situation the current floor is {fire_alarm_travel.current_floor}!')


class Elevator:
    def __init__(self, go_to_floor: int, current_floor, bottom_floor: int, top_floor: int):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor
        if bottom_floor <= go_to_floor < current_floor:
            for i in range(-(go_to_floor - current_floor)):
                self.go_down()
        elif top_floor >= go_to_floor > current_floor:
            for i in range(go_to_floor - current_floor):
                self.go_up()
        # else:
        # print("This floor doesn't exist.")

    def go_down(self):
        print("one floor down!")
        self.current_floor -= 1
        return self.current_floor

    def go_up(self):
        print("one floor up!")
        self.current_floor += 1
        return self.current_floor


elevator_no = int(input("Enter the Number of elevator you want to use."))
floor = int(input("Enter the floor you want to reach."))
# result = Elevator(floor, 0, 0, 5)
# print(f'Current floor is {result.current_floor}')
a_building = Building(25, 0, 100)
a_building.run_elevator(elevator_no, floor)
a_building.fire_alarm()


# Part 4

# import random
# from prettytable import PrettyTable
#
#
# class Race:
#     def __init__(self, name: str, distance: int, cars: list):
#         self.name = name
#         self.distance = distance
#         self.cars = cars
#
#      # def hour_passes(self):
#      #    for i in range(10):
#
# class Car:
#     def __init__(self, reg_num, max_speed, current_speed=0, travelled_distance=0):
#         self.reg_num = reg_num
#         self.max_speed = max_speed
#         self.current_speed = current_speed
#         self.travelled_distance = travelled_distance
#
#     def Acceleration(self, acceleration):
#         self.acceleration = acceleration
#         self.max_speed += self.acceleration
#         # print(f"The speed is {self.max_speed}")
#         if self.max_speed < 0:
#             self.max_speed = 0
#             # print(f"The speed is {self.max_speed}")
#
#     def drive(self, hours):
#         self.hours = hours
#         self.travelled_distance += self.hours * self.max_speed
#         # print(f"The Travelled distance is {self.travelled_distance}")
#
#
#
# cars_list = []
# overall_distance = 0
#
# for i in range(10):
#     car_name = "ABC-" + str(i + 1)
#     car_list = []
#     car_list.append(car_name)
#     max_speed = random.randrange(100, 200)
#     car = Car(car_name, max_speed)
#     changed_speed = random.randint(-10, 15)
#     car.Acceleration(changed_speed)
#     car_list.append(car.max_speed)
#     car.drive(1)
#     distance = car.travelled_distance
#     car_list.append(distance)
#     cars_list.append(car_list)
# # print(cars_list)
# while overall_distance < 10000:
#     for i in range(10):
#         max_speed = random.randrange(100, 200)
#         changed_speed = random.randint(-10, 15)
#         car = Car(car_name, max_speed)
#         car.Acceleration(changed_speed)
#         cars_list[i][1] = car.max_speed
#         car.drive(1)
#         cars_list[i][2] += car.travelled_distance
#         overall_distance = cars_list[i][2]
#         if overall_distance > 10000:
#             break
#
# table = PrettyTable(["Car Name", "Speed", "Travelled Distance"])
# for i in cars_list:
#     car_name = i[0]
#     max_speed = i[1]
#     travelled_distance = i[2]
#     table.add_row([car_name, max_speed, travelled_distance])
# print(table.get_string(sortby="Travelled Distance", reversesort=True))

def find_max_distance(car_list):
    max_distance = 0
    for i in car_list:
        distance = car.travelled_dist
        if distance > max_distance:
            max_distance = distance
    return max_distance


class Car:
    def __init__(self, registration, max_speed, current_speed=0, travelled_dist=0):
        self.registration = registration
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travelled_dist = travelled_dist

    def accelerate(self, speed_change):
        if self.max_speed >= self.current_speed + speed_change >= 0:
            self.current_speed = self.current_speed + speed_change
        elif self.current_speed + speed_change > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed + speed_change < 0:
            self.current_speed = 0
        return

    def drive(self, hours):
        self.travelled_dist = self.travelled_dist + (self.current_speed * hours)


max_dist = 0
cars = []
for car in range(10):
    registration = "ABC-" + str(car + 1)
    max_speed = random.randint(100, 200)
    new_car = Car(registration, max_speed)
    cars.append(new_car)

while max_dist < 10000:
    for car in cars:
        accelerate = random.randint(-10, 15)
        car.accelerate(accelerate)

    for car in cars:
        car.drive(1)

    max_dist = find_max_distance(cars)

table = []
for car in cars:
    table.append([car.registration, car.max_speed, car.current_speed, car.travelled_dist])
print("")
print(tabulate(table, headers=['registration', 'max speed', 'current speed', 'travelled distance'], tablefmt='orgtbl'))


class Race:
    def __init__(self, name, distance, car_list):
        self.name = name
        self.distance = distance
        self.car_list = car_list

    def hour_pass(self):
        for car in self.car_list:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        print(self.name + ";")
        for car in self.car_list:
            print(f"{car.registration:6s}: {car.current_speed:3d}, {car.travelled_dist} km")

    def race_finished(self):
        for car in self.car_list:
            if car.travelled_dist >= self.distance:
                return True
        return False


cars_list = []
for i in range(1, 11):
    new_car = Car(("ABC-" + str(i + 1)), random.randint(100, 200))
    cars_list.append(new_car)
race = Race("derby", 8000, cars_list)
n = 0
while not race.race_finished():
    race.hour_pass()
    n += 1
    if n % 10 == 0:
        print(f"After {n} hours")
        race.print_status()
print(f"The final result after {n} hours is: ")
race.print_status()
