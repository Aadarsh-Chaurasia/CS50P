amount = 50
while amount > 0 and amount <= 50:
    print(f"Amount Due: {amount}")
    paid = int(input("Insert Coin: "))
    if (paid == 5 or paid == 10 or paid == 25):
        amount -= paid
print(f"Change Owed: {-1 * amount}")
