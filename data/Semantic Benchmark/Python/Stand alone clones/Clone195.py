def factors(num) :
	numroot = int(math.sqrt(num)) + 1
	for i in xrange(2, numroot) :
		divider, remainder = divmod(num, i)
		if not remainder :
			yield i
			break
	else :
		yield num
		return
	for factor in factors(divider) :
		yield factor


def factors(n) :
	i = 2
	while n > 1 :
		p = 0
		while n > 1 and n % i == 0 :
			p += 1
			n /= i
		if p :
			yield (i, p)
		i += 1

