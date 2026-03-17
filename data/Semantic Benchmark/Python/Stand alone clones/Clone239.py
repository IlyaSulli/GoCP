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


def flatten(seq) :
	l = []
	for elt in seq :
		t = type(elt)
		if t is tuple or t is list :
			for elt2 in flatten(elt) :
				l.append(elt2)
		else :
			l.append(elt)
	return l

