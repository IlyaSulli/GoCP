def flatten(xs) :
	res = []
	def loop(ys) :
		for i in ys :
			if isinstance(i, list) :
				loop(i)
			else :
				res.append(i)
	loop(xs)
	return res


def flatten(TheList) :
	listIsNested = True
	while listIsNested :
		keepChecking = False
		Temp = []
		for element in TheList :
			if isinstance(element, list) :
				Temp.extend(element)
				keepChecking = True
			else :
				Temp.append(element)
		listIsNested = keepChecking
		TheList = Temp [:]
	return TheList

