import time
from operator import index


class Book:
    def __init__(self,id,title,author,genre):
        self.id=id
        self.title=title
        self.author=author
        self.genre=genre
        self.is_available=True

    def display(self):
        print(f"author by {self.author} this is {self.genre} book")
        print(f"the title is {self.title}")

    # def is_availble(self):
    #     if self.is_available:
    #         return True
    #     else:
    #         return False

    def loan(self,member):
        if not self.is_available:
            print("this book is out of the stock")
            return
        print(f"{member.name} has took the book {self.title}")
        self.is_available=False
        return True

    def return_book(self,member):
        print(f"{member.name} has return the book {self.title}")
        self.is_available=True

class Member:
    def __init__(self,name,id,age,loyal):
        self.name=name
        self.id=id
        self.age=age
        self.loyal=loyal
        self.contain_book=[]
    def borrow(self,book):
        if book.title not in self.contain_book:
            if book.loan(member=self):
                self.contain_book.append(book.title)
                return
        print("I already have the book")

    def return_book(self,book):
        try:
            index = self.contain_book.index(book.title)
        except:
            print("i cant return something i dont have")
            return

        self.contain_book.remove(self.contain_book[index])
        book.is_available=True












book1=Book(id=1,title="Abook",author="Ahmad",genre="Action")
# book.loan(2)

book2=Book(id=2,title="Abook2",author="Abd",genre="romantic")


member=Member(name='khaled',id=1,age=40,loyal=True)
if book1.is_available:
    member.borrow(book1)
    time.sleep(1)

member.borrow(book1)
print(book1.is_available)
print(member.contain_book)
member.return_book(book1)
print(book1.is_available)
print(member.contain_book)