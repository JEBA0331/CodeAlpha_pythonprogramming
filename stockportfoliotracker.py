stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 135
}

total_value = 0

print("📊 Stock Portfolio Tracker")

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()
    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        total_value += stock_prices[stock] * quantity
    else:
        print("Stock not available.")

print("💰 Total Investment Value: ₹", total_value)

# Save result to file (UTF-8 FIX)
with open("portfolio.txt", "w", encoding="utf-8") as file:
    file.write(f"Total Investment Value: ₹{total_value}")

print("✅ Saved result in portfolio.txt")
