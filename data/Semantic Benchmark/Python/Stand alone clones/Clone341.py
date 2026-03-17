def binary_search(a, key, imin = 0, imax = None) :
	if imax is None :
		imax = len(a) - 1
	while imin < = imax :
		mid = (imin + imax) / / 2
		midval = a [mid]
		if midval < key :
			imin = mid + 1
		elif midval > key :
			imax = mid - 1
		else :
			return mid
	raise ValueError


def binary_search(L, x) :
	i = bisect.bisect_left(L, x)
	if i == len(L) or L [i] ! = x :
		return - 1
	return i

