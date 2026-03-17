def almostIncreasingSequence(sequence) :
	t = 0
	for i in range(len(sequence)) :
		temp = sequence.copy()
		del temp [i]
		if temp == sorted(temp) and not (any(i == j for i, j in zip(sorted(temp), sorted(temp) [1 :]))) :
			t += 1
	return t > 0


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

