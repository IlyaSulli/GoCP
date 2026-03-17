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


def bubble(values) :
	length = len(values) - 1
	sorted = False
	while not sorted :
		sorted = True
		for element in range(0, length) :
			if values [element] > values [element + 1] :
				hold = values [element + 1]
				values [element + 1] = values [element]
				values [element] = hold
				sorted = False
	return values

