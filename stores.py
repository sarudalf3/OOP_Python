class Store:
    def __init__(self, name): #, market):
        self.name = name
        self.productsList = []

    def add_product(self, new_product):
        self.productsList.append(new_product)

    def sell_product(self, product):
        for prod in self.productsList:
            if prod.ID == product.ID:
                self.productsList.remove(prod)

    def inflation(self, percent):
        for products in self.productsList:
            products.update_price(percent, True)

    def set_clearance (self, category, percent_discount):
        for product in self.productsList:
            if product.category == category:
                product.update_price(percent_discount, False)

    def __str__(self):
        out = f"Store: {self.name}"
        for prod in self.productsList:
            out += f"\n{prod.name} "
        return out        