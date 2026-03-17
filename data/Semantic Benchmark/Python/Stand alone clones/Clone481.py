def pay_with_coins(amount) :
	coins = [0 for i in range(len(currencies))]
	amount = int(amount * 100)
	values = [c * 100 for c in currencies]
	for currency in values :
		i = values.index(currency)
		coins [i] = 0
		while amount > = currency :
			amount -= currency
			coins [i] += 1
	return coins


def pay_with_coins(amount) :
	amount = Decimal(amount)
	coins_list = [0, 0, 0, 0, 0, 0, 0, 0]
	if amount == 0 :
		return (coins_list)
	else :
		while amount > Decimal("2.00") :
			coins_list [0] = (coins_list [0] + 1)
			amount = amount - Decimal("2.00")
		while amount > = Decimal("1.00") and amount < Decimal("2.00") :
			coins_list [1] = (coins_list [1] + 1)
			amount = amount - Decimal("1.00")
		while amount > = Decimal("0.50") and amount < Decimal("1.00") :
			coins_list [2] = (coins_list [2] + 1)
			amount = amount - Decimal("0.50")
		while amount > = Decimal("0.20") and amount < Decimal("0.50") :
			coins_list [3] = (coins_list [3] + 1)
			amount = amount - Decimal("0.20")
		while amount > = Decimal("0.10") and amount < Decimal("0.20") :
			coins_list [4] = (coins_list [4] + 1)
			amount = amount - Decimal("0.10")
		while amount > = Decimal("0.05") and amount < Decimal("0.10") :
			coins_list [5] = (coins_list [5] + 1)
			amount = amount - Decimal("0.05")
		while amount > = Decimal("0.02") and amount < Decimal("0.05") :
			coins_list [6] = (coins_list [6] + 1)
			amount = amount - Decimal("0.02")
		while amount > = Decimal("0.01") and amount < Decimal("0.05") :
			coins_list [7] = (coins_list [7] + 1)
			amount = amount - Decimal("0.01")
		return (coins_list)

