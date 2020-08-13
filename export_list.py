catalog = [
    ["P1", 100],
    ["P2", 324],
    ["P3", 2],
]

order = [
    ["P1", 12],
    ["P3", 100],
]

catalog_dict = {}
for c in catalog:
    catalog_dict[c[0]] = c

def get_total_amount_for_order(catalog, order):
    total = 0
    for item in order:
        part_number = item[0]
        catalog_item = catalog_dict[part_number]
        price = catalog_item[1]
        quantity = item[1]
        total += price * quantity
    return total

result = get_total_amount_for_order(catalog, order)
print(result)
