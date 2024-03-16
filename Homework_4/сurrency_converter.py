print('Currency converter UAH --> USD and UAH --> EUR\n')

uah_input = float(input("Enter amount: "))

usd_result = uah_input * 0.026
eur_result = uah_input * 0.024
print(f"{uah_input} UAH it's {usd_result:.2f} USD and {eur_result:.2f} EUR")
