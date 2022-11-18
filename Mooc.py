from datetime import date
from os import times


# Mooc Part 8-1
def smallest_average(first: dict, second: dict, third: dict):
    first_average = (first["result1"] + first["result2"] + first["result3"]) / 3
    second_average = (second["result1"] + second["result2"] + second["result3"]) / 3
    third_average = (third["result1"] + third["result2"] + third["result3"]) / 3
    if first_average < second_average and first_average < third_average:
        return first
    elif second_average < third_average and second_average < first_average:
        return second
    else:
        return third


person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}
print(smallest_average(person1, person2, person3))


# Mooc part 8-2


def row_sums(matrix: list):
    list1 = matrix[0]
    result1 = 0
    for item in list1:
        result1 += item
    list1.append(result1)
    matrix[0] = list1

    list2 = matrix[1]
    result2 = 0
    for item in list2:
        result2 += item
    list2.append(result2)
    matrix[1] = list2
    return matrix


my_matrix = [[1, 2], [3, 4]]
row_sums(my_matrix)
print(my_matrix)


# Mooc Part 8-3


def list_years(dates: list):
    years = []
    for date in dates:
        year = date.year
        years.append(year)
    years.sort()
    return years


date1 = date(2019, 2, 3)
date2 = date(2006, 10, 10)
date3 = date(1993, 5, 9)

years = list_years([date1, date2, date3])
print(years)


# Mooc Part 8-4


# for i in range(1, shopping_list.number_of_items()+1):
#     item = shopping_list.item(i)
#     amount = shopping_list.amount(i)
#     print(f"{item}: {amount} units")
#
# if __name__ == "__main__":
#     my_list = ShoppingList()
#     my_list.add_item("bananas", 10)
#     my_list.add_item("apples", 5)
#     my_list.add_item("pineapple", 1)
#
#     print(total_units(my_list))


# Mooc 8-5


class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year


python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)

print(f"{python.author}: {python.name} ({python.year})")
print(f"The genre of the book {everest.name} is {everest.genre}")


# Mooc 8-6

class CheckList:
    def __init__(self, header: str, entries: list):
        self.header = header
        self.entries = entries


class Customer:
    def __init__(self, id: str, balance: float, discount: int):
        self.id = id
        self.balance = balance
        self.discount = discount


class Cable:
    def __init__(self, model: str, length: float, max_speed: int, bidirectional: bool):
        self.model = model
        self.length = length
        self.max_speed = max_speed
        self.bidirectional = bidirectional


# Mooc 8-7

class Pet:
    def __init__(self, name: str, species: str, year_of_birth: int):
        self.name = name
        self.species = species
        self.year_of_birth = year_of_birth


def new_pet(name, species, year):
    return Pet(name, species, year)


fluffy = new_pet("Fluffy", "dog", 2017)
print(fluffy.name)
print(fluffy.species)
print(fluffy.year_of_birth)


# Mooc 8-9

# python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
# everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
# norma = Book("Norma", "Sofi Oksanen", "crime", 2015)
#
# older_book(python, everest)
# older_book(python, norma)


# Mooc 8-10


# python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
# everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
# norma = Book("Norma", "Sofi Oksanen", "crime", 2015)
#
# books = [python, everest, norma, Book("The Snowman", "Jo Nesbø", "crime", 2007)]
#
# print("Books in the crime genre:")
# for book in books_of_genre(books, "crime"):
#     print(f"{book.author}: {book.name}")


# Mooc 8-11 (not completed)

class DecreasingCounter:
    def __init__(self, initial_value: int):
        first_value = initial_value
        self.value = first_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        if self.value >= 1:
            self.value -= 1
            return self.value

        else:
            self.value = 0
            return self.value

    def set_to_zero(self):
        self.value = 0
        return self.value

    def reset_original_value(self):
        self.value = counter.first_value
        return self.value


counter = DecreasingCounter(100)
counter.print_value()
counter.decrease()
counter.print_value()
counter.decrease()
counter.print_value()
counter.set_to_zero()
counter.print_value()


