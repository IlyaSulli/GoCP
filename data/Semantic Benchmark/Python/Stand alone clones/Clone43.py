def bubble_sort(l) :
	exchanged = True
	iteration = 0
	n = len(l)
	while (exchanged) :
		iteration += 1
		exchanged = False
		for i in range(n - 1) :
			if l [i] > l [i + 1] :
				exchanged = True
				l [i], l [i + 1] = l [i + 1], l [i]
		n -= 1
	print 'Iterations: %s' % (iteration)
	return l


def bubble_sort(l) :
	for passes_left in range(len(l) - 1, 0, - 1) :
		for index in range(passes_left) :
			if l [index] < l [index + 1] :
				l [index], l [index + 1] = l [index + 1], l [index]
	return l

