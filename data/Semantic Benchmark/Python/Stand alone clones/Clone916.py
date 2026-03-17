def prime_factors(n) :
	factors = []
	d = 2
	while (d * d < = n) :
		while (n > 1) :
			while n % d == 0 :
				factors.append(d)
				n = n / d
			d += 1
	return factors [- 1]


def prime_factors(n) :
	i = 2
	factors = []
	while i * i < = n :
		if n % i :
			i += 1
		else :
			n //= i
			factors.append(i)
	if n > 1 :
		factors.append(n)
	return factors