# counter.reset_original_value()


# Mooc 8-12(incomplete)

class Person:
    def __init__(self, names: str):
        self.names = names

    def return_first_name(self):
        items = self.names
        first_name = ""
        for item in items:
            if item == " ":
                break
            else:
                first_name += item
        return first_name

    def return_last_name(self):
        items = self.names
        last_name = items[1]


if __name__ == "__main__":
    peter = Person("Peter Pythons")
    print(peter.return_first_name())
    # print(peter.return_last_name())

    paula = Person("Paula Pythonnen")
    print(paula.return_first_name())
    # print(paula.return_last_name())


# Mooc 8-13(Incomplete)

# class NumberStats:
#     def __init__(self):
#         # self.numbers = 0
#         pass
#     def add_number(self, number: int):
#         self.numbers = number
#         print(self.numbers)
#         self.count_numbers()
#         self.get_sum(self.numbers)
#     def count_numbers(self, count):
#         self.count += count
#         self.count += 1
#         return self.count
#
#
#     def get_sum(self, numbers):
#         list = []
#         list.append(numbers)
#         print(list)
#         sum_amount = 0
#         for i in range(int(len(list))):
#             sum_amount += int(i)
#
#             return sum_amount
#
#
# stats = NumberStats()
# stats.add_number(3)
# stats.add_number(5)
# stats.add_number(1)
# stats.add_number(2)
# print("Numbers added:", stats.count_numbers())
# print("Sum of numbers:", stats.get_sum)
# print("Mean of numbers:", stats.average())


# Mooc 8-14


class Stopwatch:
    def __init__(self):
        self.seconds = 00
        self.minutes = 00
        self.tick()

    def tick(self):
        if self.seconds == 59:
            self.minutes += 1
            self.seconds = 00
        else:
            self.seconds += 1

        return self.seconds, self.minutes

    def __str__(self):
        self.watch = [self.minutes, self.seconds]
        return f"{self.watch[0]}:{self.watch[1]}"


class Clock:

    def __str__(self):
        return f"{self.hour}:{self.minute}:{self.second}"

    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def tick(self):
        if self.minute == 59 and self.second == 59:
            self.hour += 1
            self.second = 00
            self.minute = 00
        elif self.second == 59:
            self.minute += 1
            self.second = 00
        else:
            self.second += 1

    def set(self, new_hour, new_minute):
        self.hour = new_hour
        self.minute = new_minute
        self.second = 00
        return self.hour, self.minute, self.second


watch = Stopwatch()
for i in range(3600):
    print(watch)
    watch.tick()

clock = Clock(23, 59, 55)
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.set(12, 5)
print(clock)


# Mooc 8-15

class LunchCard:
    def __init__(self, balance: float):
        self.balance = "{:.1f}".format(balance)

    def __str__(self):
        return f"The balance is {self.balance} euros."

    def eat_lunch(self):
        self.balance = "{:.1f}".format(float(self.balance) - 2.60)
        return self.balance

    def eat_special(self):
        self.balance = "{:.1f}".format(float(self.balance) - 4.60)
        return self.balance

    def deposit_money(self, deposit: float):
        self.deposit = deposit
        self.balance = "{:.1f}".format(float(self.balance) + self.deposit)


card = LunchCard(50)
print(card)

card.eat_lunch()
print(card)

card.eat_special()
card.eat_lunch()
print(card)

card = LunchCard(10)
print(card)
card.deposit_money(15)
print(card)
card.deposit_money(10)
print(card)
card.deposit_money(200)
print(card)
card = LunchCard(10)
card.deposit_money(-10)
print(card)


# Mooc 8-16


# Mooc 9-1


class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed


def fastest_car(cars_list):
    top_speed = 0
    for x in cars_list:
        if x.speed > top_speed:
            top_speed = x.speed
            name = x.name
    return name


