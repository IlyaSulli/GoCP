def most_common(l) :
	try :
		return mode(l)
	except StatisticsError as e :
		if 'no unique mode' in e.args [0] :
			return l [0]
		raise


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

