def sublist(a, b) :
	index_a = 0
	index_b = 0
	len_a = len(a)
	len_b = len(b)
	while index_a < len_a and index_b < len_b :
		if a [index_a] == b [index_b] :
			index_a += 1
			index_b += 1
		else :
			index_b += 1
	return index_a == len_a


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