if __name__ == "__main__":
    car1 = Car("Saab", 195)
    car2 = Car("Lada", 110)
    car3 = Car("Ferrari", 280)
    car4 = Car("Trabant", 85)

    cars = [car1, car2, car3, car4]
    print(fastest_car(cars))


# Mooc 9-2

class ExamSubmission:
    def __init__(self, examinee: str, points: int):
        self.examinee = examinee
        self.points = points


def passed(examinee_list: list, min_point: int):
    passing = []
    for i in examinee_list:
        if i.points >= min_point:
            passed_list = []
            passed_list.append(i.examinee)
            passed_list.append(i.points)
            passing.append(passed_list)
    return passing





if __name__ == "__main__":
    s1 = ExamSubmission("Peter", 12)
    s2 = ExamSubmission("Pippa", 19)
    s3 = ExamSubmission("Paul", 15)
    s4 = ExamSubmission("Phoebe", 9)
    s5 = ExamSubmission("Persephone", 17)
    exam_list = [s1, s2, s3, s4, s5]
    # print(s1.points)
    passes = passed(exam_list, 15)
    for passing in passes:
        print(f"ExamSubmission(examinee: {passing[0]}, points: {passing[1]})")


# Mooc 9-3

class Person:
    def __init__(self, name: str, age: int, height: int, weigh: int):
        self.name = name
        self.age = age
        self.height = height
        self.weigh = weigh




class BabyCentre:
    times = 0
    def weigh(self, person: Person):
        # return the weight of the person passed as an argument
        self.weigh_ins()
        self.times += 1
        return person.weigh

    def feed(self, person: Person):
        person.weigh += 1
        return person.weigh

    def weigh_ins(self):
        return self.times


baby_centre = BabyCentre()
#
eric = Person("Eric", 1, 110, 7)
# peter = Person("Peter", 33, 176, 85)
#
# print(f"{eric.name} weighs {baby_centre.weigh(eric)} kg")
# print(f"{peter.name} weighs {baby_centre.weigh(peter)} kg")
#
# # Part2
#
# baby_centre.feed(eric)
# baby_centre.feed(eric)
# baby_centre.feed(eric)
#
# print(f"{eric.name} weighs {baby_centre.weigh(eric)} kg")
# print(f"{peter.name} weighs {baby_centre.weigh(peter)} kg")

# Part 3

print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

baby_centre.weigh(eric)
baby_centre.weigh(eric)

print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

baby_centre.weigh(eric)
baby_centre.weigh(eric)
baby_centre.weigh(eric)
baby_centre.weigh(eric)

print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

# Mooc 9-4






# Mooc 9-5


class RealProperty:
    def __init__(self, rooms: int, square_metres: int, price_per_sqm: int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm



    def bigger(self, another_property: "RealProperty"):
        if self.square_metres > another_property.square_metres:
            return True
        else:
            return False

    def price_difference(self, another_price: "RealProperty"):
        total_price = (another_price.price_per_sqm/another_price.square_metres) - (self.price_per_sqm/self.square_metres)
        # print(total_price)
        difference = total_price * self.square_metres
        return difference




central_studio = RealProperty(1, 16, 5500)
downtown_two_bedroom = RealProperty(2, 38, 4200)
suburbs_three_bedroom = RealProperty(3, 78, 2500)

print(central_studio.bigger(downtown_two_bedroom))
print(suburbs_three_bedroom.bigger(downtown_two_bedroom))


print(central_studio.price_difference(downtown_two_bedroom))
# print(suburbs_three_bedroom.price_difference(downtown_two_bedroom))


# Mooc 9-6




# Mooc 9-7

class Present:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name}({self.weight}kg)"


class Box:
    weight = 0
    def add_present(self, present):
        self.present = present


    def total_weight(self):
        self.weight += self.present.weight
        return self.weight


    def __str__(self):
        return f"{self.weight}"


book = Present("ABC Book", 2)

print("The name of the present:", book.name)
print("The weight of the present:", book.weight)
print("Present:", book)

