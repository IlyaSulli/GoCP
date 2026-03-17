def merge(left, right, compare) :
	result = []
	i, j = 0, 0
	while i < len(left) and j < len(right) :
		if compare(left [i], right [j]) :
			result.append(left [i])
			i += 1
		else :
			result.append(right [j])
			j += 1
	while i < len(left) :
		result.append(left [i])
		i += 1
	while j < len(right) :
		result.append(right [j])
		j += 1
	return result


def merge(x) :
	if len(x) == 1 :
		return x
	else :
		mid = int(len(x) / 2)
		l = merge(x [: mid])
		r = merge(x [mid :])
	i = j = 0
	result = []
	while i < len(l) and j < len(r) :
		if l [i] < r [j] :
			result.append(l [i])
			i += 1
		else :
			result.append(r [j])
			j += 1
	result += l [i :]
	result += r [j :]
	return result

