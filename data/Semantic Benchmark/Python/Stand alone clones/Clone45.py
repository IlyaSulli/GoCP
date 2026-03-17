def bubble(arr) :
	l = len(arr)
	for a in range(l) :
		for b in range(l - 1) :
			if (arr [a] < arr [b]) :
			arr [a], arr [b] = arr [b], arr [a]
	return arr


def bubble(badList) :
	length = len(badList) - 1
	element = 0
	while element < length :
		if badList [element] > badList [element + 1] :
			hold = badList [element + 1]
			badList [element + 1] = badList [element]
			badList [element] = hold
			element = 0
			print badList
		else :
			element = element + 1

