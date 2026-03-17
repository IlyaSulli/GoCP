def almostIncreasingSequence(sequence) :
	for i, x in enumerate(sequence) :
		ret = False
		s = sequence [: i] + sequence [i + 1 :]
		for j, y in enumerate(s [1 :]) :
			if s [j + 1] < = s [j] :
				ret = True
				break
			if ret :
				break
		if not ret :
			return True
	return False


def almostIncreasingSequence(sequence) :
	j = first_bad_pair(sequence, - 1)
	if j == - 1 :
		return True
	if first_bad_pair(sequence, j) == - 1 :
		return True
	if first_bad_pair(sequence, j + 1) == - 1 :
		return True
	return False

