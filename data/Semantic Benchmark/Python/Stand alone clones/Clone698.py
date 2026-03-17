def biggest() :
	big_x, big_y, max_seen = 0, 0, 0
	for x in xrange(999, 99, - 1) :
		for y in xrange(x, 99, - 1) :
			if x * y < max_seen : continue
			if is_palindrome(x * y) :
				big_x, big_y, max_seen = x, y, x * y
	return big_x, big_y, max_seen


def biggest() :
	big_x, big_y, max_seen, prod = 0, 0, 0, 0
	for r in xrange(maxFactor, minFactor - 1, - 1) :
		if r * r < max_seen : break
		for i in xrange(0, maxFactor - r + 1) :
			prod = (r + i) * (r - i)
			if prod < max_seen : break
			if is_palindrome(prod) :
				big_x, big_y, max_seen = r + i, r - i, prod
		for i in xrange(0, maxFactor - r + 1) :
			prod = (r + i) * (r - i - 1)
			if prod < max_seen : break
			if is_palindrome(prod) :
				big_x, big_y, max_seen = r + i, r - i - 1, prod
	return big_x, big_y, max_seen

