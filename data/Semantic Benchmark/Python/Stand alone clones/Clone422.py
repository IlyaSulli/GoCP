def getPrimes(n) :
	i = 2
	while i < n :
		prime = True
		for a in xrange(2, i) :
			if i % a == 0 :
				prime = False
				break
		if prime :
			yield i
		i += 1


def getPrimes(n) :
	yield 2
	i = 1
	while i < = n - 2 :
		i += 2
		if isprime(i) :
			yield i

