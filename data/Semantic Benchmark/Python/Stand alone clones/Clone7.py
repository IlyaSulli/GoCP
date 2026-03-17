def factors(n) :
	f = 2
	increments = itertools.chain([1, 2, 2], itertools.cycle([4, 2, 4, 2, 4, 6, 2, 6]))
	for incr in increments :
		if f * f > n :
			break
		while n % f == 0 :
			yield f
			n //= f
		f += incr
	if n > 1 :
		yield n


def factors(n) :
	gaps = [1, 2, 2, 4, 2, 4, 2, 4, 6, 2, 6]
	length, cycle = 11, 3
	f, fs, nxt = 2, [], 0
	while f * f < = n :
		while n % f == 0 :
			fs.append(f)
			n /= f
		f += gaps [nxt]
		nxt += 1
		if nxt == length :
			nxt = cycle
	if n > 1 : fs.append(n)
	return fs

