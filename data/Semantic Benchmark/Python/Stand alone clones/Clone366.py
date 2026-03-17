def median(x) :
	if len(x) % 2 == 0 :
		x = sorted(x)
		num = round(len(x) / 2)
		num2 = num - 1
		middlenum = (x [num] + x [num2]) / 2
	else :
		x = sorted(x)
		listlength = len(x)
		num = round(listlength / 2)
		middlenum = x [num]
	return middlenum


def median(lst) :
	quotient, remainder = divmod(len(lst), 2)
	if remainder :
		return sorted(lst) [quotient]
	return sum(sorted(lst) [quotient - 1 : quotient + 1]) / 2.

