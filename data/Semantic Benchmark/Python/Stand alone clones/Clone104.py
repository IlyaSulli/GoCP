def lone_sum(* args) :
	d = defaultdict(int)
	for x in args :
		d [x] += 1
	return sum(val for val, apps in d.iteritems() if apps == 1)


def lone_sum(* args) :
	seen = set()
	summands = set()
	for x in args :
		if x not in seen :
			summands.add(x)
			seen.add(x)
		else :
			summands.discard(x)
	return sum(summands)

