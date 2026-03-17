def almostIncreasingSequence(list) :
	removedIdx = []
	for idx, item in enumerate(list) :
		tmp = []
		for i in range(idx - 1, - 1, - 1) :
			if list [idx] < = list [i] :
				tmp.append(i)
		if len(tmp) > 1 :
			removedIdx.append(idx)
		else :
			if len(tmp) > 0 :
				removedIdx.append(tmp [0])
	return len(set(removedIdx)) < = 1


def almostIncreasingSequence(sequence) :
	j = first_bad_pair(sequence, - 1)
	if j == - 1 :
		return True
	if first_bad_pair(sequence, j) == - 1 :
		return True
	if first_bad_pair(sequence, j + 1) == - 1 :
		return True
	return False

