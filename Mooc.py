from datetime import date


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


