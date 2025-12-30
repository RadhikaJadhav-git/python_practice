amount = float(input("Enter amount in INR: "))

usd = amount * 0.012
eur = amount * 0.011

print("USD:", round(usd, 2))
print("EUR:", round(eur, 2))
