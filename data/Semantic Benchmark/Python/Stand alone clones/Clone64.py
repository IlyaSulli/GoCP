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


def is_sorted(lst) :
	try :
		sorted(lst, cmp = my_cmp)
		return True
	except ValueError :
		return False

