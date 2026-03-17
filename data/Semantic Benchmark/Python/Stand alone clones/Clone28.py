def most_common(lst) :
	cur_length = 0
	max_length = 0
	cur_i = 0
	max_i = 0
	cur_item = None
	max_item = None
	for i, item in sorted(enumerate(lst), key = lambda x : x [1]) :
		if cur_item is None or cur_item ! = item :
			if cur_length > max_length or (cur_length == max_length and cur_i < max_i) :
				max_length = cur_length
				max_i = cur_i
				max_item = cur_item
			cur_length = 1
			cur_i = i
			cur_item = item
		else :
			cur_length += 1
	if cur_length > max_length or (cur_length == max_length and cur_i < max_i) :
		return cur_item
	return max_item


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

