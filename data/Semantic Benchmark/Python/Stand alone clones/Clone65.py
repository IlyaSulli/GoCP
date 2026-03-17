def is_sorted(lst) :
	it = iter(lst)
	try :
		prev = it.next()
	except StopIteration :
		return True
	for x in it :
		if prev > x :
			return False
		prev = x
	return True


def is_sorted(lst, key = lambda x : x) :
	for i, el in enumerate(lst [1 :]) :
		if key(el) < key(lst [i]) :
			return False
	return True

