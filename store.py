#
# NOUNS - People
# VERBS - Methods
# AJECTIVES - Attributes
#
# Inventory
# InventoryItem Part_number, SerialNumber
#
# Catalog - AddItem()
# CatalogItem (part_number, price,name,desc,image_path, quantityonhand)
#
# Cart - Collection - AddItem()
# CartItem(catalog_item, quantity, tax)
#
# OptionSet e.g. size, or color
# Option(name, price_adjustment=0)

# STORY - NARATIVE
# USE CASE

# Create catalog item
# As a:       store manager
# I want to:  add catalog items
# So as to:   make them available for sale.

# Add item to inventory
# As a:       As a warehouse manage
# I want to:  Take an item into inventory
# So as to:   Track increasing inventory levels.

# Add item to cart.
# As a:       As a store customer
# I want to:  create a set of items
# So as to:   so i can pay once for many things to save time.


class InventoryItem:
    pass


class Choice:
    def __init__(self, name, additional_price=0.0):
        self.name = name
        self.additional_price = additional_price

    def __str__(self):
        return f"{self.name} +${self.additional_price}"


class ChoiceSet:
    def __init__(self, name, choice_list):
        self.name = name
        self.choice_list: [Choice] = choice_list


class CatalogItem:
    def __init__(self, name: str, price, choice_sets: [ChoiceSet] = None):
        self.name: str = name
        self.price = price
        self.choice_sets = choice_sets if choice_sets is not None else []


class Category:
    # CONSTRUCTOR CALLED AUTOMTICLLY WHEN CREATE AN INSTANCE e.g Category("drinks")
    def __init__(self, name: str, category_items: [CatalogItem] = None):
        self.name: str = name
        self.category_items = category_items if category_items is not None else []

    def add_item(self, menu_item):
        self.category_items.append(menu_item)


class Catalog:
    def __init__(self):
        self.category_list = []

    def add_category(self, category: Category):
        self.category_list.append(category)


class Customer:
    def __init__(self, name, phone, address):
        self.name: str = name
        self.phone: str = phone
        self.address: str = address
        self.licence_plate: str = ""
        self.car_make: str = ""
        self.car_model: str = ""


class CartItem:
    def __init__(self, item: CatalogItem, quantity=1, choices: [Choice] = None):
        self.item = item
        self.quantity = quantity
        self.choices: [Choice] = [] if choices is None else choices

    def subtotal(self):
        return self.quantity * self.item.price

    def __str__(self):
        return f"{self.quantity} {self.item.name} @{self.item.price}={self.subtotal()}"


class Order:
    def __init__(self):
        self.customer: Customer = Customer("", "", "")
        self.item_list: [CartItem] = []

    def total(self):
        grand_total = 0
        for item in self.item_list:
            grand_total += item.subtotal()
            for c in item.choices:
                grand_total += c.additional_price
        return grand_total


# TESTS
if __name__ == "__main__":

    shirts = Category("Shirts")

    shirts.add_item(CatalogItem("T-Shirt", 3.33))
    shirts.add_item(CatalogItem("Button Down", 2.22))

    shoes = Category("Shoes")

    shoes.add_item(CatalogItem("Tennis", 33.33))
    shoes.add_item(CatalogItem("Boot", 222.22))

    shoes.add_item(CatalogItem("Custom Shirt", 44.44, [
        ChoiceSet("size", [
            Choice("Small"),
            Choice("Medium"),
            Choice("Large", 5.00),
        ]),
        ChoiceSet("color", [
            Choice("Red"),
            Choice("Green"),
            Choice("Gold", 7.00),
        ])
    ]))

    catalog = Catalog()
    catalog.add_category(shoes)

    order = Order()
    selection = catalog.category_list[0].category_items[0]
    order.item_list.append(CartItem(selection, quantity=2))

    custom_selection = catalog.category_list[0].category_items[2]
    order.item_list.append(CartItem(custom_selection, quantity=1, choices=[
        custom_selection.choice_sets[0].choice_list[2],
        custom_selection.choice_sets[1].choice_list[2]
    ]))

    for item in order.item_list:
        print(item)
        for choice in item.choices:
            print(f"\t{choice}")
    print(f"TOTAL: {order.total():.2f}")
