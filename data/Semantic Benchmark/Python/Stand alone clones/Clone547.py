def is_prime(x) :
	if x < 2 :
		return False
	for n in range(2, (x) - 1) :
		if x % n == 0 :
			return False
	return True


def is_prime(n) :
	if n == 2 or n == 3 : return True
	if n < 2 or n % 2 == 0 : return False
	if n < 9 : return True
	if n % 3 == 0 : return False
	r = int(n ** 0.5)
	f = 5
	while f < = r :
		print '\t', f
		if n % f == 0 : return False
		if n % (f + 2) == 0 : return False
		f += 6
	return True

