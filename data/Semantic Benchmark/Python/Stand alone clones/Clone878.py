def sublist(a, b) :
	seq = iter(b)
	try :
		for x in a :
			while next(seq) ! = x : pass
		else :
			return True
	except StopIteration :
		pass
	return False


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

