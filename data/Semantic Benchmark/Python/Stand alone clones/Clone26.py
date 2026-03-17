def most_common(iterable) :
	lst = [(x, i) for i, x in enumerate(iterable)]
	lst.sort()
	lst_final = []
	itr = iter(lst)
	count = 1
	tup = next(itr)
	x_cur, i_cur = tup
	for tup in itr :
		if x_cur == tup [0] :
			count += 1
		else :
			t = (- count, i_cur, x_cur)
			lst_final.append(t)
			x_cur, i_cur = tup
			count = 1
	t = (- count, i_cur, x_cur)
	lst_final.append(t)
	lst_final.sort()
	answer = lst_final [0] [2]
	return answer


def most_common(L) :
	SL = sorted((x, i) for i, x in enumerate(L))
	groups = itertools.groupby(SL, key = operator.itemgetter(0))
	def _auxfun(g) :
		item, iterable = g
		count = 0
		min_index = len(L)
		for _, where in iterable :
			count += 1
			min_index = min(min_index, where)
		return count, - min_index
	return max(groups, key = _auxfun) [0]

