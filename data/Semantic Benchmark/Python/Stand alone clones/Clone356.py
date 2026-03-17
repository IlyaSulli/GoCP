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


def median(array) :
	array = sorted(array)
	half, odd = divmod(len(array), 2)
	if odd :
		return array [half]
	return (array [half - 1] + array [half]) / 2.0

