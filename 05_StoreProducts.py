from products import Product
from stores import Store

store01 = Store("Valaparaiso")
print(store01)
store02 = Store("Concepcion")
print(store02)
print("------------")

product01 = Product("Spagghetti","Pasta",990)
print(product01)
product02 = Product("Almond milk","Daily",3250)
print(product02)
product03 = Product("Watermelon","Fruits",2500)
print(product03)

print("------------")
product03.print_info()
product02.update_price(30, True)
product02.print_info()
product01.update_price(20, False)
product01.print_info()

print("------------")
store01.add_product(product03)
print(store01)
store02.add_product(product01)
store02.add_product(product02)
print(store02)

print("------------")
store02.sell_product(product01)
print(store02)

print("------------")
store01.add_product(product01)
print(store01)
store01.inflation(2)
print(store01)

print("------------")
product04 = Product("yoghurt","Daily",750)
store02.add_product(product04)
store02.set_clearance("Daily",1)
print(store02)
