#Создать класс магазин-----------------------------------
class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item, price):
        self.items[item] = price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def get_item_price(self, item):
        return self.items.get(item, None)

    def update_item_price(self, item, new_price):
        if item in self.items:
            self.items[item] = new_price


#Создать объект магазин--------------------------------------------------
shop1 = Store('Магазин фруктов', 'Тополиная 12')
shop2 = Store('Магазин игрушек', 'Тополиная 14')
shop3 = Store('Магазин одежды', 'Тополиная 20')

shop1.add_item('яблоки', 0.5)
shop1.add_item('бананы', 0.75)
shop1.remove_item('яблоки')
shop1.update_item_price('бананы', 1.0)
print(shop1.items)  # {'bananas': 1.0}
print(shop1.get_item_price('бананы'))  # 1.0
print(shop1.get_item_price('яблоки'))  # None