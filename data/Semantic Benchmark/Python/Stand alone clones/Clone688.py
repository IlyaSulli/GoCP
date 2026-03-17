def go(iterable) :
	itr = iter(iterable)
	try :
		next(num for num in itr if num % 2 == 1)
		return next(i for i, num in enumerate(itr, 1) if num % 2 == 0)
	except StopIteration :
		return - 1


def go(list1) :
	odd = None
	even = None
	for i in range(0, len(list1)) :
		if list1 [i] % 2 == 1 :
			odd = i
			break
	if odd is not None :
		for i in range(odd, len(list1)) :
			if list1 [i] % 2 == 0 :
				even = i
				break
	if odd is None or even is None :
		return - 1
	else :
		return even - odd

