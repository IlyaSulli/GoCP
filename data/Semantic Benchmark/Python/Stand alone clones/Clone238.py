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


def flatten(x) :
	if isinstance(x, collections.Iterable) :
		return [a for i in x for a in flatten(i)]
	else :
		return [x]

