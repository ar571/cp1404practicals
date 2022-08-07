items = int(input("Number of items: "))
total_price = 0

while items < 0:
    print("Invalid number of items")
    items = int(input("Number of items: "))

for i in range(items):
    price = float(input("Price of item: "))
    total_price += price

print(f"Total price for {items} items is ${total_price:.2f}")