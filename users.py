class User:
    def __init__(self, username):
        self.username = username
        self.reading_list = []

    def add_book(self, book):
        self.reading_list.append(book)

    def mark_book_as_read(self, book_title):
        for book in self.reading_list:
            if book.title == book_title:
                book.mark_as_read()

    def mark_book_as_unread(self, book_title):
        for book in self.reading_list:
            if book.title == book_title:
                book.mark_as_unread()

    def leave_review(self, book_title, review, rating):
        for book in self.reading_list:
            if book.title == book_title:
                book.add_review(review, rating)
