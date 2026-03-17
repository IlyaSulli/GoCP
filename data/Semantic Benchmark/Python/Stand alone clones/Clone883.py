def sublist(a, b) :
	i = - 1
	try :
		for e in a :
			i = b.index(e, i + 1)
	except ValueError :
		return False
	else :
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

