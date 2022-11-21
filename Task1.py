from random import shuffle

# 1. Створити клас BOOKSHELF (книжкова полиця) з такими 
# властивостями: назва, список назв книжок; методами: конструктор класу, 
# додання книги на полицю, видалення книги з полиці, перемішування книг на 
# полиці. Написати програму, яка імітуватиме книжкову поличку. 


class BOOKSHELF():

    
    def __init__(self, name, books_list):
        self.name = str(name)
        self.book_list = books_list

    
    
    def add_book(self, book_name):
        self.book_list.append(book_name)
    
    
    def delete_book(self, book_name):
        self.book_list.remove(book_name)

    
    def shuffle_books(self):
        shuffle(self.book_list)


shelf = BOOKSHELF("Домашня", ["Воно", "1984", "Острів скарбів", "Білий Клик", "Ми", "Війна та мир"])


print(shelf.name)
print(shelf.book_list)


shelf.add_book("Гаррі Поттер")
shelf.add_book("Місто")
shelf.delete_book("Ми")
print(shelf.book_list)
shelf.shuffle_books()
print(shelf.book_list)
