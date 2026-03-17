def median(midlist) :
	midlist.sort()
	lens = len(midlist)
	if lens % 2 ! = 0 :
		midl = (lens / 2)
		res = midlist [midl]
	else :
		odd = (lens / 2) - 1
		ev = (lens / 2)
		res = float(midlist [odd] + midlist [ev]) / float(2)
	return res


def median(l) :
	half = len(l) / / 2
	l.sort()
	if not len(l) % 2 :
		return (l [half - 1] + l [half]) / 2.0
	return l [half]

