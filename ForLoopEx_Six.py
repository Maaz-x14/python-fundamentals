total = 0
items = ["Fruits", "Veggies", "Lentils"]
prices = [10, 20, 30]
for i in range(3):
    print(f"{items[i]}: ${prices[i]}")
for i in prices:
    total += i
print(f"Total = ${total}")