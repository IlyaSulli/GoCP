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


def merge(arr, p, q, r) :
	n1 = q - p + 1
	n2 = r - q
	right, left = [], []
	for i in range(n1) :
		left.append(arr [p + i])
	for j in range(n2) :
		right.append(arr [q + j + 1])
	left.append(float('inf'))
	right.append(float('inf'))
	i = j = 0
	for k in range(p, r + 1) :
		if left [i] < = right [j] :
			arr [k] = left [i]
			i += 1
		else :
			arr [k] = right [j]
			j += 1

