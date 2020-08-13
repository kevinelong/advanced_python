# Data mapping
# multiple sources into one
# even if the sources use different words for various items
# that really mean the same thing
source_one = [
    {"id": 1, "name": "apple", "qty": 6, "price_each": 10.00},
    {"id": 2, "name": "orange", "qty": 12, "price_each": 4.00},
    {"id": 3, "name": "apple", "qty": 24, "price_each": 6.00},
    {"id": 4, "name": "orange", "qty": 48, "price_each": 0.10},
]
# conflicting ID, different field names, and altered product names
source_two = [
    {"id": 1, "product": "APPLES", "quantity": 5, "price": 10.00},
    {"id": 2, "product": "ORANGES", "quantity": 12, "price": 4.00},
    {"id": 3, "product": "APPLES", "quantity": 5, "price": 6.00},
    {"id": 4, "product": "ORANGES", "quantity": 48, "price": 0.10},
]
field_map = {
    "name": "product_name",
    "product": "product_name",
    "qty": "quantity",
    "price_each": "price",
}
value_map = {
    "APPLES": "apple",
    "ORANGES": "orange",
}
output_list = []
for source in [source_one, source_two]:
    for item in source:
        output_item = {}
        for key in item:
            value = item[key]
            field = field_map[key] if key in field_map else key  # TERNARY ? :
            final_value = value_map[value] if value in value_map else value
            output_item[field] = final_value
        output_list.append(output_item)
print(output_list)

totals = {}
for item in output_list:
    p = item["product_name"]
    q = item["quantity"]
    totals[p] = totals[p] + q if p in totals else q
print(totals)


