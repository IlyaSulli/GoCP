def primes(n) :
	primfac = []
	d = 2
	while d * d < = n :
		while (n % d) == 0 :
			primfac.append(d)
			n //= d
		d += 1
	if n > 1 :
		primfac.append(n)
	return primfac


def primes(n) :
	if n < 2 : return
	yield 2
	plist = [2]
	for i in range(3, n) :
		test = True
		for j in plist :
			if j > n ** 0.5 :
				break
			if i % j == 0 :
				test = False
				break
		if test :
			plist.append(i)
			yield i

