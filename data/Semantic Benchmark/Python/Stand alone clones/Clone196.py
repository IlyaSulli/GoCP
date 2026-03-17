def factorize(n) :
	divisors = itertools.count(2)
	divisor = divisors.next()
	while True :
		if divisor ** 2 > n :
			yield n
			break
		a, b = divmod(n, divisor)
		if b == 0 :
			yield divisor
			n = a
		else :
			divisor = divisors.next()


def factorize(n) :
	divisors = itertools.count(2)
	for divisor in divisors :
		if divisor ** 2 > n :
			yield n
			break
		while n % divisor == 0 :
			yield divisor
			n //= divisor

