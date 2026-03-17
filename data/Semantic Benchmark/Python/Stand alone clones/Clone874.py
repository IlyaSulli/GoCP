def sublist(a, b) :
	last = 0
	for el_a in a :
		if el_a in b [last :] :
			last = b [last :].index(el_a)
		else :
			return False
	return True


def sublist(x, y) :
	if x and not y :
		return False
	i, lim = 0, len(y)
	for e in x :
		while e ! = y [i] :
			i += 1
			if i == lim :
				return False
		i += 1
	return True

