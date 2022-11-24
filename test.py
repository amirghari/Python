class Employee:

    total_employees = 0

    def __init__(self, first_name, last_name):
        Employee.total_employees = Employee.total_employees + 1
        self.employee_number = Employee.total_employees
        self.first_name = first_name
        self.last_name = last_name

    def print_information(self):
        print(f"{self.employee_number}: {self.first_name} {self.last_name}")

class HourlyPaid(Employee):

    def __init__(self, first_name, last_name, hourly_pay):
        self.hourly_pay = hourly_pay
        super().__init__(first_name, last_name)

    def print_information(self):
        super().print_information()
        print(f"Hourly pay: {self.hourly_pay}")

class MonthlyPaid(Employee):

    def __init__(self, first_name, last_name, monthly_pay):
        self.monthly_pay = monthly_pay
        super().__init__(first_name, last_name)

    def print_information(self):
        super().print_information()
        print(f"Monthly pay: {self.monthly_pay}")


employees = []
employees.append(HourlyPaid("Viivi", "Virta", 12.35))
employees.append(MonthlyPaid("Ahmed", "Habib", 2750))
employees.append(Employee("Pekka", "Puro"))
employees.append(HourlyPaid("Olga", "Glebova", 14.92))

for e in employees:
    e.print_information()


print()

#

class Book:
   """ This class models a simple book """
   def __init__(self, name: str, author: str):
       self.name = name
       self.author = author


class BookContainer:
   """ This class models a container for books """

   def __init__(self):
       self.books = []

   def add_book(self, book: Book):
       self.books.append(book)

   def list_books(self):
       for book in self.books:
           print(f"{book.name} ({book.author})")


class Bookshelf(BookContainer):
   """ This class models a shelf for books """

   def __init__(self):
       super().__init__()

   def add_book(self, book: Book, location: int):
       self.books.insert(location, book)


if __name__ == "__main__":
   # Create some books for testing
   b1 = Book("Old Man and the Sea", "Ernest Hemingway")
   b2 = Book("Silent Spring", "Rachel Carson")
   b3 = Book("Pride and Prejudice", "Jane Austen")

   # Create a BookContainer and add the books
   container = BookContainer()
   container.add_book(b1)
   container.add_book(b2)
   container.add_book(b3)

   # Create a Bookshelf and add the books (always to the beginning)
   shelf = Bookshelf()
   shelf.add_book(b1, 0)
   shelf.add_book(b2, 0)
   shelf.add_book(b3, 0)


   # Tulostetaan
   print("Container:")
   container.list_books()

   print()

   print("Shelf:")
   shelf.list_books()

#
print()

class Product:
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    def __str__(self):
        return f"{self.__name} (price {self.__price})"

    @property
    def price(self):
        return self.__price

    def greater(self, another_product):
        return self.price > another_product.price


orange = Product("Orange", 2.90)
apple = Product("Apple", 3.95)

# if orange > apple:
#     print("Orange is greater")
# else:
#     print("Apple is greater")
print(apple)
