def int2base(x, b, alphabet = '0123456789abcdefghijklmnopqrstuvwxyz') :
	'convert an integer to its string representation in a given base'
	if b < 2 or b > len(alphabet) :
		if b == 64 :
			alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
		else :
			raise AssertionError("int2base base out of range")
	if isinstance(x, complex) :
		return (int2base(x.real, b, alphabet), int2base(x.imag, b, alphabet))
	if x < = 0 :
		if x == 0 :
			return alphabet [0]
		else :
			return '-' + int2base(- x, b, alphabet)
	rets = ''
	while x > 0 :
		x, idx = divmod(x, b)
		rets = alphabet [idx] + rets
	return rets


def int2base(x, base) :
	if x < 0 :
		sign = - 1
	elif x == 0 :
		return digs [0]
	else :
		sign = 1
	x *= sign
	digits = []
	while x :
		digits.append(digs [int(x % base)])
		x = int(x / base)
	if sign < 0 :
		digits.append('-')
	digits.reverse()
	return ''.join(digits)

