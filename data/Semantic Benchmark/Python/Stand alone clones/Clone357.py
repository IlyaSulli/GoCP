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


def median(lst) :
	quotient, remainder = divmod(len(lst), 2)
	if remainder :
		return sorted(lst) [quotient]
	return sum(sorted(lst) [quotient - 1 : quotient + 1]) / 2.

