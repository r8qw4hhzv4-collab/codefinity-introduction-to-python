# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold



def calculate_revenue(prices, quantities_sold):
    revenue = []
    for i in range(len(prices)):
        rev = prices[i] * quantities_sold[i]
        revenue.append(rev)
    return revenue

revenue = calculate_revenue(prices, quantities_sold)
tuple(revenue)

revenue_per_product = list((zip(products, revenue)))

def formatted_output(revenues_):
    revenues_.sort()
    return revenues_
    

for i in range(len(revenue)):
    print(f"{products[i]} has total revenue of ${revenue[i]}")
print(formatted_output(revenue))
# print(list(revenues__fake))
    
  
# Example of expected output line (do not remove):
# print(f"{revenue[0]} has total revenue of ${revenue[1]}")