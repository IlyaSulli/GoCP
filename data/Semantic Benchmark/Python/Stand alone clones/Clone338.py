def binary_search(a, x, lo = 0, hi = - 1) :
	i = bisect(a, x, lo, hi)
	if i == 0 :
		return - 1
	elif a [i - 1] == x :
		return i - 1
	else :
		return - 1


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

