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
