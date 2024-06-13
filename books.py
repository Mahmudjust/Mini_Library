class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_read = False
        self.reviews = []
        self.ratings = []

    def mark_as_read(self):
        self.is_read = True

    def mark_as_unread(self):
        self.is_read = False

    def add_review(self, review, rating):
        self.reviews.append(review)
        self.ratings.append(rating)
