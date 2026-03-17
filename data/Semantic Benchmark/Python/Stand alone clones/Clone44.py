def bubble(arr) :
	l = len(arr)
	for a in range(l) :
		for b in range(l - 1) :
			if (arr [a] < arr [b]) :
			arr [a], arr [b] = arr [b], arr [a]
	return arr


def bubble(badList) :
	length = len(badList) - 1
	unsorted = True
	while unsorted :
		unsorted = False
		for element in range(0, length) :
			if badList [element] > badList [element + 1] :
				hold = badList [element + 1]
				badList [element + 1] = badList [element]
				badList [element] = hold
				unsorted = True
		return badList

