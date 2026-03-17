def is_prime(x) :
	if x < 2 :
		return False
	for n in range(2, (x) - 1) :
		if x % n == 0 :
			return False
	return True


def is_prime(n) :
	if n < 2 :
		return False;
	if n % 2 == 0 :
		return n == 2
	k = 3
	while k * k < = n :
		if n % k == 0 :
			return False
		k += 2
	return True

