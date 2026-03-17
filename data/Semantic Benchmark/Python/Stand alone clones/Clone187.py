def ask_digit() :
	while True :
		digit = raw_input("Please enter a number between 1 and 5: ")
		if re.match(r"[1-5]$", digit) :
			return int(digit)


def ask_digit(calls = 0) :
	if calls > 10 :
		print "You are so boring..."
		raise ValueError("Can't get answer from user")
	try :
		num = int(raw_input("Enter number 1-5: "))
	except ValueError :
		print "Not a digit"
		return ask_digit(calls + 1)
	if num < 1 or num > 5 :
		print "Not valid"
		return ask_digit(calls + 1)
	return num

