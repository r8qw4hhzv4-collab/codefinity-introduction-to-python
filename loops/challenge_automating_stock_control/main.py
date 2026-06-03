# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print("Processing started")

for item in inventory:
    name = inventory[item]
    current_stock = name[0]
    min_req_stock = name[1]
    restock_quantity = name[2]
    sale_status = name[3]
    
    while current_stock < min_req_stock:
        current_stock = current_stock + restock_quantity
        if current_stock >= min_req_stock:
            inventory[item][0] = current_stock
        
    
    if current_stock > discount_threshold:
        inventory[item][3] = True
        
    print(f"Processing {item}")




print("Processing completed")














