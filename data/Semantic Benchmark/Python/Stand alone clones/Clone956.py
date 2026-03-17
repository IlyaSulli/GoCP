def calculate_tax(people) :
	while True :
		try :
			iterating_people = people.keys()
			for key in iterating_people :
				earning = people [key]
				if earning < = 1000 :
					people [key] = 0
				elif earning in range(1001, 10001) :
					tax1 = 0 * 1000
					tax2 = 0.1 * (earning - 1000)
					total_tax = tax1 + tax2
					people [key] = total_tax
				elif earning in range(10001, 20201) :
					tax1 = 0 * 1000
					tax2 = 0.1 * 9000
					tax3 = 0.15 * (earning - 10000)
					total_tax = tax1 + tax2 + tax3
					people [key] = total_tax
				elif earning in range(20201, 30751) :
					tax1 = 0 * 1000
					tax2 = 0.1 * 9000
					tax3 = 0.15 * 10200
					tax4 = 0.20 * (earning - 20200)
					total_tax = tax1 + tax2 + tax3 + tax4
					people [key] = total_tax
				elif earning in range(30751, 50001) :
					tax1 = 0 * 1000
					tax2 = 0.1 * 9000
					tax3 = 0.15 * 10200
					tax4 = 0.20 * 10550
					tax5 = 0.25 * (earning - 30750)
					total_tax = tax1 + tax2 + tax3 + tax4 + tax5
					people [key] = total_tax
				elif earning > 50000 :
					tax1 = 0 * 1000
					tax2 = 0.1 * 9000
					tax3 = 0.15 * 10200
					tax4 = 0.20 * 10550
					tax5 = 0.25 * 19250
					tax6 = 0.3 * (earning - 50000)
					total_tax = tax1 + tax2 + tax3 + tax4 + tax5 + tax6
					people [key] = total_tax
			return people
			break
		except (AttributeError, TypeError) :
			raise ValueError('The provided input is not a dictionary')


def calculate_tax(income_input) :
	for item in income_input :
		income = income_input [item]
		if (income > = 0) and (income < = 1000) :
			tax = (0 * income)
		elif (income > 1000) and (income < = 10000) :
			tax = (0.1 * (income - 1000))
		elif (income > 10000) and (income < = 20200) :
			tax = ((0.1 * (10000 - 1000)) + (0.15 * (income - 10000)))
		elif (income > 20200) and (income < = 30750) :
			tax = ((0.1 * (10000 - 1000)) + (0.15 * (20200 - 10000)) + (0.2 * (income - 20200)))
		elif (income > 30750) and (income < = 50000) :
			tax = ((0.1 * (10000 - 1000)) + (0.15 * (20200 - 10000)) + (0.2 * (30750 - 20200)) + (0.25 * (income - 30750)))
		elif (income > 50000) :
			tax = ((0.1 * (10000 - 1000)) + (0.15 * (20200 - 10000)) + (0.2 * (30750 - 20200)) + (0.25 * (50000 - 30750)) + (0.3 * (income - 50000)))
		else :
			pass
		income_input [item] = int(tax)
	return income_input

