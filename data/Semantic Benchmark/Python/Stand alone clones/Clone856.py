def choose(n, k) :
	if 0 < = k < = n :
		ntok = 1
		ktok = 1
		for t in xrange(1, min(k, n - k) + 1) :
			ntok *= n
			ktok *= t
			n -= 1
		return ntok / / ktok
	else :
		return 0


def choose(n, r) :
	assert n > = 0
	assert 0 < = r < = n
	c = 1L
	denom = 1
	for (num, denom) in zip(xrange(n, n - r, - 1), xrange(1, r + 1, 1)) :
		c = (c * num) / / denom
	return c

