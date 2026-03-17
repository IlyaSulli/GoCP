def merge(a, low, mid, high) :
	l = a [low : mid + 1]
	r = a [mid + 1 : high + 1]
	k = 0; i = 0; j = 0;
	c = [0 for i in range(low, high + 1)]
	while (i < len(l) and j < len(r)) :
		if (l [i] < = r [j]) :
			c [k] = (l [i])
			k += 1
			i += 1
		else :
			c [k] = (r [j])
			j += 1
			k += 1
	while (i < len(l)) :
		c [k] = (l [i])
		k += 1
		i += 1
	while (j < len(r)) :
		c [k] = (r [j])
		k += 1
		j += 1
	a [low : high + 1] = c
	def mergesort(a, low, high) :
		if (high > low) :
			mid = (low + high) / / 2
			mergesort(a, low, mid)
			mergesort(a, mid + 1, high)
			merge(a, low, mid, high)
	a = [12, 8, 3, 2, 9, 0]
	mergesort(a, 0, len(a) - 1)
	print (a)


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

