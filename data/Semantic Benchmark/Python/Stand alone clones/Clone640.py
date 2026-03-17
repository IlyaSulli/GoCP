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

