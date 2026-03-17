def mssl(l) :
	best = cur = 0
	curi = starti = besti = 0
	for ind, i in enumerate(l) :
		if cur + i > 0 :
			cur += i
		else :
			cur, curi = 0, ind + 1
		if cur > best :
			starti, besti, best = curi, ind + 1, cur
	return starti, besti, best


def mssl(lst, return_sublist = False) :
	d = defaultdict(list)
	for i in range(len(lst) + 1) :
		for j in range(len(lst) + 1) :
			d [sum(lst [i : j])].append(lst [i : j])
	key = max(d.keys())
	if return_sublist :
		return (key, d [key])
	return key

