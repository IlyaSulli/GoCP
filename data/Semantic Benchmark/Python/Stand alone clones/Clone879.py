def sublist(a, b) :
	if not a :
		return True
	for k in range(len(b)) :
		if a [0] == b [k] :
			return sublist(a [1 :], b [k + 1 :])
	return False


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

