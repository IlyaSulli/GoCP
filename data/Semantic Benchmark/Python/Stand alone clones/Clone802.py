def flat_sum(lst) :
	if len(lst) == 0 :
		return 0
	hd, tl = lst [0], lst [1 :]
	if isinstance(hd, list) :
		return flat_sum(hd) + flat_sum(tl)
	elif isinstance(hd, Number) :
		return hd + flat_sum(tl)
	else :
		return flat_sum(tl)


def flat_sum(q) :
	global total
	if not q :
		return
	if isinstance(q, list) :
		if not isinstance(q [0], list) and not isinstance(q [0], str) :
			total += q [0]
		else :
			flat_sum(q [0])
		flat_sum(q [1 :])
	else :
		if not isinstance(q, str) :
			total += q

