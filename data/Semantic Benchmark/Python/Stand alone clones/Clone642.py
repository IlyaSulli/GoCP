def myMin(mylist) :
	smallest = float('inf')
	for l in mylist :
		if isinstance(l, list) :
			tmp = myMin(l)
			if tmp < smallest :
				smallest = tmp
		elif l < smallest :
			smallest = l
	if smallest == float('inf') :
		return None
	return smallest


def myMin(lst) :
	smallest = None
	for i in lst :
		if isinstance(i, list) :
			i = myMin(i)
		if smallest is None or i is not None and i < smallest :
			smallest = i
	return smallest

