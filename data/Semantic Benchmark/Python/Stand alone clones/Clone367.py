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


def median(l) :
	half = len(l) / / 2
	l.sort()
	if not len(l) % 2 :
		return (l [half - 1] + l [half]) / 2.0
	return l [half]

