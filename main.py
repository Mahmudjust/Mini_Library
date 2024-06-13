from books import Book
from users import User

def main():
    user = User("example_user")

    while True:
        print("\n1. Add Book\n2. Mark as Read\n3. Mark as Unread\n4. Add Review\n5. Display Reviews\n6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            book = Book(title, author)
            user.add_book(book)
            print(f"Book '{title}' added.")
        
        elif choice == '2':
            title = input("Enter book title to mark as read: ")
            user.mark_book_as_read(title)
            print(f"Book '{title}' marked as read.")
        
        elif choice == '3':
            title = input("Enter book title to mark as unread: ")
            user.mark_book_as_unread(title)
            print(f"Book '{title}' marked as unread.")
        
        elif choice == '4':
            title = input("Enter book title to review: ")
            review = input("Enter your review: ")
            rating = int(input("Enter your rating (1-5): "))
            user.leave_review(title, review, rating)
            print(f"Review for '{title}' added.")
        
        elif choice == '5':
            title = input("Enter book title to display reviews: ")
            for book in user.reading_list:
                if book.title == title:
                    print(f"\nReviews for {book.title}:")
                    for review in book.reviews:
                        print(review)
                    print(f"Ratings: {book.ratings}")

        elif choice == '6':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
