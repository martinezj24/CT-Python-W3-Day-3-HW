# Task 1: Create Base Product Class

class Product():

    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
    
    def display_info(self):
        print(f"\nProduct ID: {self.product_id}")
        print(f"Book Title: {self.name}")
        print(f"Price: {self.price}")

# Task 2: Implementing Subclasses for Specifc Products


class Book(Product):

    def __init__(self, product_id, name, price, author):
       super().__init__(product_id, name, price)
       self.author = author

# Task 3: Override Display Method in Subclasses

    def display_info(self):
       super().display_info()
       print(f"Author: {self.author}")



# Task 4: Test Product Catalog Functionality

my_book = Book("123", "More Than A Carpenter", 6.99, 'Josh McDowell')
my_book.display_info()

my_book2 = Book('456', "The Case For Christ", 19.99, 'Lee Strobel')
my_book2.display_info()