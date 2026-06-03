# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []

# item is the repeading fruit str
# name are the list values associated with each fruit str
for item in products:
    vals = products[item]
    vals[0] = float(vals[0])
    vals[1] = int(vals[1])
    total_sales = (vals[0] * vals[1])
    total_sales_list.append(total_sales)
    
    
    print(f"Total sales for {item}: ${total_sales}")
total_sum = sum(total_sales_list)
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)

print(f"Total sum of all sales: $ {total_sum}")
print(f"Minimum sales: ${min_sales}")
print(f"Maximum sales: ${max_sales}")







