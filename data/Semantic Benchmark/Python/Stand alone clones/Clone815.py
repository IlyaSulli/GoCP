def compare(a, b) :
	i_zip = list(enumerate(zip(a, b)))
	llen = len(a)
	hp = llen / / 2
	def find_index(i_zip) :
		for i, (x, y) in i_zip :
			if x ! = y :
				return i
		return i_zip [0] [0]
	n = find_index(i_zip [: hp])
	p = find_index(i_zip [hp :])
	m = llen - p
	q = llen - n
	if a [: n] + a [p : q] + a [m : p] + a [n : m] + a [q :] ! = b :
		return None
	return n, m


def compare(A, B) :
	same = True
	for i, (a, b) in enumerate(zip(A, B)) :
		if same and a ! = b :
			same = False
			n = i
			firstval = a
		elif (not same) and (a == b or b == firstval) :
			m = i
			break
	origin = A [n : m]
	if n == 0 :
		dest = A [- m :]
		B_expect = dest + A [m : - m] + origin
	else :
		dest = A [- m : - n]
		B_expect = A [: n] + dest + A [m : - m] + origin + A [- n :]
	return bool(B_expect == B)

