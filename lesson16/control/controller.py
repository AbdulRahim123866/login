from random import randint, choice

from constans import BookStatus
from main import Book, Employee, Order

inventory=[
    Book(**{
        "BID":i,
        "title": f"Book {i}"
        ,"author":f"Author {i}",
        "price":randint(2,25)
        ,"quantity":10,
        "status":choice([BookStatus.USED,BookStatus.NEW])


    }
    )for i in range(100)



]
print(inventory)


class Library:
    def __init__(self):
        self.inventory=inventory
        self.employee=Employee

    def List_books(self):
        return self.inventory.copy()

    def place_order(self,client ,quantity, books:list[str]):
        not_available=[book.title for book in self.inventory if book.status != BookStatus.AVAILABE or book.quantity <=0]


        for name in books:
            if name not in not_available:
                print(f"Book with name {name} is not available")


        for book in self.inventory:
            if book.title in books:
                book.quantity -=quantity
                book.status=BookStatus.RESERVED



        total_price = sum([book.price for book in self.inventory if book.title in books ])
        return  Order(client,book,quantity ,total_price)
