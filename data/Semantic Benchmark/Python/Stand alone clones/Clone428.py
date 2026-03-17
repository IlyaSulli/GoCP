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


def mssl(x) :
	max_ending_here = max_so_far = 0
	for a in x :
		max_ending_here = max(0, max_ending_here + a)
		max_so_far = max(max_so_far, max_ending_here)
	return max_so_far

