PriceHouse = 1000000
GoodCredit = int(input("Is credit of buyer good? Press 1 for True: "))
if GoodCredit == 1:
    down_payment = PriceHouse * 0.1
else:
    down_payment = PriceHouse * 0.2
print(f"Down payment would be: ${int(down_payment)}")
