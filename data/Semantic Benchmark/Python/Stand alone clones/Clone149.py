def main() :
	principle = decimal.Decimal(raw_input('Please enter your loan amount:'))
	rate = decimal.Decimal(raw_input('Please enter rate of interest (percent):')) / 100
	term = decimal.Decimal(raw_input('Please enter loan period (years):')) * 12
	interest = (principle * rate).quantize(decimal.Decimal('.01'), rounding = decimal.ROUND_HALF_EVEN)
	balance = principle + interest
	payment = (balance / term).quantize(decimal.Decimal('.01'), rounding = decimal.ROUND_CEILING)
	print "Payment\t\tAmount Paid\t\tRem.Bal."
	for count in range(1 + term) :
		if count == 0 :
			print count, "\t\t0.00\t\t\t", balance
		elif count == term :
			payment = balance
			balance -= payment
			print count, "\t\t", payment, "\t\t\t", balance
		else :
			balance -= payment
			print count, "\t\t", payment, "\t\t\t", balance


def main() :
	amt = getAmt('Amount borrowed ($): ')
	rate = getAmt('Interest rate (%/yr): ')
	pd = getAmt('Loan term (years): ')
	loan = MonthlyFixedPaymentLoan(amt, rate / 100, pd * 12)
	print ('')
	print (loan)
	print ('')
	print ('Month     Payment       Balance')
	print ('-----    --------    ----------')
	for mo, pay, rem in loan.payments() :
		print ('{0:>4}     ${1:>7}    ${2:>9}'.format(mo, pay, rem))

