def f(n, _sequence = None) :
	if _sequence is None :
		_sequence = [0] * (n + 1)
	if n == 0 or n == 1 :
		val = n
	else :
		f(n - 1, _sequence)
		f(n - 2, _sequence)
		val = 0.5 * (_sequence [n - 1] + _sequence [n - 2])
	_sequence [n] = val
	return _sequence


def f(n) :
	def aux(n, acc, a, b) :
		if n == 0 :
			return acc + [a]
		else :
			return aux(n - 1, acc + [a], b, 0.5 * (a + b))
	return aux(n, [], 0, 1)

