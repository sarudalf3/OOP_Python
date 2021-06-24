class Product:

    ID_idx = 1

    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price
        self.ID = Product.ID_idx
        Product.ID_idx += 1

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price *= (1+(percent_change/100))
        else:
            self.price *= (1-(percent_change/100))
        print(f"Product: {self.name}, update the price in {self.price}")
        return self

    def print_info(self) : 
        print(f"product {self.name} belongs to category {self.category}, has a price {self.price} and get the ID {self.ID}")

    def __str__(self):
        return f"Product: {self.name} \nID:{self.ID} \nCategory: {self.category}\nPrice: {self.price}"
