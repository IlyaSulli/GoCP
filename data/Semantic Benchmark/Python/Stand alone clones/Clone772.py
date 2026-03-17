def bitwise_or(num1, num2) :
	new_num1 = list(num1 [2 :])
	new_num2 = list(num2 [2 :])
	if len(num1) > len(num2) :
		new_num2 [: 0] = '0' * (len(num1) - len(num2))
	elif len(num1) < len(num2) :
		new_num1 [: 0] = '0' * (len(num2) - len(num1))
	new_num = []
	for c1, c2 in zip(new_num1, new_num2) :
		if c1 == "1" or c2 == "1" :
			new_num.append("1")
		else :
			new_num.append(c1)
	return '0b' + ''.join(new_num)


def bitwise_or(num1, num2) :
	new_num1 = []
	new_num2 = []
	new_num = []
	for c in num1 [2 :] :
		new_num1.append(c)
	for c in num2 [2 :] :
		new_num2.append(c)
	if len(num1) ! = len(num2) :
		if len(num1) > len(num2) :
			diff1 = ["0"] * (len(num1) - len(num2))
			new_num2 = diff1 + new_num2
		if len(num1) < len(num2) :
			diff1 = ["0"] * (len(num2) - len(num1))
			new_num1 = diff1 + new_num1
	for i in range(len(new_num1)) :
		if new_num1 [i] == "1" or new_num2 [i] == "1" :
			new_num.append("1")
		else :
			new_num.append(new_num1 [i])
	final = "".join(new_num)
	return final

