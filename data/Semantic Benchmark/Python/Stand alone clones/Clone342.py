def binary_search(L, x) :
	i = bisect.bisect_left(L, x)
	if i == len(L) or L [i] ! = x :
		return - 1
	return i


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

