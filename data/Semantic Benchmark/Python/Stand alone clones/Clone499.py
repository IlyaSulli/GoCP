def matched(str) :
	ope = []
	clo = []
	for i in range(0, len(str)) :
		l = str [i]
		if l == "(" :
			ope = ope + ["("]
		elif l == ")" :
			clo = clo + [")"]
	if len(ope) == len(clo) :
		return True
	else :
		return False


def matched(str) :
	count = 0
	for i in str :
		if i == "(" :
			count += 1
		elif i == ")" :
			count -= 1
		if count < 0 :
			return False
	return count == 0

