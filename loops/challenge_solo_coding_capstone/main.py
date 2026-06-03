# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}
# 0: stock 1: price 2: discount price
for item in inventory:
    name = inventory[item]
    discounted_price = name[2]
    regular_price = name[1]
    if name[0] < 30:
        print(f"{item} need restocking.")
    if name[0] > 100:
        print(f"{item} should be sold at the discounted price of {discounted_price}.")
    if (30 <= name[0] <= 100):
        print(f"{item} should be sold at the regular price of {regular_price}.")
        





















