def find(l, elem) :
	for row, i in enumerate(l) :
		try :
			column = i.index(elem)
		except ValueError :
			continue
		return row, column
	return - 1


def find(needle, haystack) :
	if needle == haystack : return []
	if isinstance(haystack, str) and len(haystack) < = 1 : return None
	try :
		for i, e in enumerate(haystack) :
			r = find(needle, e)
			if r is not None :
				r.insert(0, i)
				return r
	except TypeError :
		pass
	return None

