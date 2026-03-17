def paren(n, known = {}) :
	if n in known :
		return known [n]
	ps = set(['(' * n + ')' * n])
	for i in range(1, n) :
		for f in paren(i, known) :
			for s in paren(n - i, known) :
				ps.add(f + s)
	known [n] = ps
	return ps


def paren(left, right = None) :
	if right is None :
		right = left
	if left == right == 0 :
		yield ""
	else :
		if left > 0 :
			for p in paren(left - 1, right) :
				yield "(" + p
		if right > left :
			for p in paren(left, right - 1) :
				yield ")" + p

