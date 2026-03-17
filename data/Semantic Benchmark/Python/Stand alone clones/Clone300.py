def combinations(sequence, length, NULL = object()) :
	if length < = 0 :
		combos = [NULL]
	else :
		combos = []
		for i, item in enumerate(sequence, 1) :
			rem_items = sequence [i :]
			rem_combos = combinations(rem_items, length - 1)
			combos.extend(item if combo is NULL else [item, combo] for combo in rem_combos)
	return combos


def combinations(iterable, r) :
	pool = tuple(iterable)
	n = len(pool)
	if r > n :
		return
	indices = range(r)
	yield tuple(pool [i] for i in indices)
	while True :
		for i in reversed(range(r)) :
			if indices [i] ! = i + n - r :
				break
		else :
			return
		indices [i] += 1
		for j in range(i + 1, r) :
			indices [j] = indices [j - 1] + 1
		yield tuple(pool [i] for i in indices)

