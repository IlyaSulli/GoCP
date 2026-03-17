def consec(n, iterable) :
	result = set()
	prev = None
	count = 0
	for item in iterable :
		if item == prev :
			count += 1
			if count == n :
				result.add(prev)
		else :
			prev = item
			count = 1
	return result


def consec(n, l) :
	it = iter(l)
	prev = next(it)
	st = set()
	while prev ! = "" :
		for i in range(n - 1) :
			ele = next(it, "")
			if ele ! = prev or ele == "" :
				break
			prev = ele
		else :
			st.add(ele)
		prev = ele
	return st

