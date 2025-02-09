items = ["Laptop", "Phone", "Tablet"]
prices = [1000, 500, 300]

for i, (item, price) in enumerate(zip(items, prices), start=1):
    print(f"{i}. {item} costs ${price}")
