from string import Template

total = 0

basket = [
    {"item": "Rock", "price": 11, "qty": 1},
    {"item": "Paper", "price": 22, "qty": 2},
    {"item": "Scissors", "price": 33, "qty": 3},
]

template = Template("$qty x $item = $price")

for item in basket:
    print(template.substitute(item))
    total += item["price"]

print(f"Total is: {total}")
