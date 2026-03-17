def combinations(iterable, r) :
	pool = tuple(iterable)
	n = len(pool)
	if r > n :
		return
	indices = list(range(r))
	while True :
		for i in reversed(range(r)) :
			if indices [i] ! = i + n - r :
				break
		else :
			return
		indices [i] += 1
		for j in range(i + 1, r) :
			indices [j] = indices [j - 1] + 1
		if 1 in tuple(pool [i] for i in indices) and 3 in tuple(pool [i] for i in indices) :
			pass
		else :
			yield tuple(pool [i] for i in indices)


def combinations(iterable, r, combIndeciesExclusions = set()) :
	pool = tuple(iterable)
	n = len(pool)
	for indices in permutations(range(n), r) :
		if (len(combIndeciesExclusions) == 0 or not combIndeciesExclusions.issubset(indices)) and sorted(indices) == list(indices) :
			yield tuple(pool [i] for i in indices)

