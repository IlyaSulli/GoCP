def contains(sub, pri) :
	M, N = len(pri), len(sub)
	i, LAST = 0, M - N + 1
	while True :
		try :
			found = pri.index(sub [0], i, LAST)
		except ValueError :
			return False
		if pri [found : found + N] == sub :
			return [found, found + N - 1]
		else :
			i = found + 1


def contains(small, big) :
	for i in xrange(1 + len(big) - len(small)) :
		if small == big [i : i + len(small)] :
			return i, i + len(small) - 1
	return False

