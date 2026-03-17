def binary_search(a, x, lo = 0, hi = - 1) :
	i = bisect(a, x, lo, hi)
	if i == 0 :
		return - 1
	elif a [i - 1] == x :
		return i - 1
	else :
		return - 1


def binary_search(a, x, lo = 0, hi = None) :
	if hi is None :
		hi = len(a)
	while lo < hi :
		mid = (lo + hi) / / 2
		midval = a [mid]
		if midval < x :
			lo = mid + 1
		elif midval > x :
			hi = mid
		else :
			return mid
	return - 1

