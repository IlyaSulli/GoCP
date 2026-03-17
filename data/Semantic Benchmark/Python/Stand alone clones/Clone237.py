def flatten(xs) :
	res = []
	def loop(ys) :
		for i in ys :
			if isinstance(i, list) :
				loop(i)
			else :
				res.append(i)
	loop(xs)
	return res


def flatten(seq) :
	l = []
	for elt in seq :
		t = type(elt)
		if t is tuple or t is list :
			for elt2 in flatten(elt) :
				l.append(elt2)
		else :
			l.append(elt)
	return l

