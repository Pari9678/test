class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed==False:
            self.is_borrowed=True
            print (self.title, "is borrowed")
        else:
            print (self.title, "is not avaliable")

    def return_book(self):
        if self.is_borrowed==True:
            self.is_borrowed=False
            print (self.title, "is returned")
        else:
            print (self.title, "was not borrowed")

book_1 = Book("Shatter Me", "Tahereh Mafi")
book_2 = Book("Legend", "Marie Lu")
book_3 = Book("Once upon a broken heart", "Stephanie Garber")


book_1.borrow()
book_1.return_book()
book_2.borrow()
book_2.return_book()
book_3.borrow()
book_3.return_book()