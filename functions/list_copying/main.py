# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

# Call the function and store the updated prices
def apply_discount(prices):
    prices_copy = prices.copy()
    for i in range(len(prices_copy)):
        if prices[i] > 2:
            prices_copy[i] = prices_copy[i] * 0.9
    return prices_copy






updated_prices = apply_discount(product_prices)
print(f"Updated product prices: {updated_prices}")