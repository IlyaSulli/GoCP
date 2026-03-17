def transform_non_affine(self, a) :
	result = np.empty_like(a)
	a_idx = 0
	csum = 0
	for left, right in self._breaks :
		while a_idx < len(a) and a [a_idx] < left :
			result [a_idx] = a [a_idx] - csum
			a_idx += 1
		while a_idx < len(a) and a [a_idx] < = right :
			result [a_idx] = left - csum
			a_idx += 1
		csum += right - left
	while a_idx < len(a) :
		result [a_idx] = a [a_idx] - csum
		a_idx += 1
	return result


def transform_non_affine(self, a) :
	diff = np.zeros(len(a))
	total_shift = 0
	for left, right in self._breaks :
		pos = bisect.bisect_right(a, left - total_shift)
		if pos > = len(diff) :
			break
		diff [pos] = right - left
		total_shift += right - left
	return a + diff.cumsum()

