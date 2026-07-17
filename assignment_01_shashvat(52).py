class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.available = True

class Patron:
    def __init__(self,name):
        self.name = name

class Library:
    def __init__(self):
        self.books = []
        self.patron = []

    def add_book(self,title,author):
        book = Book(title,author)
        self.books.append(book)
        print("Book has been added successfully")

    def register_patron(self,name):
        patron = Patron(name)
        self.patron.append(patron)
        print("patron has been registered successfully")

    def issue_book(self,title,name):
        patron_found = False

        for patron in self.patron:
            if patron.name == name:
                patron_found = True
                break

        if not patron_found:
            print("Book cannot be issued. Patron is not registered.")
            return

        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print("Book has been issued to", name)
                return

        print("Book not available in the library")

    def return_book(self,title):
        for book in self.books:
            if book.title == title:
                book.available = True
                print("Book has been returned to librarry successfully")
                return

    def show_books(self):
        print("\nBook in library")
        for book in self.books:
            if book.available:
                status = "available"
            else:
                status = "issued"
            print("Title:", book.title)
            print("Author:", book.author)
            print("status:", status)

# main program where we will call the functions which we have defined above
print("Welcome to the Library of MIT School Of Computing!!!!")

library = Library()

while True:
    print("\n-------Check the below given options and choose any one of them--------")
    print("1.ADD BOOK")
    print("2.REGISTER PATRON")
    print("3.ISSUE BOOK")
    print("4.RETURN BOOK")
    print("5.SHOW BOOK")
    print("6.EXIT")

    choice = int(input("Enter the option number: "))

    if choice == 1:
        title = input("Enter book: ")
        author = input("Enter author name: ")
        library.add_book(title,author)

    elif choice == 2:
        name = input("Enter patron name: ")
        library.register_patron(name)

    elif choice == 3:
        title = input("Enter book title: ")
        name = input("Enter patron name: ")
        library.issue_book(title,name)

    elif choice == 4:
        title = input("Enter Book title: ")
        library.return_book(title)

    elif choice == 5:
        library.show_books()

    elif choice == 6:
        print("Thank you Have a great day ahed !!")
        break

    else:
        print("please do enter the valid option number")