box = Box()
box.add_present(book)
print(box.total_weight())

cd = Present("Pink Floyd: Dark Side of the Moon", 1)
box.add_present(cd)
print(box.total_weight())


# Mooc 9-8

class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height


class Room:
    def __init__(self):
        self.people = []
    def add(self, person):
        self.people.append(person)
        return self.people

    def is_empty(self):
        if len(self.people) == 0:
            return True
        else:
            return False

    def print_contents(self):
        for i in self.people:
            print(f"{i.name}({i.height})")

    def shortest(self):
        if len(self.people) == 0:
            return None
        else:
            shortest = self.people[0].height
            for i in self.people:
                if i.height < shortest:
                    shortest = i.height
                    self.shortest_person = i

            return self.shortest_person


    def remove_shortest(self):
        self.people.remove(self.shortest_person)
        return self.shortest_person

room = Room()
print("Is the room empty?", room.is_empty())
room.add(Person("Lea", 183))
room.add(Person("Kenya", 172))
room.add(Person("Ally", 166))
room.add(Person("Nina", 162))
room.add(Person("Dorothy", 155))
print("Is the room empty?", room.is_empty())
room.print_contents()

room.add(Person("Lea", 183))
room.add(Person("Kenya", 172))
room.add(Person("Nina", 162))
room.add(Person("Ally", 166))

print()

print("Is the room empty?", room.is_empty())
print("Shortest:", room.shortest())

print()

room.print_contents()

removed = room.remove_shortest()
print(f"Removed from room: {removed.name}")

print()

room.print_contents()


# Mooc 9-9

class Car:
    def __init__(self):
        self.__tank_amount = 0
        self.__odometer = 0


    def fill_up(self):
        self.__tank_amount = 60
        return self.__tank_amount

    def drive(self, dis):
        if self.__tank_amount > dis:
            self.__odometer += dis
            self.__tank_amount -= self.__odometer
        else:
            self.__odometer += self.__tank_amount
            self.__tank_amount = 0
        return self.__tank_amount, self.__odometer

    def __str__(self):
        return f"odometer reading {self.__odometer} km, petrol remaining {self.__tank_amount} litres"



car = Car()
print(car)
car.fill_up()
print(car)
car.drive(20)
print(car)
car.drive(50)
print(car)
car.drive(10)
print(car)
car.fill_up()
car.fill_up()
print(car)


# Mooc 9-10





# Mooc 9-11

class WeatherStation:
    def __init__(self, name):
        self.name = name
        self.observations = []

    def add_observation(self, observation):
        self.observations.append(observation)

    def latest_observation(self):
        last_index = int(len(self.observations)) - 1
        self.last_item = self.observations[last_index]
        # print(self.last_item)
        return self.last_item


    def number_of_observations(self):
        self.overall_num = len(self.observations)
        return self.overall_num

    def __str__(self):
        return f"{self.name}, {self.overall_num} observations"




station = WeatherStation("Houston")
station.add_observation("Rain 10mm")
station.add_observation("Sunny")
print(station.latest_observation())

station.add_observation("Thunderstorm")
print(station.latest_observation())

print(station.number_of_observations())
print(station)


# Mooc 9-12

class BankAccount:
    def __init__(self, name: str, account_no: str, balance: float):
        self.name = name
        self.account_no = account_no
        self.balance = balance

    def deposit(self, money: float):
        self.money = money
        self.balance += self.money
        self.__service_charged()
        return self.balance


    def withdraw(self, money: float):
        self.money = money
        if self.balance > self.money:
            self.__service_charged()
            self.balance -= self.money
        else:
            print("Tou don't have enough budget")

    def balance(self):
        return self.balance

    def __service_charged(self):
        service = self.balance * 0.01
        self.balance -= service
        return self.balance











account = BankAccount("Randy Riches", "12345-6789", 1000)
account.withdraw(100)
print(account.balance)
account.deposit(100)
print(account.balance)

