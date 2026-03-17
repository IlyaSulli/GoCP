def second_largest(numbers) :
	count = 0
	m1 = m2 = float('-inf')
	for x in numbers :
		count += 1
		if x > m2 :
			if x > = m1 :
				m1, m2 = x, m1
			else :
				m2 = x
	return m2 if count > = 2 else None


def second_largest(L) :
	if (len(L) < 2) :
		raise Exception("Second_Of_One")
	KFL = None
	KFS = None
	n = 0
	for k in L :
		if (KFL == None or k > = L [KFL]) :
			KFS = KFL
			KFL = n
		elif (KFS == None or k > = L [KFS]) :
			KFS = n
		n += 1
	return (KFS)

