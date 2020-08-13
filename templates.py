
from string import Template


basket = [
    {
        "item": "Rock",
        "price": 11,
        "qty": 1
    },
    {"item": "Paper", "price": 22, "qty": 2},
    {"item": "Scissors", "price": 33, "qty": 3},
]

template = Template("$qty, $item, $price")
total = 0

for item in basket:
    text = template.substitute(item)
    print(text)

    # total = total + (item["price"] * item["qty"])
    price = item["price"]
    quantity = item["qty"]
    extended_price = price * quantity
    total = total + extended_price

print(f"Total is: {total}")
