def merge(left_side, right_side) :
	result = []
	while len(left_side) > 0 or len(right_side) > 0 :
		if len(left_side) > 0 and len(right_side) > 0 :
			if left_side [0] < = right_side [0] :
				result.append(left_side.pop(0))
			else :
				result.append(right_side.pop(0))
		elif len(left_side) > 0 :
			result.append(left_side.pop(0))
		elif len(right_side) > 0 :
			result.append(right_side.pop(0))
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

