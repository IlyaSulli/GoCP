def mssl(lst, return_sublist = False) :
	d = defaultdict(list)
	for i in range(len(lst) + 1) :
		for j in range(len(lst) + 1) :
			d [sum(lst [i : j])].append(lst [i : j])
	key = max(d.keys())
	if return_sublist :
		return (key, d [key])
	return key


def mssl(x) :
	max_ending_here = max_so_far = 0
	for a in x :
		max_ending_here = max(0, max_ending_here + a)
		max_so_far = max(max_so_far, max_ending_here)
	return max_so_far

