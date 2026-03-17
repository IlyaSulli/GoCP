def issorted(vec, ascending = True) :
	if len(vec) < 2 :
		return True
	if ascending :
		for i in range(1, len(vec)) :
			if vec [i - 1] > vec [i] :
				return False
		return True
	else :
		for i in range(1, len(vec)) :
			if vec [i - 1] < vec [i] :
				return False
		return True


def issorted(x) :
	try :
		if x.dtype.kind == 'u' :
			x = numpy.int64(x)
	except AttributeError :
		pass
	return (numpy.diff(x) > = 0).all()

