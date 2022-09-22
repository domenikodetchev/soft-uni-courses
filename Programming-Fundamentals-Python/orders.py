num_of_orders = int(input())
coffee = 0
for i in range(1, num_of_orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    if days < 1 or days > 31:
        continue
    if capsules < 1 or capsules > 2000:
        continue
    price = (price_per_capsule*capsules)*days
    print(f"The price for the coffee is: {price:.2f}")
    coffee += price
print(f"Total: {coffee:.2f}")